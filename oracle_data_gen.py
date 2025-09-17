# oracle_data_gen.py

import argparse
import random
import json
import uuid
from faker import Faker
from decimal import Decimal
from datetime import datetime, timedelta

# Initialize Faker for data generation
fake = Faker()

def get_oracle_types_and_generators():
    """
    Returns a list of dictionaries, each representing an Oracle data type.
    Includes the SQL definition and a Python function to generate fake data.
    """
    return [
        # --- Character Types ---
        {'name': 'CHAR', 'definition': 'CHAR(10)', 'generator': lambda: fake.pystr(min_chars=10, max_chars=10)},
        {'name': 'VARCHAR2', 'definition': 'VARCHAR2(255)', 'generator': lambda: fake.sentence()},
        {'name': 'VARCHAR', 'definition': 'VARCHAR(100)', 'generator': lambda: fake.text(max_nb_chars=100)},
        {'name': 'NCHAR', 'definition': 'NCHAR(10)', 'generator': lambda: fake.pystr(min_chars=10, max_chars=10)},
        {'name': 'NVARCHAR2', 'definition': 'NVARCHAR2(255)', 'generator': lambda: fake.sentence()},

        # --- LOB Character Types ---
        {'name': 'CLOB', 'definition': 'CLOB', 'generator': lambda: fake.text(max_nb_chars=2000)},
        {'name': 'NCLOB', 'definition': 'NCLOB', 'generator': lambda: fake.text(max_nb_chars=2000)},
        # Note: Only one LONG column allowed per table - using CLOB instead
        # {'name': 'LONG', 'definition': 'LONG', 'generator': lambda: fake.text(max_nb_chars=1000)},

        # --- Raw/Binary Types ---
        {'name': 'RAW', 'definition': 'RAW(100)', 'generator': lambda: fake.binary(length=50).hex()},
        # Note: Only one LONG RAW column allowed per table - using BLOB instead
        # {'name': 'LONG_RAW', 'definition': 'LONG RAW', 'generator': lambda: fake.binary(length=100).hex()},

        # --- Numeric Types ---
        {'name': 'NUMBER', 'definition': 'NUMBER', 'generator': lambda: fake.random_int(min=-999999999, max=999999999)},
        {'name': 'NUMBER_PRECISION', 'definition': 'NUMBER(10,2)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999999)}.{fake.random_int(10, 99)}')},
        {'name': 'NUMBER_SCALE', 'definition': 'NUMBER(8,3)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999)}.{fake.random_int(100, 999)}')},
        {'name': 'BINARY_FLOAT', 'definition': 'BINARY_FLOAT', 'generator': lambda: fake.pyfloat()},
        {'name': 'BINARY_DOUBLE', 'definition': 'BINARY_DOUBLE', 'generator': lambda: fake.pyfloat()},

        # --- Date/Time Types ---
        {'name': 'DATE', 'definition': 'DATE', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'TIMESTAMP', 'definition': 'TIMESTAMP', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'TIMESTAMP_PRECISION', 'definition': 'TIMESTAMP(6)', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'TIMESTAMP_TZ', 'definition': 'TIMESTAMP WITH TIME ZONE', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'TIMESTAMP_LTZ', 'definition': 'TIMESTAMP WITH LOCAL TIME ZONE', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'INTERVAL_YM', 'definition': 'INTERVAL YEAR TO MONTH', 'generator': lambda: f"INTERVAL '{fake.random_int(0, 10)}-{fake.random_int(0, 11)}' YEAR TO MONTH"},
        {'name': 'INTERVAL_DS', 'definition': 'INTERVAL DAY TO SECOND', 'generator': lambda: f"INTERVAL '{fake.random_int(0, 30)} {fake.random_int(0, 23):02d}:{fake.random_int(0, 59):02d}:{fake.random_int(0, 59):02d}' DAY TO SECOND"},

        # --- LOB Binary Types ---
        {'name': 'BLOB', 'definition': 'BLOB', 'generator': lambda: fake.binary(length=512).hex()},
        {'name': 'BFILE', 'definition': 'BFILE', 'generator': lambda: f"BFILENAME('DATA_DIR', '{fake.file_name()}.dat')"},

        # --- Rowid Types (Note: ROWID columns are typically system-generated, not user-inserted)
        # {'name': 'ROWID', 'definition': 'ROWID', 'generator': lambda: 'SYSTEM_GENERATED'},
        {'name': 'UROWID', 'definition': 'UROWID', 'generator': lambda: ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/', k=18))},

        # --- XML Type ---
        {'name': 'XMLTYPE', 'definition': 'XMLTYPE', 'generator': lambda: f"<person><name>{fake.name()}</name><age>{fake.random_int(18, 80)}</age></person>"},
    ]

