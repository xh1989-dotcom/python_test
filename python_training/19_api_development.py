"""
Python Training - File 19: API Development

This file covers:
- Creating REST APIs
- HTTP methods and status codes
- API endpoints and routing
- Request and response handling
- API authentication basics
- Error handling in APIs
- Practical examples
"""

print("API Development with Flask")

# Basic REST API structure
basic_api_code = '''
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample data store (in real applications, use a database)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 28},
    {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 32},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 25}
]

# GET /users - Retrieve all users
@app.route("/api/users", methods=["GET"])
def get_users():
    return jsonify({
        "status": "success",
        "data": users,
        "count": len(users)
    })

# GET /users/<id> - Retrieve a specific user
@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify({
            "status": "success",
            "data": user
        })
    else:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

# POST /users - Create a new user
@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    
    # Validation
    if not data or "name" not in data or "email" not in data:
        return jsonify({
            "status": "error",
            "message": "Name and email are required"
        }), 400
    
    # Create new user
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age", 0)
    }
    users.append(new_user)
    
    return jsonify({
        "status": "success",
        "data": new_user,
        "message": "User created successfully"
    }), 201

# PUT /users/<id> - Update a user
@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    
    data = request.get_json()
    if not data:
        return jsonify({
            "status": "error",
            "message": "No data provided"
        }), 400
    
    # Update user fields
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    user["age"] = data.get("age", user["age"])
    
    return jsonify({
        "status": "success",
        "data": user,
        "message": "User updated successfully"
    })

# DELETE /users/<id> - Delete a user
@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    
    users = [u for u in users if u["id"] != user_id]
    
    return jsonify({
        "status": "success",
        "message": "User deleted successfully"
    })

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == "__main__":
    app.run(debug=True)
'''

print("Basic REST API Structure:")
print(basic_api_code)

# API with request validation
validation_api_code = '''
from flask import Flask, jsonify, request
from functools import wraps
import re

app = Flask(__name__)

def validate_json(*expected_args):
    """Decorator to validate JSON request"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not request.is_json:
                return jsonify({"error": "Content-Type must be application/json"}), 400
            
            json_data = request.get_json()
            if not json_data:
                return jsonify({"error": "No JSON data provided"}), 400
            
            for expected_arg in expected_args:
                if expected_arg not in json_data:
                    return jsonify({"error": f"Missing required field: {expected_arg}"}), 400
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_email(email):
    """Simple email validation"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

@app.route("/api/users", methods=["POST"])
@validate_json("name", "email")
def create_user_validated():
    data = request.get_json()
    
    # Additional validation
    if not data["name"].strip():
        return jsonify({"error": "Name cannot be empty"}), 400
    
    if not validate_email(data["email"]):
        return jsonify({"error": "Invalid email format"}), 400
    
    # Check if email already exists
    # (In a real app, you'd check the database)
    
    # Create user
    user = {
        "id": 123,  # In real app, use auto-incrementing ID
        "name": data["name"],
        "email": data["email"],
        "created_at": "2023-01-01T00:00:00Z"
    }
    
    return jsonify({
        "status": "success",
        "data": user
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nAPI with Request Validation:")
print(validation_api_code)

# API with authentication
auth_api_code = '''
from flask import Flask, jsonify, request
from functools import wraps
import base64

app = Flask(__name__)

# Simple API key storage (in real apps, use a database)
API_KEYS = {
    "sk-1234567890abcdef": "admin",
    "sk-0987654321fedcba": "user"
}

