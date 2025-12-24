"""
Python Training - File 16: JSON Handling

This file covers:
- Working with JSON data
- Parsing JSON strings
- Converting Python objects to JSON
- JSON formatting and validation
- Working with APIs that return JSON
- Practical examples
"""

import json

# Basic JSON encoding (Python to JSON)
print("Basic JSON encoding:")
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "grades": [85, 92, 78],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}

# Convert Python object to JSON string
json_string = json.dumps(data)
print(f"Python dict: {data}")
print(f"JSON string: {json_string}")

# JSON encoding with formatting options
formatted_json = json.dumps(data, indent=2, sort_keys=True)
print(f"\nFormatted JSON:")
print(formatted_json)

# Basic JSON decoding (JSON to Python)
print(f"\nBasic JSON decoding:")
json_string = '{"name": "Bob", "age": 25, "city": "Boston", "is_student": true}'
python_dict = json.loads(json_string)
print(f"JSON string: {json_string}")
print(f"Python dict: {python_dict}")

# Working with different Python data types
print(f"\nJSON conversion of different data types:")

# Python to JSON conversion examples
test_data = {
    "string": "hello",
    "integer": 42,
    "float": 3.14,
    "boolean": True,
    "null_value": None,
    "list": [1, 2, 3],
    "nested_dict": {"inner": "value"}
}

json_output = json.dumps(test_data, indent=2)
print(f"Python data: {test_data}")
print(f"JSON output: {json_output}")

# Converting back to Python
python_output = json.loads(json_output)
print(f"Converted back to Python: {python_output}")

# Working with JSON files
print(f"\nWorking with JSON files:")

# Writing JSON to a file
sample_data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ],
    "total_users": 3,
    "active": True
}

# Write to file
with open("sample_data.json", "w") as file:
    json.dump(sample_data, file, indent=2)

print("JSON data written to sample_data.json")

# Read from file
with open("sample_data.json", "r") as file:
    loaded_data = json.load(file)

print(f"Loaded from file: {loaded_data}")

# JSON validation and error handling
print(f"\nJSON validation and error handling:")

def safe_json_load(json_string):
    """Safely load JSON with error handling"""
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Error at line {e.lineno}, column {e.colno}: {e.msg}")
        return None

# Valid JSON
valid_json = '{"name": "Alice", "age": 30}'
result = safe_json_load(valid_json)
print(f"Valid JSON: {result}")

# Invalid JSON
invalid_json = '{"name": "Alice", "age": 30'  # Missing closing brace
result = safe_json_load(invalid_json)
print(f"Invalid JSON result: {result}")

# Handling special cases
print(f"\nHandling special cases:")

# NaN and Infinity (JavaScript values)
try:
    # By default, json allows NaN and Infinity
    special_data = {"value": float('nan'), "inf_value": float('inf')}
    json_str = json.dumps(special_data, allow_nan=True)
    print(f"Special values JSON: {json_str}")
    
    # Loading it back (this will raise an error by default)
    loaded_special = json.loads(json_str)
    print(f"Loaded special values: {loaded_special}")
except ValueError as e:
    print(f"Error with special values: {e}")

# Custom JSON encoder/decoder
print(f"\nCustom JSON encoder/decoder:")

from datetime import datetime

