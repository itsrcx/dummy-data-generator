# 🎲 Dummy Data Generator

A comprehensive, multi-format fake data generation toolkit for testing, development, and database seeding. Generate realistic test datasets in multiple formats with support for all major database systems.

## ✨ Features

- **Multi-Format Output**: CSV, JSON Lines, XML, SQL, and Parquet
- **Database-Specific Generators**: PostgreSQL, MySQL, MSSQL, Oracle with native data types
- **Streaming Architecture**: Memory-efficient processing for large datasets
- **Cloud Integration**: Direct DynamoDB insertion capabilities
- **Configurable Schema**: Customizable data types, null probabilities, and constraints
- **Production-Ready**: Handles binary data, complex JSON, and edge cases

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/itsrcx/dummy-data-generator.git
cd dummy-data-generator

# Install dependencies
pip install -r requirements.txt

# Generate 5,000 records in multiple formats
python data_gen.py
```

## 📊 Output Formats

### Universal Generator (`data_gen.py`)
Generates data in multiple formats simultaneously:
- **CSV**: Human-readable with proper escaping
- **JSON Lines**: One JSON object per line for streaming
- **XML**: Structured XML with proper encoding
- **SQL**: Dialect-aware INSERT statements
- **Parquet**: Columnar format for analytics (optional)

### Database-Specific Generators
Each generator creates comprehensive test data using all native data types:

| Database | Generator | Key Features |
|----------|-----------|--------------|
| PostgreSQL | `postgres_data_gen.py` | 45+ data types including geometric, network, JSON |
| MySQL | `mysql_data_gen.py` | All MySQL data types with proper encoding |
| MSSQL | `mssql_data_gen.py` | SQL Server specific types and constraints |
| Oracle | `oracle_data_gen.py` | Oracle-specific data types and functions |

## 🛠️ Configuration

### Basic Configuration
```python
NUM_RECORDS = 5000      # Number of records to generate
BATCH_SIZE = 1000       # Processing batch size
SQL_DIALECT = "generic" # SQL dialect: generic, postgres, mysql, mssql, oracle
PRIMARY_KEY = True      # Enable auto-increment primary key
```

### Schema Customization
```python
SCHEMA = [
    ("id", "int"),
    ("uuid", "uuid"),
    ("first_name", "str"),
    ("email", "email"),
    ("signup_date", "date"),
    ("is_active", "bool"),
    ("profile_json", "json"),
    ("profile_picture", "binary_blob"),
    # ... more fields
]
```

### Null Value Control
```python
GLOBAL_NULL_PROB = 0.1  # 10% chance of null values
COLUMN_NULL_PROBS = {
    "last_login": 0.3,  # 30% chance for this specific column
}
```

## 📁 Project Structure

```
dummy-data-generator/
├── data_gen.py              # Universal multi-format generator
├── postgres_data_gen.py     # PostgreSQL-specific generator
├── mysql_data_gen.py        # MySQL-specific generator
├── mssql_data_gen.py        # SQL Server-specific generator
├── oracle_data_gen.py       # Oracle-specific generator
├── dynamo_insert.py         # DynamoDB insertion utility
├── requirements.txt         # Python dependencies
├── output_data_*/           # Generated datasets
└── *.sql                   # Database schema files
```

## 🎯 Use Cases

### Development & Testing
- **API Testing**: Generate realistic user data for endpoint testing
- **Performance Testing**: Create large datasets to test application performance
- **Database Migration**: Generate test data for schema validation

### Data Engineering
- **Pipeline Testing**: Test ETL processes with realistic data
- **Analytics Development**: Create datasets for BI tool development
- **Data Modeling**: Generate data for machine learning model training

### Database Administration
- **Capacity Planning**: Generate large datasets for storage planning
- **Query Optimization**: Create test data for query performance tuning
- **Backup Testing**: Generate data for backup/restore procedures

## 🔧 Advanced Features

### Binary Data Handling
- **CSV**: Hex encoding for readability
- **JSON**: Base64 encoding for portability
- **SQL**: Dialect-specific binary literals (0x, E'\\x', HEXTORAW)

### Streaming Processing
Memory-efficient batch processing allows generation of millions of records without memory issues:

```python
# Process in configurable batches
for batch in stream_generate_and_write():
    # Process batch of records
    write_to_formats(batch)
```

### Cloud Integration
Direct insertion to AWS DynamoDB with proper type conversion:

```python
# Convert floats to Decimals for DynamoDB compatibility
processed_item = convert_floats_to_decimals(item)
batch.put_item(Item=processed_item)
```

## 📈 Performance

- **Memory Efficient**: Streaming architecture handles datasets of any size
- **Fast Generation**: Optimized Faker usage with seeded randomization
- **Batch Processing**: Configurable batch sizes for optimal performance
- **Parallel Processing**: Multi-format generation in single pass

## 🔍 Sample Data

The generator creates realistic data across multiple domains:

```json
{
  "id": 1,
  "uuid": "c917b566-dceb-454e-8d07-63d22cc8a9cf",
  "first_name": "Keith",
  "last_name": "Skinner",
  "email": "lee.silva@example.com",
  "signup_date": "1985-05-08",
  "is_active": true,
  "score": 106471290.85,
  "profile_json": {
    "preferences": {"theme": "dark", "newsletter": true},
    "settings": {"notifications": "email"}
  }
}
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- pip package manager

### Installation
```bash
pip install -r requirements.txt
```

### Basic Usage
```bash
# Generate 5,000 records (default)
python data_gen.py

# Generate PostgreSQL-specific data
python postgres_data_gen.py --records 1000 --batch 100

# Insert data into DynamoDB
python dynamo_insert.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏗️ Built With

- **[Faker](https://faker.readthedocs.io/)** - Fake data generation
- **[PyArrow](https://arrow.apache.org/docs/python/)** - Parquet file support
- **[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)** - AWS integration
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation

## 📊 Stats

- **45+ PostgreSQL data types** supported
- **Multiple output formats** (CSV, JSON, XML, SQL, Parquet)
- **4 major databases** supported (PostgreSQL, MySQL, MSSQL, Oracle)
- **Memory efficient** streaming architecture
- **For testing purpose** only for inserting dummy data

---

*This project demonstrates proficiency in Python, database systems, data engineering, and cloud technologies.*