def require_api_key(f):
    """Decorator to require API key authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        
        if not auth_header:
            return jsonify({"error": "Authorization header required"}), 401
        
        try:
            # Expecting "Bearer <api_key>" format
            auth_type, api_key = auth_header.split(" ", 1)
            if auth_type.lower() != "bearer":
                return jsonify({"error": "Invalid authorization type"}), 401
        except ValueError:
            return jsonify({"error": "Invalid authorization format"}), 401
        
        if api_key not in API_KEYS:
            return jsonify({"error": "Invalid API key"}), 401
        
        # Add user info to request context
        request.user_role = API_KEYS[api_key]
        return f(*args, **kwargs)
    
    return decorated_function

@app.route("/api/protected", methods=["GET"])
@require_api_key
def protected_endpoint():
    return jsonify({
        "message": "This is a protected endpoint",
        "user_role": request.user_role
    })

@app.route("/api/public", methods=["GET"])
def public_endpoint():
    return jsonify({
        "message": "This is a public endpoint"
    })

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nAPI with Authentication:")
print(auth_api_code)

# API with database integration
db_api_code = '''
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("api_database.db")
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

def init_db():
    """Initialize the database"""
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    
    # Support for query parameters
    name_filter = request.args.get("name")
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)
    
    query = "SELECT * FROM products WHERE 1=1"
    params = []
    
    if name_filter:
        query += " AND name LIKE ?"
        params.append(f"%{name_filter}%")
    
    if min_price is not None:
        query += " AND price >= ?"
        params.append(min_price)
    
    if max_price is not None:
        query += " AND price <= ?"
        params.append(max_price)
    
    query += " ORDER BY created_at DESC"
    
    products = conn.execute(query, params).fetchall()
    conn.close()
    
    return jsonify({
        "status": "success",
        "data": [dict(p) for p in products],
        "count": len(products)
    })

@app.route("/api/products", methods=["POST"])
def create_product():
    data = request.get_json()
    
    if not data or "name" not in data or "price" not in data:
        return jsonify({
            "status": "error",
            "message": "Name and price are required"
        }), 400
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO products (name, price, description) VALUES (?, ?, ?)",
        (data["name"], data["price"], data.get("description", ""))
    )
    
    product_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return jsonify({
        "status": "success",
        "data": {
            "id": product_id,
            "name": data["name"],
            "price": data["price"],
            "description": data.get("description", "")
        }
    }), 201

@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    conn = get_db_connection()
    product = conn.execute(
        "SELECT * FROM products WHERE id = ?", (product_id,)
    ).fetchone()
    conn.close()
    
    if product:
        return jsonify({
            "status": "success",
            "data": dict(product)
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

if __name__ == "__main__":
    init_db()  # Initialize database
    app.run(debug=True)
'''

print(f"\nAPI with Database Integration:")
print(db_api_code)

# API with pagination
pagination_api_code = '''
from flask import Flask, jsonify, request
import math

app = Flask(__name__)

# Sample large dataset
large_dataset = [
    {"id": i, "name": f"Item {i}", "value": i * 10}
    for i in range(1, 1001)  # 1000 items
]

@app.route("/api/items", methods=["GET"])
def get_items_paginated():
    # Get pagination parameters
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)
    
    # Limit per_page to prevent abuse
    per_page = min(per_page, 100)
    
    # Calculate offset
    offset = (page - 1) * per_page
    
    # Get items for current page
    items = large_dataset[offset:offset + per_page]
    
    # Calculate pagination info
    total_items = len(large_dataset)
    total_pages = math.ceil(total_items / per_page)
    
    return jsonify({
        "status": "success",
        "data": items,
        "pagination": {
            "current_page": page,
            "per_page": per_page,
            "total_items": total_items,
            "total_pages": total_pages,
            "has_next": page < total_pages,
            "has_prev": page > 1
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nAPI with Pagination:")
print(pagination_api_code)

# API with rate limiting (conceptual)
rate_limiting_code = '''
from flask import Flask, jsonify, request
from functools import wraps
from time import time

app = Flask(__name__)

# Simple rate limiting store (in real apps, use Redis)
rate_limits = {}

def rate_limit(max_requests=10, window=60):
    """Rate limiting decorator"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            client_ip = request.remote_addr
            current_time = time()
            
            # Initialize client record if not exists
            if client_ip not in rate_limits:
                rate_limits[client_ip] = []
            
            # Remove old requests outside the window
            rate_limits[client_ip] = [
                req_time for req_time in rate_limits[client_ip]
                if current_time - req_time < window
            ]
            
            # Check if limit exceeded
            if len(rate_limits[client_ip]) >= max_requests:
                return jsonify({
                    "error": "Rate limit exceeded",
                    "retry_after": window
                }), 429
            
            # Add current request
            rate_limits[client_ip].append(current_time)
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route("/api/data", methods=["GET"])
@rate_limit(max_requests=5, window=60)  # 5 requests per minute
def get_data():
    return jsonify({
        "message": "Data retrieved successfully",
        "timestamp": time()
    })

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nAPI with Rate Limiting (Conceptual):")
print(rate_limiting_code)

