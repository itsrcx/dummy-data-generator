import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('people_test_dataset') # Replace with your table name

def insert_data_from_jsonl(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            try:
                item = json.loads(line)
                print(f"Inserting item: {item}")
                table.put_item(Item=item)
                print("Item inserted successfully.")
            except json.JSONDecodeError as e:
                print(f"Skipping invalid JSON line: {line.strip()}. Error: {e}")
            except Exception as e:
                print(f"An error occurred while inserting item {item}: {e}")

def convert_floats_to_decimals(obj):
    """
    Recursively converts float values in a dictionary or list
    to Decimal types, which are supported by DynamoDB.
    """
    if isinstance(obj, float):
        return Decimal(str(obj))
    if isinstance(obj, dict):
        return {k: convert_floats_to_decimals(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_floats_to_decimals(i) for i in obj]
    return obj

def insert_data_in_batches(file_path):
    """
    Reads data from a JSONL file, converts float values to Decimals,
    and inserts records into a DynamoDB table using batch_writer.
    """
    with table.batch_writer() as batch:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    item = json.loads(line)
                    # Convert any float values to Decimal before inserting
                    processed_item = convert_floats_to_decimals(item)
                    batch.put_item(Item=processed_item)
                except json.JSONDecodeError as e:
                    print(f"Skipping invalid JSON line: {line.strip()}. Error: {e}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                    
if __name__ == "__main__":
    jsonl_file_path = '/Users/raman/Documents/dummy-data-generator/output_data_20000/data_20000.jsonl'
    insert_data_in_batches(jsonl_file_path)

