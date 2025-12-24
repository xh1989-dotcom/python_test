"""
Python Training - File 17: SQLite Database

This file covers:
- Connecting to SQLite databases
- Creating tables
- Inserting, updating, and deleting data
- Querying data
- Using transactions
- Practical examples
"""

import sqlite3
from datetime import datetime

# Connecting to SQLite database (creates file if it doesn't exist)
print("Connecting to SQLite database:")
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

print("Connected to SQLite database")

# Creating a table
print(f"\nCreating 'users' table:")
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
'''
cursor.execute(create_table_query)
conn.commit()
print("Table 'users' created successfully")

# Inserting data
print(f"\nInserting data:")
insert_query = '''
INSERT INTO users (name, email, age) VALUES (?, ?, ?)
'''

users_data = [
    ('Alice Johnson', 'alice@example.com', 28),
    ('Bob Smith', 'bob@example.com', 32),
    ('Charlie Brown', 'charlie@example.com', 25),
    ('Diana Prince', 'diana@example.com', 29)
]

cursor.executemany(insert_query, users_data)
conn.commit()
print(f"Inserted {len(users_data)} users")

# Querying data
print(f"\nQuerying all users:")
cursor.execute("SELECT * FROM users")
all_users = cursor.fetchall()

for user in all_users:
    print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}, Created: {user[4]}")

# Querying with conditions
print(f"\nQuerying users older than 27:")
cursor.execute("SELECT name, age FROM users WHERE age > ?", (27,))
older_users = cursor.fetchall()

for user in older_users:
    print(f"Name: {user[0]}, Age: {user[1]}")

# Querying with LIKE
print(f"\nQuerying users with names starting with 'A':")
cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('A%',))
a_users = cursor.fetchall()

for user in a_users:
    print(f"ID: {user[0]}, Name: {user[1]}")

# Updating data
print(f"\nUpdating Alice's age:")
cursor.execute("UPDATE users SET age = ? WHERE name = ?", (29, 'Alice Johnson'))
conn.commit()
print(f"Updated {cursor.rowcount} row(s)")

# Verify update
cursor.execute("SELECT name, age FROM users WHERE name = ?", ('Alice Johnson',))
updated_user = cursor.fetchone()
print(f"Alice's updated age: {updated_user[1]}")

# Deleting data
print(f"\nDeleting user with email 'charlie@example.com':")
cursor.execute("DELETE FROM users WHERE email = ?", ('charlie@example.com',))
conn.commit()
print(f"Deleted {cursor.rowcount} row(s)")

# Verify deletion
cursor.execute("SELECT COUNT(*) FROM users")
count = cursor.fetchone()[0]
print(f"Remaining users: {count}")

# Using transactions
print(f"\nUsing transactions:")
try:
    # Start transaction
    cursor.execute("BEGIN")
    
    # Insert multiple records
    new_users = [
        ('Eve Wilson', 'eve@example.com', 31),
        ('Frank Miller', 'frank@example.com', 27)
    ]
    cursor.executemany(insert_query, new_users)
    
    # Simulate some processing
    print("Processing new user data...")
    
    # Commit transaction
    conn.commit()
    print("Transaction committed successfully")
    
except Exception as e:
    # Rollback in case of error
    conn.rollback()
    print(f"Transaction rolled back due to error: {e}")

# Query to verify transaction
cursor.execute("SELECT name, email, age FROM users WHERE email IN (?, ?)", ('eve@example.com', 'frank@example.com'))
new_users = cursor.fetchall()
for user in new_users:
    print(f"New user: {user[0]} - {user[1]}, Age: {user[2]}")

# Creating another table with foreign key relationship
print(f"\nCreating 'orders' table with foreign key:")
create_orders_table = '''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_name TEXT NOT NULL,
    quantity INTEGER DEFAULT 1,
    price REAL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
)
'''
cursor.execute(create_orders_table)
conn.commit()
print("Table 'orders' created successfully")

# Inserting order data
print(f"\nInserting order data:")
order_insert_query = '''
INSERT INTO orders (user_id, product_name, quantity, price) VALUES (?, ?, ?, ?)
'''

# Get user IDs to link orders to users
cursor.execute("SELECT id, name FROM users")
user_ids = {name.split()[0].lower(): id for id, name in cursor.fetchall()}

order_data = [
    (user_ids.get('alice', 1), 'Laptop', 1, 999.99),
    (user_ids.get('bob', 2), 'Mouse', 2, 25.50),
    (user_ids.get('diana', 3), 'Keyboard', 1, 75.00),
    (user_ids.get('eve', 4), 'Monitor', 1, 299.99)
]

cursor.executemany(order_insert_query, order_data)
conn.commit()
print(f"Inserted {len(order_data)} orders")

# Joining tables
print(f"\nJoining users and orders:")
join_query = '''
SELECT u.name, u.email, o.product_name, o.quantity, o.price, o.order_date
FROM users u
JOIN orders o ON u.id = o.user_id
ORDER BY u.name
'''

cursor.execute(join_query)
joined_results = cursor.fetchall()

for row in joined_results:
    print(f"User: {row[0]}, Product: {row[2]}, Quantity: {row[3]}, Price: ${row[4]}")

# Aggregate functions
print(f"\nUsing aggregate functions:")
agg_query = '''
SELECT 
    u.name,
    COUNT(o.id) as order_count,
    SUM(o.price * o.quantity) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY total_spent DESC
