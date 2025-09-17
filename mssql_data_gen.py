# mssql_data_gen.py

import argparse
import random
import json
import uuid
from faker import Faker
from decimal import Decimal
from datetime import datetime, timedelta

# Initialize Faker for data generation
fake = Faker()

def get_mssql_types_and_generators():
    """
    Returns a list of dictionaries, each representing a MS SQL Server data type.
    Includes the SQL definition and a Python function to generate fake data.
    """
    return [
        # --- Exact Numerics ---
        {'name': 'TINYINT', 'definition': 'TINYINT', 'generator': lambda: fake.random_int(min=0, max=255)},
        {'name': 'SMALLINT', 'definition': 'SMALLINT', 'generator': lambda: fake.random_int(min=-32768, max=32767)},
        {'name': 'INT', 'definition': 'INT', 'generator': lambda: fake.random_int(min=-2147483648, max=2147483647)},
        {'name': 'BIGINT', 'definition': 'BIGINT', 'generator': lambda: fake.random_int(min=-9223372036854775808, max=9223372036854775807)},
        {'name': 'BIT', 'definition': 'BIT', 'generator': lambda: random.choice([0, 1])},
        {'name': 'DECIMAL', 'definition': 'DECIMAL(10,2)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999999)}.{fake.random_int(10, 99)}')},
        {'name': 'NUMERIC', 'definition': 'NUMERIC(8,3)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999)}.{fake.random_int(100, 999)}')},
        {'name': 'MONEY', 'definition': 'MONEY', 'generator': lambda: Decimal(f'{fake.random_int(1, 999999)}.{fake.random_int(10, 99)}')},
        {'name': 'SMALLMONEY', 'definition': 'SMALLMONEY', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999)}.{fake.random_int(10, 99)}')},

        # --- Approximate Numerics ---
        {'name': 'FLOAT', 'definition': 'FLOAT(24)', 'generator': lambda: fake.pyfloat()},
        {'name': 'REAL', 'definition': 'REAL', 'generator': lambda: fake.pyfloat()},

        # --- Date and Time Types ---
        {'name': 'DATE', 'definition': 'DATE', 'generator': lambda: fake.date_object()},
        {'name': 'TIME', 'definition': 'TIME(3)', 'generator': lambda: fake.time_object()},
        {'name': 'DATETIME2', 'definition': 'DATETIME2(3)', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'DATETIMEOFFSET', 'definition': 'DATETIMEOFFSET(3)', 'generator': lambda: f"{fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]} +00:00"},
        {'name': 'DATETIME', 'definition': 'DATETIME', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'SMALLDATETIME', 'definition': 'SMALLDATETIME', 'generator': lambda: fake.date_time_this_decade().replace(second=0, microsecond=0)},

        # --- Character Strings ---
        {'name': 'CHAR', 'definition': 'CHAR(10)', 'generator': lambda: fake.pystr(min_chars=10, max_chars=10)},
        {'name': 'VARCHAR', 'definition': 'VARCHAR(255)', 'generator': lambda: fake.sentence()},
        {'name': 'TEXT', 'definition': 'TEXT', 'generator': lambda: fake.text(max_nb_chars=1000)},

        # --- Unicode Character Strings ---
        {'name': 'NCHAR', 'definition': 'NCHAR(10)', 'generator': lambda: fake.pystr(min_chars=10, max_chars=10)},
        {'name': 'NVARCHAR', 'definition': 'NVARCHAR(255)', 'generator': lambda: fake.sentence()},
        {'name': 'NTEXT', 'definition': 'NTEXT', 'generator': lambda: fake.text(max_nb_chars=1000)},

        # --- Binary Strings ---
        {'name': 'BINARY', 'definition': 'BINARY(16)', 'generator': lambda: fake.binary(length=16)},
        {'name': 'VARBINARY', 'definition': 'VARBINARY(100)', 'generator': lambda: fake.binary(length=random.randint(10, 100))},
        {'name': 'IMAGE', 'definition': 'IMAGE', 'generator': lambda: fake.binary(length=512)},

        # --- Other Data Types ---
        {'name': 'GEOGRAPHY', 'definition': 'GEOGRAPHY', 'generator': lambda: f"geography::Point({fake.latitude()}, {fake.longitude()}, 4326)"},
        {'name': 'GEOMETRY', 'definition': 'GEOMETRY', 'generator': lambda: f"geometry::Point({fake.longitude()}, {fake.latitude()}, 0)"},
        {'name': 'HIERARCHYID', 'definition': 'HIERARCHYID', 'generator': lambda: f"hierarchyid::Parse('/{fake.random_int(1, 10)}/{fake.random_int(1, 10)}/')"},
        {'name': 'JSON', 'definition': 'NVARCHAR(MAX)', 'generator': lambda: json.dumps({'name': fake.name(), 'age': fake.random_int(18, 80), 'city': fake.city()})},
        {'name': 'VECTOR', 'definition': 'VARBINARY(8000)', 'generator': lambda: fake.binary(length=100)},
        {'name': 'ROWVERSION', 'definition': 'ROWVERSION', 'generator': lambda: fake.binary(length=8)},
        {'name': 'SQL_VARIANT', 'definition': 'SQL_VARIANT', 'generator': lambda: fake.random_int(1, 1000)},
        {'name': 'UNIQUEIDENTIFIER', 'definition': 'UNIQUEIDENTIFIER', 'generator': lambda: str(uuid.uuid4())},
        {'name': 'XML', 'definition': 'XML', 'generator': lambda: f"<person><name>{fake.name()}</name><age>{fake.random_int(18, 80)}</age></person>"},
    ]

