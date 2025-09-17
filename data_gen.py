#!/usr/bin/env python3
import os
import uuid
import random
import json
import csv
import base64
from datetime import datetime
from faker import Faker
import pyarrow as pa
import pyarrow.parquet as pq

# --- Configuration ---
NUM_RECORDS = 5000    # total number of records (change as needed)
BATCH_SIZE = 1000     # chunk size for streaming (tune for your machine)

OUTPUT_BASE = "output_data"
OUTPUT_DIR = f"{OUTPUT_BASE}_{NUM_RECORDS}"

FORMATS = {
    "csv": True,
    "jsonl": True,
    "xml": True,
    "sql": True,
    "parquet": False,
}

# SQL dialect for SQL file generation:
# options: "generic" (portable, base64/text), "mysql", "postgres", "mssql", "oracle"
SQL_DIALECT = "generic"

TABLE_NAME_BASE = "people"
TABLE_NAME = f"{TABLE_NAME_BASE}_{NUM_RECORDS}"

# New parameter: Set to True to make 'id' a primary key with auto-increment behavior
PRIMARY_KEY = True
if  PRIMARY_KEY:
    TABLE_NAME = f"{TABLE_NAME_BASE}_{NUM_RECORDS}_with_PK"
    OUTPUT_DIR = f"{OUTPUT_DIR}_WITH_PK"

# Null-/empty-value config
GLOBAL_NULL_PROB = 0.1
COLUMN_NULL_PROBS = {}


SCHEMA = [
    ("id", "int"),
    ("uuid", "uuid"),
    ("first_name", "str"),
    ("last_name", "str"),
    ("email", "email"),
    ("signup_date", "date"),
    ("signup_datetime", "datetime"),
    ("is_active", "bool"),
    ("score", "float"),
    ("balance", "decimal"),
    ("age", "int_small"),
    ("country_code", "str_fixed_2"),
    ("profile_json", "json"),
    ("notes", "text_long"),
    ("profile_picture", "binary_blob"),
    ("last_login", "datetime_nullable"),
    ("rating", "enum_1_to_5"),
    ("tags", "list_str"),
]

# --- Setup ---
fake = Faker()
Faker.seed(1234)
random.seed(1234)

# --- Helpers ---
def should_null(col_name):
    if col_name == "id":
        return False
    if col_name in COLUMN_NULL_PROBS:
        p = COLUMN_NULL_PROBS[col_name]
    else:
        p = GLOBAL_NULL_PROB
    return random.random() < p

def gen_value(typ, col_name):
    if should_null(col_name):
        return None
    if typ == "int":
        return random.randint(1, 10**9)
    elif typ == "uuid":
        return str(uuid.uuid4())
    elif typ == "str":
        return fake.first_name()
    elif typ == "str_fixed_2":
        # 2-letter code; fallback if Faker returns 3
        code = fake.country_code()
        return code[:2]
    elif typ == "email":
        # don't use unique across massive ranges to avoid exhaustion; it's fine for testing
        return fake.email()
    elif typ == "date":
        return fake.date_between(start_date='-10y', end_date='today')
    elif typ == "datetime":
        return fake.date_time_between(start_date='-5y', end_date='now')
    elif typ == "datetime_nullable":
        return fake.date_time_between(start_date='-5y', end_date='now')
    elif typ == "bool":
        return random.choice([True, False])
    elif typ == "float":
        return round(random.uniform(0, 10000), 2)
    elif typ == "decimal":
        return round(random.uniform(-1000000, 1000000), 4)
    elif typ == "int_small":
        return random.randint(0, 32767)
    elif typ == "json":
        return {
            "preferences": {
                "theme": random.choice(["light", "dark"]),
                "newsletter": random.choice([True, False]),
            },
            "settings": {
                "notifications": random.choice(["all", "email", "sms", "none"])
            },
        }
    elif typ == "binary_blob":
        # small binary sample; you can increase size if needed
        return os.urandom(16)
    elif typ == "enum_1_to_5":
        return random.choice([1,2,3,4,5])
    elif typ == "list_str":
        n = random.randint(0, 4)
        return [fake.word() for _ in range(n)]
    elif typ == "text_long":
        return fake.text(max_nb_chars=200)
    else:
        return None