def format_for_sql(value, data_type_name=None):
    """Formats a Python value into a string suitable for an Oracle INSERT statement."""
    if value is None:
        return "NULL"
    
    # For numbers, just convert to string
    if isinstance(value, (int, float, Decimal)):
        return str(value)

    # For datetime objects, format them for Oracle
    if hasattr(value, 'strftime'):
        if data_type_name and 'TIMESTAMP_TZ' in data_type_name:
            return f"TO_TIMESTAMP_TZ('{value.strftime('%Y-%m-%d %H:%M:%S')} +00:00', 'YYYY-MM-DD HH24:MI:SS TZH:TZM')"
        elif data_type_name and 'TIMESTAMP_LTZ' in data_type_name:
            return f"TO_TIMESTAMP('{value.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS')"
        elif data_type_name and 'TIMESTAMP' in data_type_name:
            return f"TO_TIMESTAMP('{value.strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS')"
        else:
            return f"TO_DATE('{value.strftime('%Y-%m-%d')}', 'YYYY-MM-DD')"

    # For RAW data (hex strings), use HEXTORAW function
    if data_type_name and ('RAW' in data_type_name) and isinstance(value, str):
        return f"HEXTORAW('{value}')"

    # For BLOB data (hex strings), use HEXTORAW function
    if data_type_name and data_type_name == 'BLOB' and isinstance(value, str):
        return f"HEXTORAW('{value}')"

    # For BFILE and INTERVAL functions, don't quote them
    if isinstance(value, str) and any(func in value for func in ['BFILENAME(', 'INTERVAL ']):
        return value
    
    # For XMLType, wrap in XMLType constructor
    if data_type_name == 'XMLTYPE' and isinstance(value, str):
        escaped_xml = value.replace("'", "''")
        return f"XMLType('{escaped_xml}')"
    
    # For UROWID, use CHARTOROWID function
    if data_type_name == 'UROWID' and isinstance(value, str):
        return f"CHARTOROWID('{value}')"

    # For everything else (strings, etc.), escape and quote
    s = str(value).replace("'", "''")
    return f"'{s}'"

