# postgres_data_gen.py

import argparse
import random
import json
import uuid
from faker import Faker
from decimal import Decimal
from datetime import datetime, timedelta
import ipaddress

# Initialize Faker for data generation
fake = Faker()

def get_postgres_types_and_generators():
    """
    Returns a list of dictionaries, each representing a PostgreSQL data type.
    Includes the SQL definition and a Python function to generate fake data.
    """
    return [
        # --- Numeric Types ---
        {'name': 'SMALLINT', 'definition': 'SMALLINT', 'generator': lambda: fake.random_int(min=-32768, max=32767)},
        {'name': 'INTEGER', 'definition': 'INTEGER', 'generator': lambda: fake.random_int(min=-2147483648, max=2147483647)},
        {'name': 'BIGINT', 'definition': 'BIGINT', 'generator': lambda: fake.random_int(min=-9223372036854775808, max=9223372036854775807)},
        {'name': 'DECIMAL', 'definition': 'DECIMAL(10,2)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999999)}.{fake.random_int(10, 99)}')},
        {'name': 'NUMERIC', 'definition': 'NUMERIC(8,3)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999)}.{fake.random_int(100, 999)}')},
        {'name': 'REAL', 'definition': 'REAL', 'generator': lambda: fake.pyfloat()},
        {'name': 'DOUBLE_PRECISION', 'definition': 'DOUBLE PRECISION', 'generator': lambda: fake.pyfloat()},

        # --- Serial Types ---
        {'name': 'SERIAL', 'definition': 'SERIAL', 'generator': lambda: fake.random_int(1, 2147483647)},
        {'name': 'SMALLSERIAL', 'definition': 'SMALLSERIAL', 'generator': lambda: fake.random_int(1, 32767)},
        {'name': 'BIGSERIAL', 'definition': 'BIGSERIAL', 'generator': lambda: fake.random_int(1, 9223372036854775807)},

        # --- Monetary Types ---
        {'name': 'MONEY', 'definition': 'MONEY', 'generator': lambda: f'${fake.pydecimal(left_digits=5, right_digits=2, positive=True)}'},

        # --- Character Types ---
        {'name': 'CHAR', 'definition': 'CHAR(10)', 'generator': lambda: fake.pystr(min_chars=10, max_chars=10)},
        {'name': 'VARCHAR', 'definition': 'VARCHAR(255)', 'generator': lambda: fake.sentence()},
        {'name': 'TEXT', 'definition': 'TEXT', 'generator': lambda: fake.text(max_nb_chars=1000)},

        # --- Binary Data Types ---
        {'name': 'BYTEA', 'definition': 'BYTEA', 'generator': lambda: f"\\x{fake.binary(length=32).hex()}"},

        # --- Date/Time Types ---
        {'name': 'DATE', 'definition': 'DATE', 'generator': lambda: fake.date_object()},
        {'name': 'TIME', 'definition': 'TIME', 'generator': lambda: fake.time_object()},
        {'name': 'TIMETZ', 'definition': 'TIME WITH TIME ZONE', 'generator': lambda: f"{fake.time_object()}+00"},
        {'name': 'TIMESTAMP', 'definition': 'TIMESTAMP', 'generator': lambda: fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')},
        {'name': 'TIMESTAMPTZ', 'definition': 'TIMESTAMP WITH TIME ZONE', 'generator': lambda: fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S+00')},
        {'name': 'INTERVAL', 'definition': 'INTERVAL', 'generator': lambda: f"{fake.random_int(1, 365)} days"},

        # --- Boolean Type ---
        {'name': 'BOOLEAN', 'definition': 'BOOLEAN', 'generator': lambda: fake.boolean()},

        # --- Enumerated Types ---
        {'name': 'ENUM', 'definition': "mood_enum", 'generator': lambda: random.choice(['happy', 'sad', 'neutral'])},

        # --- Geometric Types ---
        {'name': 'POINT', 'definition': 'POINT', 'generator': lambda: f"({fake.longitude()},{fake.latitude()})"},
        {'name': 'LINE', 'definition': 'LINE', 'generator': lambda: f"{{{fake.pyfloat()},{fake.pyfloat()},{fake.pyfloat()}}}"},
        {'name': 'LSEG', 'definition': 'LSEG', 'generator': lambda: f"[({fake.longitude()},{fake.latitude()}),({fake.longitude()},{fake.latitude()})]"},
        {'name': 'BOX', 'definition': 'BOX', 'generator': lambda: f"({fake.longitude()},{fake.latitude()}),({fake.longitude()},{fake.latitude()})"},
        {'name': 'PATH', 'definition': 'PATH', 'generator': lambda: f"[({fake.longitude()},{fake.latitude()}),({fake.longitude()},{fake.latitude()})]"},
        {'name': 'POLYGON', 'definition': 'POLYGON', 'generator': lambda: f"(({fake.longitude()},{fake.latitude()}),({fake.longitude()},{fake.latitude()}),({fake.longitude()},{fake.latitude()}))"},
        {'name': 'CIRCLE', 'definition': 'CIRCLE', 'generator': lambda: f"<({fake.longitude()},{fake.latitude()}),{fake.random_int(1, 100)}>"},

        # --- Network Address Types ---
        {'name': 'CIDR', 'definition': 'CIDR', 'generator': lambda: f"{fake.random_int(10, 192)}.{fake.random_int(0, 255)}.0.0/{random.choice([16, 24])}"},
        {'name': 'INET', 'definition': 'INET', 'generator': lambda: fake.ipv4()},
        {'name': 'MACADDR', 'definition': 'MACADDR', 'generator': lambda: fake.mac_address()},
        {'name': 'MACADDR8', 'definition': 'MACADDR8', 'generator': lambda: ':'.join([fake.hexify('^^') for _ in range(8)])},

        # --- Bit String Types ---
        {'name': 'BIT', 'definition': 'BIT(8)', 'generator': lambda: f"B'{format(fake.random_int(0, 255), '08b')}'"},
        {'name': 'VARBIT', 'definition': 'BIT VARYING(16)', 'generator': lambda: f"B'{format(fake.random_int(0, 65535), 'b')}'"},

        # --- Text Search Types ---
        {'name': 'TSVECTOR', 'definition': 'TSVECTOR', 'generator': lambda: f"'{fake.word()}:1 {fake.word()}:2'"},
        {'name': 'TSQUERY', 'definition': 'TSQUERY', 'generator': lambda: f"'{fake.word()} & {fake.word()}'"},

        # --- UUID Type ---
        {'name': 'UUID', 'definition': 'UUID', 'generator': lambda: str(uuid.uuid4())},

        # --- XML Type ---
        {'name': 'XML', 'definition': 'XML', 'generator': lambda: f"<person><name>{fake.name()}</name><age>{fake.random_int(18, 80)}</age></person>"},

        # --- JSON Types ---
        {'name': 'JSON', 'definition': 'JSON', 'generator': lambda: json.dumps({'name': fake.name(), 'age': fake.random_int(18, 80), 'city': fake.city()})},
        {'name': 'JSONB', 'definition': 'JSONB', 'generator': lambda: json.dumps({'id': fake.random_int(1, 1000), 'data': fake.word(), 'active': fake.boolean()})},

        # --- Array Types ---
        {'name': 'INT_ARRAY', 'definition': 'INTEGER[]', 'generator': lambda: f"{{{','.join([str(fake.random_int(1, 100)) for _ in range(3)])}}}"},
        {'name': 'TEXT_ARRAY', 'definition': 'TEXT[]', 'generator': lambda: '{' + ','.join([f'"{fake.word()}"' for _ in range(3)]) + '}'},

        # --- Range Types ---
        {'name': 'INT4RANGE', 'definition': 'INT4RANGE', 'generator': lambda: (lambda a, b: f"[{min(a,b)},{max(a,b)})")(fake.random_int(1, 100), fake.random_int(1, 100))},
        {'name': 'TSRANGE', 'definition': 'TSRANGE', 'generator': lambda: (lambda d1, d2: f"[{min(d1,d2).strftime('%Y-%m-%d %H:%M:%S')},{max(d1,d2).strftime('%Y-%m-%d %H:%M:%S')})")(fake.date_time_this_year(), fake.date_time_this_year())},
    ]

def format_for_sql(value):
    """Formats a Python value into a string suitable for a PostgreSQL INSERT statement."""
    if value is None:
        return "NULL"
    
    # For numbers, just convert to string
    if isinstance(value, (int, float, Decimal)):
        return str(value)

    # For booleans
    if isinstance(value, bool):
        return 'TRUE' if value else 'FALSE'

    # For datetime objects, format them properly
    if hasattr(value, 'strftime'):
        return f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'"

    # For bytea (already formatted with \x prefix)
    if isinstance(value, str) and value.startswith('\\x'):
        return f"'{value}'"

    # For bit strings (already formatted with B prefix)
    if isinstance(value, str) and value.startswith("B'"):
        return value

    # For geometric types and special formats, don't quote if they contain specific patterns
    if isinstance(value, str) and any(char in value for char in ['(', '[', '<', '{']):
        return f"'{value}'"

    # For everything else (strings, dates, etc.), escape and quote
    s = str(value).replace("'", "''")
    return f"'{s}'"

def main():
    parser = argparse.ArgumentParser(description="Generate a .sql file with a comprehensive PostgreSQL CREATE TABLE statement and random INSERTs.")
    parser.add_argument('--records', type=int, default=15, help='Total number of INSERT statements to create.')
    parser.add_argument('--batch', type=int, default=5, help='Number of rows per INSERT statement.')
    parser.add_argument('--null-percent', type=float, default=10.0, help='Percentage chance for any value to be NULL (0-100).')
    parser.add_argument('--not-null-columns', type=str, nargs='*', default=[], help='List of column names to make NOT NULL (e.g., SMALLINT CHAR JSON).')
    parser.add_argument('--null-columns', type=str, nargs='*', default=[], help='List of column names that should always be NULL (e.g., SMALLINT CHAR JSON).')
    parser.add_argument('--table-name', type=str, default='all_types_table', help='Name of the table in the SQL script.')
    parser.add_argument('--output-file', type=str, default='postgres_all_data_types.sql', help='Name of the output .sql file.')
    
    args = parser.parse_args()

    # Get the list of types and their data generators
    data_types = get_postgres_types_and_generators()

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
            
            # --- Write Header and CREATE TYPE/TABLE statements ---
            f.write(f"-- PostgreSQL Data Generation Script\n")
            f.write(f"-- Generated on: {datetime.now().isoformat()}\n")
            f.write(f"-- Records: {args.records}\n")
            f.write(f"-- Batch size: {args.batch}\n")
            f.write(f"-- NOT NULL columns: {', '.join(args.not_null_columns) if args.not_null_columns else 'None'}\n")
            f.write(f"-- Always NULL columns: {', '.join(args.null_columns) if args.null_columns else 'None'}\n\n")

            # Create enum type first
            f.write("DROP TYPE IF EXISTS mood_enum CASCADE;\n")
            f.write("CREATE TYPE mood_enum AS ENUM ('happy', 'sad', 'neutral');\n\n")

            f.write(f'DROP TABLE IF EXISTS "{args.table_name}";\n\n')
            
            f.write(f'CREATE TABLE "{args.table_name}" (\n')
            f.write('  "id" SERIAL PRIMARY KEY,\n')
            
            # Create column definitions from the types and random names
            column_defs = []
            for i, (name, dtype) in enumerate(zip(column_names, data_types)):
                not_null_clause = " NOT NULL" if i in not_null_columns else ""
                column_defs.append(f'  "{name}" {dtype["definition"]}{not_null_clause}')
            f.write(',\n'.join(column_defs))
            f.write("\n);\n\n")

            # --- Write INSERT statements ---
            print(f"NOT NULL column indices: {not_null_columns}")
            print(f"NULL column indices: {null_columns}")
            print(f"Generating {args.records} records in batches of {args.batch}...")
            
            # Exclude SERIAL columns from INSERT statements
            non_serial_indices = [i for i, dtype in enumerate(data_types) if 'SERIAL' not in dtype['name']]
            non_serial_names = [column_names[i] for i in non_serial_indices]
            cols_for_insert = ', '.join([f'"{name}"' for name in non_serial_names])
            
            for i in range(0, args.records, args.batch):
                batch_size = min(args.batch, args.records - i)
                
                f.write(f'INSERT INTO "{args.table_name}" ({cols_for_insert}) VALUES\n')
                
                batch_values = []
                for j in range(batch_size):
                    values = []
                    for k in non_serial_indices:
                        dtype = data_types[k]
                        # Force NULL for null_columns
                        if k in null_columns:
                            values.append(format_for_sql(None))
                        # Force non-null for NOT NULL columns
                        elif k in not_null_columns:
                            generated_value = dtype['generator']()
                            values.append(format_for_sql(generated_value))
                        # Use null percentage for other columns
                        elif random.random() < (args.null_percent / 100):
                            values.append(format_for_sql(None))
                        else:
                            generated_value = dtype['generator']()
                            values.append(format_for_sql(generated_value))
                    
                    batch_values.append(f"({', '.join(values)})")
                
                f.write(',\n'.join(batch_values) + ';\n\n')

        print("\n✅ Success!")
        print(f"Generated {args.output_file} with {args.records} records in batches of {args.batch}.")

    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    main()
    