def sql_col_type(typ, col, dialect):
    # Return SQL column type for given schema type and dialect
    # Keep conservative, portable mappings
    type_str = ""
    if typ == "int":
        type_str = "INT"
    if typ == "int_small":
        type_str = "SMALLINT"
    if typ == "uuid":
        type_str = "CHAR(36)"
    if typ in ("str", "str_fixed_2", "email"):
        type_str = "VARCHAR(150)"
    if typ == "date":
        type_str = "DATE"
    if typ in ("datetime", "datetime_nullable"):
        type_str = "TIMESTAMP"
    if typ == "bool":
        # BOOLEAN supported by many engines; fallback SMALLINT where necessary
        type_str = "BOOLEAN" if dialect != "oracle" else "NUMBER(1)"
    if typ == "float":
        type_str = "FLOAT"
    if typ == "decimal":
        type_str = "DECIMAL(18,4)"
    if typ == "json":
        # Not all engines have JSON type; generic TEXT is safer
        type_str = "JSON" if dialect in ("postgres",) else "TEXT"
    if typ == "binary_blob":
        if dialect == "postgres":
            type_str = "BYTEA"
        if dialect == "mssql":
            type_str = "VARBINARY(MAX)"
        if dialect == "oracle":
            type_str = "BLOB"
        # mysql, mariadb, generic -> BLOB or TEXT if generic
        type_str = "BLOB" if dialect in ("mysql", "mariadb") else "TEXT"
    if typ in ("text_long", "list_str"):
        type_str = "TEXT"
    if typ == "enum_1_to_5":
        type_str = "SMALLINT"
    
    # Add PRIMARY KEY and AUTO_INCREMENT/IDENTITY if applicable
    if col == "id" and PRIMARY_KEY:
        if dialect == "postgres":
            return "SERIAL PRIMARY KEY"
        elif dialect == "mysql":
            return "INT AUTO_INCREMENT PRIMARY KEY"
        elif dialect == "mssql":
            return "INT IDENTITY(1,1) PRIMARY KEY"
        else: # generic/oracle
            return "INT PRIMARY KEY"
    
    return type_str

def sql_encode_binary(bytes_val, dialect):
    # Convert raw bytes to SQL literal per dialect
    if bytes_val is None:
        return "NULL"
    hexed = bytes_val.hex()
    if dialect in ("mysql", "mariadb", "mssql"):
        # 0xHEX
        return "0x" + hexed
    if dialect == "postgres":
        # E'\\xHEX' (note double-escaped backslash for file)
        return "E'\\\\x" + hexed + "'"
    if dialect == "oracle":
        # HEXTORAW('HEX')
        return f"HEXTORAW('{hexed}')"
    # generic: base64 string wrapped as quoted TEXT (portable)
    b64 = base64.b64encode(bytes_val).decode('ascii')
    s = b64.replace("'", "''")
    return f"'{s}'"