def format_for_sql(value, data_type_name=None):
    """Formats a Python value into a string suitable for a MS SQL Server INSERT statement."""
    if value is None:
        return "NULL"
    
    # For byte strings, use the hexadecimal literal format 0x...
    if isinstance(value, bytes):
        return f"0x{value.hex()}"

    # For numbers, just convert to string
    if isinstance(value, (int, float, Decimal)):
        return str(value)

    # For booleans (BIT type)
    if isinstance(value, bool):
        return '1' if value else '0'

    # For datetime objects, format them properly
    if hasattr(value, 'strftime'):
        return f"'{value.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}'"

    # For geometry/geography functions, don't quote them
    if isinstance(value, str) and any(prefix in value for prefix in ['geography::', 'geometry::', 'hierarchyid::']):
        return value

    # For everything else (strings, dates, etc.), escape and quote
    s = str(value).replace("'", "''")
    return f"'{s}'"

def main():
    parser = argparse.ArgumentParser(description="Generate a .sql file with a comprehensive MS SQL Server CREATE TABLE statement and random INSERTs.")
    parser.add_argument('--records', type=int, default=15, help='Total number of INSERT statements to create.')
    parser.add_argument('--batch', type=int, default=5, help='Number of rows per INSERT statement.')
    parser.add_argument('--null-percent', type=float, default=10.0, help='Percentage chance for any value to be NULL (0-100).')
    parser.add_argument('--not-null-columns', type=str, nargs='*', default=[], help='List of column names to make NOT NULL (e.g., TINYINT CHAR JSON).')
    parser.add_argument('--null-columns', type=str, nargs='*', default=[], help='List of column names that should always be NULL (e.g., TINYINT CHAR JSON).')
    parser.add_argument('--table-name', type=str, default='all_types_table', help='Name of the table in the SQL script.')
    parser.add_argument('--output-file', type=str, default='mssql_all_data_types.sql', help='Name of the output .sql file.')
    
    args = parser.parse_args()

    # Get the list of types and their data generators
    data_types = get_mssql_types_and_generators()

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
            f.write(f"-- MS SQL Server Data Generation Script\n")
            f.write(f"-- Generated on: {datetime.now().isoformat()}\n")
            f.write(f"-- Records: {args.records}\n")
            f.write("-- Batch size is not valid as Oracle doesn't support batch write like other DBs")
            f.write(f"-- NOT NULL columns: {', '.join(args.not_null_columns) if args.not_null_columns else 'None'}\n")
            f.write(f"-- Always NULL columns: {', '.join(args.null_columns) if args.null_columns else 'None'}\n\n")

            f.write(f"DROP TABLE IF EXISTS [{args.table_name}];\n\n")
            
            f.write(f"CREATE TABLE [{args.table_name}] (\n")
            f.write("  [id] INT IDENTITY(1,1) PRIMARY KEY,\n")
            
            # Create column definitions from the types and random names
            column_defs = []
            for i, (name, dtype) in enumerate(zip(column_names, data_types)):
                not_null_clause = " NOT NULL" if i in not_null_columns else ""
                # Skip ROWVERSION from NOT NULL as it's auto-generated
                if dtype['name'] == 'ROWVERSION':
                    not_null_clause = ""
                column_defs.append(f"  [{name}] {dtype['definition']}{not_null_clause}")
            f.write(',\n'.join(column_defs))
            f.write("\n);\n\n")

            # --- Write INSERT statements ---
            print(f"NOT NULL column indices: {not_null_columns}")
            print(f"NULL column indices: {null_columns}")
            print(f"Generating {args.records} records in batches of {args.batch}...")
            
            # Exclude ROWVERSION columns from INSERT statements (auto-generated)
            excluded_types = {'ROWVERSION'}
            insertable_indices = [i for i, dtype in enumerate(data_types) if dtype['name'] not in excluded_types]
            insertable_names = [column_names[i] for i in insertable_indices]
            cols_for_insert = ', '.join([f"[{name}]" for name in insertable_names])
            
            for i in range(0, args.records, args.batch):
                batch_size = min(args.batch, args.records - i)
                
                f.write(f"INSERT INTO [{args.table_name}] ({cols_for_insert}) VALUES\n")
                
                batch_values = []
                for j in range(batch_size):
                    values = []
                    for k in insertable_indices:
                        dtype = data_types[k]
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
                    
                    batch_values.append(f"({', '.join(values)})")
                
                f.write(',\n'.join(batch_values) + ';\n\n')

        print("\n✅ Success!")
        print(f"Generated {args.output_file} with {args.records} records in batches of {args.batch}.")

    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == '__main__':
    main()