'''

cursor.execute(agg_query)
agg_results = cursor.fetchall()

for row in agg_results:
    print(f"User: {row[0]}, Orders: {row[1]}, Total Spent: ${row[2] or 0}")

# Creating an index for better performance
print(f"\nCreating index on users email:")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)")
print("Index created on users email column")

# Using parameterized queries to prevent SQL injection
print(f"\nUsing parameterized queries:")

def get_user_by_email(conn, email):
    """Safely get user by email using parameterized query"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    return cursor.fetchone()

user = get_user_by_email(conn, 'alice@example.com')
if user:
    print(f"Found user: {user[1]} ({user[2]})")

# Demonstrating potential SQL injection vulnerability with string formatting
print(f"\nDemonstrating safe vs unsafe queries:")

def unsafe_query(conn, email):
    """UNSAFE - Don't use this in real applications!"""
    cursor = conn.cursor()
    # This is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor.execute(query)
    return cursor.fetchall()

def safe_query(conn, email):
    """SAFE - Use parameterized queries"""
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE email = ?"
    cursor.execute(query, (email,))
    return cursor.fetchall()

# Both work the same for normal input
normal_email = 'bob@example.com'
print(f"Safe query result: {safe_query(conn, normal_email)[0][1]}")
print(f"Unsafe query result: {unsafe_query(conn, normal_email)[0][1]}")

# Practical example: User management system
print(f"\nPractical example - User management system:")

class UserManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def add_user(self, username, email, full_name=None):
        try:
            self.cursor.execute(
                "INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)",
                (username, email, full_name)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Username or email already exists
    
    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return self.cursor.fetchone()
    
    def update_user(self, username, **kwargs):
        if not kwargs:
            return False
        
        # Build dynamic query
        fields = []
        values = []
        for key, value in kwargs.items():
            if key in ['username', 'email', 'full_name']:
                fields.append(f"{key} = ?")
                values.append(value)
        
        if not fields:
            return False
        
        values.append(username)
        query = f"UPDATE users SET {', '.join(fields)} WHERE username = ?"
        
        self.cursor.execute(query, values)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def delete_user(self, username):
        self.cursor.execute("DELETE FROM users WHERE username = ?", (username,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def list_users(self):
        self.cursor.execute("SELECT username, email, full_name FROM users ORDER BY username")
        return self.cursor.fetchall()
    
    def close(self):
        self.conn.close()

# Using the User Manager
user_manager = UserManager('users.db')

# Add users
users_to_add = [
    ('alice123', 'alice123@example.com', 'Alice Johnson'),
    ('bob456', 'bob456@example.com', 'Bob Smith'),
    ('charlie789', 'charlie789@example.com', 'Charlie Brown')
]

for username, email, full_name in users_to_add:
    if user_manager.add_user(username, email, full_name):
        print(f"Added user: {username}")
    else:
        print(f"Failed to add user: {username}")

# List all users
print(f"\nAll users:")
for user in user_manager.list_users():
    print(f"  {user[0]} - {user[1]} ({user[2]})")

# Get specific user
user = user_manager.get_user('alice123')
if user:
    print(f"\nRetrieved user: {user}")

# Update user
if user_manager.update_user('alice123', full_name='Alice J. Johnson'):
    print(f"Updated user: alice123")

# Close connection
user_manager.close()

# Closing the main connection
conn.close()
print(f"\nDatabase connection closed")

# Cleanup: Remove created database files
import os
for db_file in ['example.db', 'users.db']:
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed {db_file}")

print("\nSQLite database operations completed!")