def format_sql_value(val, typ, dialect):
    # Format a Python value into a SQL literal for the chosen dialect
    if val is None:
        return "NULL"
    if typ in ("int", "int_small", "enum_1_to_5"):
        return str(val)
    if typ in ("float", "decimal"):
        return str(val)
    if typ == "date":
        return f"'{val.isoformat()}'"
    if typ in ("datetime", "datetime_nullable"):
        return f"'{val.strftime('%Y-%m-%d %H:%M:%S')}'"
    if typ == "bool":
        # MySQL and Postgres accept TRUE/FALSE; Oracle uses 1/0
        if dialect == "oracle":
            return "1" if val else "0"
        return "TRUE" if val else "FALSE"
    if typ == "uuid":
        s = str(val).replace("'", "''")
        return f"'{s}'"
    if typ == "binary_blob":
        return sql_encode_binary(val, dialect)
    # strings, json, lists -> quote and escape
    if typ == "json":
        s = json.dumps(val).replace("'", "''")
        return f"'{s}'"
    if typ == "list_str":
        if val is None:
            return "NULL"
        s = ",".join(val).replace("'", "''")
        return f"'{s}'"
    # default string/text
    s = str(val).replace("'", "''")
    return f"'{s}'"

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# --- Main streaming generator/writer ---
def stream_generate_and_write():
    ensure_dir(OUTPUT_DIR)

    csv_file_path = os.path.join(OUTPUT_DIR, f"data_{NUM_RECORDS}.csv")
    jsonl_file_path = os.path.join(OUTPUT_DIR, f"data_{NUM_RECORDS}.jsonl")
    xml_file_path = os.path.join(OUTPUT_DIR, f"data_{NUM_RECORDS}.xml")
    sql_file_path = os.path.join(OUTPUT_DIR, f"data_{NUM_RECORDS}.{SQL_DIALECT}.sql")

    fh_csv = fh_jsonl = fh_xml = fh_sql = None
    writer_csv = None

    if FORMATS["csv"]:
        fh_csv = open(csv_file_path, "w", newline="", encoding="utf-8")
        writer_csv = csv.writer(fh_csv)
        writer_csv.writerow([col for (col, _) in SCHEMA])

    if FORMATS["jsonl"]:
        fh_jsonl = open(jsonl_file_path, "w", encoding="utf-8")

    if FORMATS["xml"]:
        fh_xml = open(xml_file_path, "w", encoding="utf-8")
        fh_xml.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        fh_xml.write(f"<Records count=\"{NUM_RECORDS}\">\n")

    if FORMATS["sql"]:
        fh_sql = open(sql_file_path, "w", encoding="utf-8")
        # Create table DDL using dialect-aware types
        fh_sql.write(f"CREATE TABLE {TABLE_NAME} (\n")
        col_defs = []
        for (col, typ) in SCHEMA:
            col_def = f"  {col} {sql_col_type(typ, col, SQL_DIALECT)}"
            col_defs.append(col_def)
        fh_sql.write(",\n".join(col_defs))
        fh_sql.write("\n);\n\n")
        
        # For generic dialect, if we encoded binary as base64 in a TEXT column, add a comment
        if SQL_DIALECT == "generic":
            fh_sql.write(f"-- NOTE: binary fields encoded as base64 in TEXT columns for portability.\n\n")

    # Parquet: write parts if enabled
    batch_id = 0
    rec_id = 1
    while rec_id <= NUM_RECORDS:
        limit = min(BATCH_SIZE, NUM_RECORDS - rec_id + 1)
        batch = []
        for _ in range(limit):
            rec = {}
            for (col, typ) in SCHEMA:
                if col == "id":
                    rec[col] = rec_id
                else:
                    rec[col] = gen_value(typ, col)
            batch.append(rec)
            rec_id += 1

        # CSV
        if FORMATS["csv"]:
            for rec in batch:
                row = []
                for (col, typ) in SCHEMA:
                    v = rec[col]
                    if v is None:
                        row.append("")
                    elif typ == "binary_blob":
                        # CSV: hex is readable
                        row.append(v.hex())
                    elif typ == "json":
                        row.append(json.dumps(v))
                    elif typ == "list_str":
                        row.append(",".join(v))
                    else:
                        row.append(str(v))
                writer_csv.writerow(row)
            fh_csv.flush()

        # JSONL
        if FORMATS["jsonl"]:
            for rec in batch:
                out = {}
                for (col, typ) in SCHEMA:
                    v = rec[col]
                    if v is None:
                        out[col] = None
                    elif typ == "binary_blob":
                        # JSON: base64 is portable
                        out[col] = base64.b64encode(v).decode('ascii')
                    else:
                        out[col] = v
                fh_jsonl.write(json.dumps(out, default=str) + "\n")
            fh_jsonl.flush()

        # XML
        if FORMATS["xml"]:
            for rec in batch:
                fh_xml.write("  <Record>\n")
                for (col, typ) in SCHEMA:
                    v = rec[col]
                    if v is None:
                        text = ""
                    elif typ == "binary_blob":
                        text = v.hex()
                    elif typ == "json":
                        text = json.dumps(v)
                    elif typ == "list_str":
                        text = ",".join(v)
                    else:
                        text = str(v)
                    # very simple escaping for XML special chars
                    text = (text.replace("&", "&amp;")
                                .replace("<", "&lt;")
                                .replace(">", "&gt;")
                                .replace("'", "&apos;")
                                .replace('"', "&quot;"))
                    fh_xml.write(f"    <{col}>{text}</{col}>\n")
                fh_xml.write("  </Record>\n")
            fh_xml.flush()

        # SQL
        if FORMATS["sql"]:
            cols = [col for (col, _) in SCHEMA if not (PRIMARY_KEY and col == 'id')]
            values_rows = []
            for rec in batch:
                vals = [format_sql_value(rec[col], typ, SQL_DIALECT) for (col, typ) in SCHEMA if not (PRIMARY_KEY and col == 'id')]
                values_rows.append(f"({', '.join(vals)})")

            # Write one INSERT statement for the whole batch
            fh_sql.write(
                f"INSERT INTO {TABLE_NAME} ({', '.join(cols)}) VALUES\n  "
                + ",\n  ".join(values_rows)
                + ";\n"
            )
            fh_sql.flush()

        # Parquet
        if FORMATS["parquet"]:
            import pandas as pd
            df_batch = pd.DataFrame(batch)
            for (col, typ) in SCHEMA:
                if typ == "binary_blob":
                    df_batch[col] = df_batch[col].apply(lambda x: x if isinstance(x, (bytes, bytearray)) else None)
                elif typ == "json":
                    df_batch[col] = df_batch[col].apply(lambda x: json.dumps(x) if x is not None else None)
                elif typ == "list_str":
                    df_batch[col] = df_batch[col].apply(lambda x: ",".join(x) if (x is not None and isinstance(x, list)) else None)
            table = pa.Table.from_pandas(df_batch)
            parquet_part_path = os.path.join(OUTPUT_DIR, f"data_{NUM_RECORDS}_part_{batch_id}.parquet")
            pq.write_table(table, parquet_part_path)
            batch_id += 1

    # Close and finalize files
    if FORMATS["xml"]:
        fh_xml.write("</Records>\n")
        fh_xml.close()
    if FORMATS["csv"]:
        fh_csv.close()
    if FORMATS["jsonl"]:
        fh_jsonl.close()
    if FORMATS["sql"]:
        fh_sql.close()

if __name__ == "__main__":
    stream_generate_and_write()