def main():
    parser = argparse.ArgumentParser(description="Generate a .sql file with a comprehensive Oracle CREATE TABLE statement and random INSERTs.")
    parser.add_argument('--records', type=int, default=15, help='Total number of INSERT statements to create.')
    parser.add_argument('--batch', type=int, default=5, help='Number of rows per INSERT statement.')
    parser.add_argument('--null-percent', type=float, default=10.0, help='Percentage chance for any value to be NULL (0-100).')
    parser.add_argument('--not-null-columns', type=str, nargs='*', default=[], help='List of column names to make NOT NULL (e.g., CHAR VARCHAR2 NUMBER).')
    parser.add_argument('--null-columns', type=str, nargs='*', default=[], help='List of column names that should always be NULL (e.g., CHAR VARCHAR2 NUMBER).')
    parser.add_argument('--table-name', type=str, default='all_types_table', help='Name of the table in the SQL script.')
    parser.add_argument('--output-file', type=str, default='oracle_all_data_types.sql', help='Name of the output .sql file.')
    
    args = parser.parse_args()

    # Get the list of types and their data generators
    data_types = get_oracle_types_and_generators()

    # Generate unique, random column names
    column_names = [f"col_{dtype['name'].lower()}_{i}" for i, dtype in enumerate(data_types)]
    
    # Find indices of columns to be NOT NULL and always NULL
    not_null_columns = set()
    null_columns = set()
    if args.not_null_columns:
        print(f"Looking for NOT NULL columns: {args.not_null_columns}")
        for col_type in args.not_null_columns:
            found = False
            for i, dtype in enumerate(data_types):
                if dtype['name'].upper() == col_type.upper():
                    not_null_columns.add(i)
                    print(f"Found NOT NULL column: {dtype['name']} at index {i}")
                    found = True
                    break
            if not found:
                print(f"WARNING: Column type '{col_type}' not found!")
    if args.null_columns:
        for col_type in args.null_columns:
            for i, dtype in enumerate(data_types):
                if dtype['name'].upper() == col_type.upper():
                    null_columns.add(i)
                    break

    try:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            print(f"Generating SQL file: {args.output_file}")
            
            # --- Write Header and CREATE TABLE statement ---
            f.write(f"-- Oracle Data Generation Script\n")
            f.write(f"-- Generated on: {datetime.now().isoformat()}\n")
            f.write(f"-- Records: {args.records}\n")
            f.write(f"-- Batch size: {args.batch}\n")
            f.write(f"-- NOT NULL columns: {', '.join(args.not_null_columns) if args.not_null_columns else 'None'}\n")
            f.write(f"-- Always NULL columns: {', '.join(args.null_columns) if args.null_columns else 'None'}\n\n")

            # Create directory for BFILE (Oracle specific)
            f.write("-- Create directory for BFILE (run as SYSDBA if needed)\n")
            f.write("-- CREATE OR REPLACE DIRECTORY DATA_DIR AS '/path/to/data';\n\n")

            f.write(f"DROP TABLE {args.table_name} CASCADE CONSTRAINTS;\n\n")
            
            f.write(f"CREATE TABLE {args.table_name} (\n")
            f.write("  id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,\n")
            
            # Create column definitions from the types and random names
            column_defs = []
            for i, (name, dtype) in enumerate(zip(column_names, data_types)):
                not_null_clause = " NOT NULL" if i in not_null_columns else ""
                column_defs.append(f"  {name} {dtype['definition']}{not_null_clause}")
            f.write(',\n'.join(column_defs))
            f.write("\n);\n\n")

            # --- Write INSERT statements ---
            print(f"NOT NULL column indices: {not_null_columns}")
            print(f"NULL column indices: {null_columns}")
            print(f"Generating {args.records} individual INSERT records...")
            
            # Prepare column names list for the INSERT query
            cols_for_insert = ', '.join(column_names)
            
            for i in range(args.records):
                values = []
                for k, dtype in enumerate(data_types):
                    # Force NULL for null_columns
                    if k in null_columns:
                        values.append(format_for_sql(None))
                    # Force non-null for NOT NULL columns
                    elif k in not_null_columns:
                        generated_value = dtype['generator']()
                        values.append(format_for_sql(generated_value, dtype['name']))
                    # Use null percentage for other columns
                    elif random.random() < (args.null_percent / 100):
                        values.append(format_for_sql(None))
                    else:
                        generated_value = dtype['generator']()
                        values.append(format_for_sql(generated_value, dtype['name']))
                
                f.write(f"INSERT INTO {args.table_name} ({cols_for_insert}) VALUES ({', '.join(values)});\n")

            # Add commit statement for Oracle
            f.write("COMMIT;\n")

        print("\n✅ Success!")
        print(f"Generated {args.output_file} with {args.records} individual INSERT records.")

    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    main()