class DateTimeEncoder(json.JSONEncoder):
    """Custom encoder for datetime objects"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Using custom encoder
data_with_datetime = {
    "name": "Event",
    "date": datetime.now(),
    "attendees": ["Alice", "Bob"]
}

json_with_datetime = json.dumps(data_with_datetime, cls=DateTimeEncoder, indent=2)
print(f"JSON with datetime: {json_with_datetime}")

# Practical example: API response processing
print(f"\nPractical example - API response processing:")

# Simulate an API response
api_response = '''
{
    "status": "success",
    "data": {
        "users": [
            {
                "id": 1,
                "name": "Alice Johnson",
                "email": "alice@example.com",
                "profile": {
                    "age": 28,
                    "city": "New York",
                    "skills": ["Python", "JavaScript", "SQL"]
                }
            },
            {
                "id": 2,
                "name": "Bob Smith",
                "email": "bob@example.com",
                "profile": {
                    "age": 32,
                    "city": "San Francisco",
                    "skills": ["Java", "C++", "Python"]
                }
            }
        ],
        "total": 2
    }
}
'''

# Parse the API response
try:
    response_data = json.loads(api_response)
    
    if response_data["status"] == "success":
        users = response_data["data"]["users"]
        print(f"Total users: {response_data['data']['total']}")
        
        for user in users:
            print(f"User: {user['name']} ({user['email']})")
            profile = user['profile']
            print(f"  Age: {profile['age']}, City: {profile['city']}")
            print(f"  Skills: {', '.join(profile['skills'])}")
    else:
        print("API request failed")
        
except json.JSONDecodeError as e:
    print(f"Failed to parse API response: {e}")

# Practical example: JSON data transformation
print(f"\nJSON data transformation:")

# Original data structure
original_data = [
    {"name": "Product A", "price": 29.99, "in_stock": True},
    {"name": "Product B", "price": 49.99, "in_stock": False},
    {"name": "Product C", "price": 19.99, "in_stock": True}
]

# Transform to different structure
transformed_data = {
    "products": {
        "available": [],
        "unavailable": []
    },
    "summary": {
        "total": len(original_data),
        "available_count": sum(1 for p in original_data if p["in_stock"]),
        "total_value": sum(p["price"] for p in original_data if p["in_stock"])
    }
}

for product in original_data:
    category = "available" if product["in_stock"] else "unavailable"
    transformed_data["products"][category].append({
        "id": product["name"],
        "cost": product["price"]
    })

# Convert to JSON
transformed_json = json.dumps(transformed_data, indent=2)
print("Transformed data structure:")
print(transformed_json)

# Practical example: Configuration file handling
print(f"\nConfiguration file handling:")

config_data = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp_db",
        "credentials": {
            "username": "admin",
            "password": "secret"
        }
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30,
        "retries": 3
    },
    "features": {
        "enable_logging": True,
        "debug_mode": False,
        "max_connections": 100
    }
}

# Save configuration
with open("app_config.json", "w") as config_file:
    json.dump(config_data, config_file, indent=2)

print("Configuration saved to app_config.json")

# Load configuration
with open("app_config.json", "r") as config_file:
    loaded_config = json.load(config_file)

print(f"Database host: {loaded_config['database']['host']}")
print(f"API timeout: {loaded_config['api']['timeout']} seconds")
print(f"Logging enabled: {loaded_config['features']['enable_logging']}")

# Working with large JSON files efficiently
print(f"\nWorking with large JSON data:")

def process_large_json():
    """Simulate processing large JSON data"""
    # Create large dataset
    large_data = {
        "records": [
            {"id": i, "value": f"item_{i}", "active": i % 2 == 0}
            for i in range(1000)
        ]
    }
    
    # Serialize to JSON
    json_str = json.dumps(large_data)
    print(f"Original data size: {len(json_str)} characters")
    
    # Deserialize
    parsed_data = json.loads(json_str)
    print(f"Number of records: {len(parsed_data['records'])}")
    
    # Process subset
    active_records = [r for r in parsed_data['records'] if r['active']]
    print(f"Active records: {len(active_records)}")

process_large_json()

# Pretty printing JSON
print(f"\nPretty printing JSON:")

compact_json = '{"name":"Alice","age":30,"hobbies":["reading","swimming"],"address":{"city":"New York","zip":"10001"}}'
parsed = json.loads(compact_json)
pretty_json = json.dumps(parsed, indent=4, sort_keys=True)
print("Compact JSON:")
print(compact_json)
print("\nPretty JSON:")
print(pretty_json)

# Cleanup: Remove created files
import os
for file in ["sample_data.json", "app_config.json"]:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")

print("\nJSON handling completed!")