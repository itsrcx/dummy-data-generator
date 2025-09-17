# generate_sql_file.py

import argparse
import random
import json
import re
from faker import Faker
from decimal import Decimal
from datetime import datetime

# Initialize Faker for data generation
fake = Faker()

def get_mysql_types_and_generators():
    """
    Returns a list of dictionaries, each representing a MySQL data type.
    Includes the SQL definition and a Python function to generate fake data.
    """
    return [
        # --- Numeric Types ---
        {'name': 'TINYINT', 'definition': 'TINYINT', 'generator': lambda: fake.random_int(min=-128, max=127)},
        {'name': 'SMALLINT', 'definition': 'SMALLINT', 'generator': lambda: fake.random_int(min=-32768, max=32767)},
        {'name': 'MEDIUMINT', 'definition': 'MEDIUMINT', 'generator': lambda: fake.random_int(min=-8388608, max=8388607)},
        {'name': 'INT', 'definition': 'INT', 'generator': lambda: fake.random_int(min=-2147483648, max=2147483647)},
        {'name': 'INTEGER', 'definition': 'INTEGER', 'generator': lambda: fake.random_int(min=-2147483648, max=2147483647)},
        {'name': 'BIGINT', 'definition': 'BIGINT', 'generator': lambda: fake.random_int(min=-9223372036854775808, max=9223372036854775807)},
        {'name': 'DECIMAL', 'definition': 'DECIMAL(10, 2)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999999)}.{fake.random_int(10, 99)}')},
        {'name': 'NUMERIC', 'definition': 'NUMERIC(8, 3)', 'generator': lambda: Decimal(f'{fake.random_int(1, 99999)}.{fake.random_int(100, 999)}')},
        {'name': 'FLOAT', 'definition': 'FLOAT', 'generator': lambda: fake.pyfloat()},
        {'name': 'DOUBLE', 'definition': 'DOUBLE', 'generator': lambda: fake.pyfloat()},
        {'name': 'BIT', 'definition': 'BIT(8)', 'generator': lambda: random.getrandbits(8).to_bytes(1, 'little')},

        # --- Date and Time Types ---
        {'name': 'DATE', 'definition': 'DATE', 'generator': lambda: fake.date_object()},
        {'name': 'DATETIME', 'definition': 'DATETIME(3)', 'generator': lambda: fake.date_time_this_decade()},
        {'name': 'TIMESTAMP', 'definition': 'TIMESTAMP', 'generator': lambda: datetime.now()},
        {'name': 'TIME', 'definition': 'TIME(3)', 'generator': lambda: fake.time_object()},
        {'name': 'YEAR', 'definition': 'YEAR', 'generator': lambda: int(fake.year())},

        # --- String Types ---
        {'name': 'CHAR', 'definition': 'CHAR(10)', 'generator': lambda: fake.pystr(min_chars=10, max_chars=10)},
        {'name': 'VARCHAR', 'definition': 'VARCHAR(255)', 'generator': lambda: fake.sentence()},
        {'name': 'BINARY', 'definition': 'BINARY(16)', 'generator': lambda: fake.binary(length=16)},
        {'name': 'VARBINARY', 'definition': 'VARBINARY(100)', 'generator': lambda: fake.binary(length=random.randint(10, 100))},
        {'name': 'BLOB', 'definition': 'BLOB', 'generator': lambda: fake.binary(length=512)},
        {'name': 'TINYBLOB', 'definition': 'TINYBLOB', 'generator': lambda: fake.binary(length=128)},
        {'name': 'MEDIUMBLOB', 'definition': 'MEDIUMBLOB', 'generator': lambda: fake.binary(length=1024)},
        {'name': 'LONGBLOB', 'definition': 'LONGBLOB', 'generator': lambda: fake.binary(length=2048)},
        {'name': 'TEXT', 'definition': 'TEXT', 'generator': lambda: fake.text(max_nb_chars=1000)},
        {'name': 'TINYTEXT', 'definition': 'TINYTEXT', 'generator': lambda: fake.text(max_nb_chars=255)},
        {'name': 'MEDIUMTEXT', 'definition': 'MEDIUMTEXT', 'generator': lambda: fake.text(max_nb_chars=5000)},
        {'name': 'LONGTEXT', 'definition': 'LONGTEXT', 'generator': lambda: fake.text(max_nb_chars=10000)},
        {'name': 'ENUM', 'definition': "ENUM('alpha', 'beta', 'gamma')", 'generator': lambda: random.choice(['alpha', 'beta', 'gamma'])},
        {'name': 'SET', 'definition': "SET('a', 'b', 'c', 'd')", 'generator': lambda: ','.join(random.sample(['a', 'b', 'c', 'd'], k=random.randint(1, 3)))},

        # --- Spatial Data Types ---
        {'name': 'POINT', 'definition': 'POINT', 'generator': lambda: f"ST_GeomFromText('POINT({fake.longitude()} {fake.latitude()})')"},
        {'name': 'LINESTRING', 'definition': 'LINESTRING', 'generator': lambda: f"ST_GeomFromText('LINESTRING({fake.longitude()} {fake.latitude()}, {fake.longitude()} {fake.latitude()})')"},
        {'name': 'POLYGON', 'definition': 'POLYGON', 'generator': lambda: (lambda x1, y1, x2, y2, x3, y3: f"ST_GeomFromText('POLYGON(({x1} {y1}, {x2} {y2}, {x3} {y3}, {x1} {y1}))')")(fake.longitude(), fake.latitude(), fake.longitude(), fake.latitude(), fake.longitude(), fake.latitude())},
        {'name': 'GEOMETRY', 'definition': 'GEOMETRY', 'generator': lambda: f"ST_GeomFromText('POINT({fake.longitude()} {fake.latitude()})')"},
        {'name': 'MULTIPOINT', 'definition': 'MULTIPOINT', 'generator': lambda: f"ST_GeomFromText('MULTIPOINT({fake.longitude()} {fake.latitude()}, {fake.longitude()} {fake.latitude()})')"},
        {'name': 'MULTILINESTRING', 'definition': 'MULTILINESTRING', 'generator': lambda: f"ST_GeomFromText('MULTILINESTRING(({fake.longitude()} {fake.latitude()}, {fake.longitude()} {fake.latitude()}), ({fake.longitude()} {fake.latitude()}, {fake.longitude()} {fake.latitude()}))')"},
        {'name': 'MULTIPOLYGON', 'definition': 'MULTIPOLYGON', 'generator': lambda: (lambda x1, y1, x2, y2, x3, y3: f"ST_GeomFromText('MULTIPOLYGON((({x1} {y1}, {x2} {y2}, {x3} {y3}, {x1} {y1})))')")(fake.longitude(), fake.latitude(), fake.longitude(), fake.latitude(), fake.longitude(), fake.latitude())},
        {'name': 'GEOMETRYCOLLECTION', 'definition': 'GEOMETRYCOLLECTION', 'generator': lambda: f"ST_GeomFromText('GEOMETRYCOLLECTION(POINT({fake.longitude()} {fake.latitude()}), LINESTRING({fake.longitude()} {fake.latitude()}, {fake.longitude()} {fake.latitude()}))')"},

        # --- JSON Data Type ---
        {'name': 'JSON', 'definition': 'JSON', 'generator': lambda: json.dumps({'name': fake.name(), 'age': fake.random_int(18, 80), 'city': fake.city()})},
    ]

