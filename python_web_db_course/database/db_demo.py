import sqlite3

def init_db():
    # 连接到 SQLite 数据库（如果不存在则创建）
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # 创建一个简单的表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
    ''')

    # 插入一些初始数据
    users = [
        ('Alice', 'alice@example.com'),
        ('Bob', 'bob@example.com')
    ]
    cursor.executemany('INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)', users)

    conn.commit()
    return conn

def query_users(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

if __name__ == '__main__':
    connection = init_db()
    print("数据库已初始化。")
    
    users = query_users(connection)
    print("当前用户列表：")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
    
    connection.close()