# API error handling best practices
error_handling_code = '''
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
import traceback

app = Flask(__name__)

@app.errorhandler(Exception)
def handle_exception(e):
    """Generic error handler"""
    # Log the error
    app.logger.error(f"Unhandled exception: {str(e)}")
    app.logger.error(traceback.format_exc())
    
    # Return JSON error response
    return jsonify({
        "status": "error",
        "message": "An internal error occurred",
        "error_type": type(e).__name__
    }), 500

@app.errorhandler(400)
def bad_request(e):
    return jsonify({
        "status": "error",
        "message": "Bad request",
        "error_code": "BAD_REQUEST"
    }), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "status": "error",
        "message": "Resource not found",
        "error_code": "NOT_FOUND"
    }), 404

@app.errorhandler(429)
def rate_limit_exceeded(e):
    return jsonify({
        "status": "error",
        "message": "Rate limit exceeded",
        "error_code": "RATE_LIMIT_EXCEEDED"
    }), 429

# Custom exception for API-specific errors
class APIError(Exception):
    def __init__(self, message, status_code=400, error_code=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.error_code = error_code or "CUSTOM_ERROR"

@app.errorhandler(APIError)
def handle_api_error(e):
    return jsonify({
        "status": "error",
        "message": e.message,
        "error_code": e.error_code
    }), e.status_code

@app.route("/api/test-error", methods=["GET"])
def test_error():
    # Example of raising custom API error
    raise APIError("This is a test API error", 400, "TEST_ERROR")

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nAPI Error Handling Best Practices:")
print(error_handling_code)

# Practical example: Task management API
task_api_code = '''
from flask import Flask, jsonify, request
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for tasks (use database in real app)
tasks = []

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    status_filter = request.args.get("status")
    priority_filter = request.args.get("priority")
    
    filtered_tasks = tasks
    
    if status_filter:
        filtered_tasks = [t for t in filtered_tasks if t["status"] == status_filter]
    
    if priority_filter:
        filtered_tasks = [t for t in filtered_tasks if t["priority"] == priority_filter]
    
    return jsonify({
        "status": "success",
        "data": filtered_tasks,
        "count": len(filtered_tasks)
    })

@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    
    required_fields = ["title", "description"]
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({
                "status": "error",
                "message": f"{field} is required"
            }), 400
    
    new_task = {
        "id": str(uuid.uuid4()),
        "title": data["title"],
        "description": data["description"],
        "status": data.get("status", "pending"),
        "priority": data.get("priority", "medium"),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    
    return jsonify({
        "status": "success",
        "data": new_task
    }), 201

@app.route("/api/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({
            "status": "error",
            "message": "Task not found"
        }), 404
    
    data = request.get_json()
    
    # Update allowed fields
    updatable_fields = ["title", "description", "status", "priority"]
    for field in updatable_fields:
        if field in data:
            task[field] = data[field]
    
    task["updated_at"] = datetime.now().isoformat()
    
    return jsonify({
        "status": "success",
        "data": task
    })

@app.route("/api/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    initial_count = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    
    if len(tasks) == initial_count:
        return jsonify({
            "status": "error",
            "message": "Task not found"
        }), 404
    
    return jsonify({
        "status": "success",
        "message": "Task deleted successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nPractical Example: Task Management API")
print(task_api_code)

print(f"\nAPI Development Concepts Covered:")
print("- REST API design principles")
print("- HTTP methods (GET, POST, PUT, DELETE)")
print("- Request and response handling")
print("- JSON data processing")
print("- API authentication")
print("- Database integration")
print("- Pagination")
print("- Rate limiting")
print("- Error handling")
print("- Validation")
print("- Best practices")

print("\nAPI development completed!")