def format_for_sql(value):
    """Formats a Python value into a string suitable for an SQL INSERT statement."""
    if value is None:
        return "NULL"
    
    # For byte strings, use the hexadecimal literal format X'...'
    if isinstance(value, bytes):
        return f"X'{value.hex()}'"

    # For numbers, just convert to string
    if isinstance(value, (int, float, Decimal)):
        return str(value)

    # For geometry functions, don't quote them
    if isinstance(value, str) and value.startswith('ST_GeomFromText('):
        return value

    # For everything else (strings, dates, etc.), escape and quote
    # Convert value to string, escape backslashes, then escape single quotes
    s = str(value).replace('\\', '\\\\').replace("'", "''")
    return f"'{s}'"

def main():
    parser = argparse.ArgumentParser(description="Generate a .sql file with a comprehensive CREATE TABLE statement and random INSERTs.")
    parser.add_argument('--records', type=int, default=15, help='Total number of INSERT statements to create.')
    parser.add_argument('--batch', type=int, default=5, help='Number of rows per INSERT statement.')
    parser.add_argument('--null-percent', type=float, default=10.0, help='Percentage chance for any value to be NULL (0-100).')
    parser.add_argument('--not-null-columns', type=str, nargs='*', default=[], help='List of column names to make NOT NULL (e.g., TINYINT CHAR JSON).')
    parser.add_argument('--null-columns', type=str, nargs='*', default=[], help='List of column names that should always be NULL (e.g., TINYINT CHAR JSON).')
    parser.add_argument('--table-name', type=str, default='all_types_table', help='Name of the table in the SQL script.')
    parser.add_argument('--output-file', type=str, default='mysql_all_data_types.sql', help='Name of the output .sql file.')
    
    args = parser.parse_args()

    # Get the list of types and their data generators
    data_types = get_mysql_types_and_generators()

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
            f.write(f"-- SQL Data Generation Script\n")
            f.write(f"-- Generated on: {datetime.now().isoformat()}\n")
            f.write(f"-- Records: {args.records}\n")
            f.write(f"-- Batch size: {args.batch}\n")
            f.write(f"-- NOT NULL columns: {', '.join(args.not_null_columns) if args.not_null_columns else 'None'}\n")
            f.write(f"-- Always NULL columns: {', '.join(args.null_columns) if args.null_columns else 'None'}\n\n")

            f.write(f"DROP TABLE IF EXISTS `{args.table_name}`;\n\n")
            
            f.write(f"CREATE TABLE `{args.table_name}` (\n")
            f.write("  `id` INT AUTO_INCREMENT PRIMARY KEY,\n")
            
            # Create column definitions from the types and random names
            column_defs = []
            for i, (name, dtype) in enumerate(zip(column_names, data_types)):
                not_null_clause = " NOT NULL" if i in not_null_columns else ""
                column_defs.append(f"  `{name}` {dtype['definition']}{not_null_clause}")
            f.write(',\n'.join(column_defs))
            f.write("\n);\n\n")

            # --- Write INSERT statements ---
            print(f"NOT NULL column indices: {not_null_columns}")
            print(f"NULL column indices: {null_columns}")
            print(f"Generating {args.records} records in batches of {args.batch}...")
            
            # Prepare column names list for the INSERT query
            cols_for_insert = ', '.join([f"`{name}`" for name in column_names])
            
            for i in range(0, args.records, args.batch):
                batch_size = min(args.batch, args.records - i)
                
                f.write(f"INSERT INTO `{args.table_name}` ({cols_for_insert}) VALUES\n")
                
                batch_values = []
                for j in range(batch_size):
                    values = []
                    for k, dtype in enumerate(data_types):
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
