"""
Python Training - File 18: Flask Basics

This file covers:
- Setting up Flask applications
- Creating routes and views
- Handling different HTTP methods
- Working with templates
- Form handling
- Basic Flask patterns
"""

# Note: This file demonstrates Flask concepts but won't run as a server
# To run Flask apps, you would typically use a separate file and run it

print("Flask Basics - Web Framework Introduction")

# Basic Flask application structure
flask_app_code = '''
from flask import Flask, render_template, request, redirect, url_for, jsonify

# Create Flask application instance
app = Flask(__name__)

# Basic route
@app.route("/")
def home():
    return "<h1>Welcome to Flask!</h1><p>This is the home page.</p>"

# Route with variable
@app.route("/user/<username>")
def user_profile(username):
    return f"<h1>User Profile: {username}</h1>"

# Route with typed variable
@app.route("/user/<int:user_id>")
def user_by_id(user_id):
    return f"<h1>User ID: {user_id}</h1>"

# Route with multiple methods
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        # Simple validation (in real apps, use proper authentication)
        if username and password:
            return f"<h1>Welcome, {username}!</h1>"
        else:
            return "<h1>Login failed. Please try again.</h1>"
    else:
        # GET request - show login form
        return """
        <form method="POST">
            <p><input type="text" name="username" placeholder="Username" required></p>
            <p><input type="password" name="password" placeholder="Password" required></p>
            <p><input type="submit" value="Login"></p>
        </form>
        """

# API route that returns JSON
@app.route("/api/users")
def api_users():
    users = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
        {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
    ]
    return jsonify(users)

# Error handler
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Page Not Found</h1><p>The requested page does not exist.</p>", 404

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
'''

print("Basic Flask Application Structure:")
print(flask_app_code)

# Flask with templates example
template_example = '''
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    users = [
        {"name": "Alice", "age": 28, "city": "New York"},
        {"name": "Bob", "age": 32, "city": "San Francisco"},
        {"name": "Charlie", "age": 25, "city": "Boston"}
    ]
    return render_template("index.html", users=users, title="User List")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nFlask with Templates:")
print(template_example)

# Template file example (index.html)
index_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .user { border: 1px solid #ccc; padding: 10px; margin: 10px 0; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    
    <h2>Users</h2>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Age</th>
                <th>City</th>
            </tr>
        </thead>
        <tbody>
            {% for user in users %}
            <tr>
                <td>{{ user.name }}</td>
                <td>{{ user.age }}</td>
                <td>{{ user.city }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <p>Total users: {{ users|length }}</p>
</body>
</html>
'''

print(f"\nExample Template (index.html):")
print(index_template)

# Form handling example
form_handling_code = '''
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Needed for flash messages

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Validate input
        if not name or not email or not message:
            flash("All fields are required!", "error")
        else:
            # In a real app, you would save this to a database
            flash(f"Thank you, {name}! Your message has been received.", "success")
            return redirect(url_for("contact"))
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nForm Handling Example:")
print(form_handling_code)

# Contact template example
contact_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea { width: 100%; padding: 8px; box-sizing: border-box; }
        button { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }
        .flash { padding: 10px; margin-bottom: 15px; border-radius: 4px; }
        .flash.success { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .flash.error { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="flash {{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form method="POST">
        <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>
        </div>
        
        <button type="submit">Send Message</button>
    </form>
</body>
</html>
'''

print(f"\nContact Form Template:")
print(contact_template)

# Flask application with database integration example
db_integration_code = '''
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn

@app.route("/")
def index():
    conn = get_db_connection()
    posts = conn.execute("SELECT * FROM posts ORDER BY created_at DESC").fetchall()
    conn.close()
    return render_template("posts.html", posts=posts)

@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        
        conn = get_db_connection()
        conn.execute("INSERT INTO posts (title, content) VALUES (?, ?)", 
                     (title, content))
        conn.commit()
        conn.close()
        
        return redirect(url_for("index"))
    
    return render_template("create.html")

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nFlask with Database Integration:")
print(db_integration_code)

# URL building and redirection example
url_example = '''
from flask import Flask, url_for, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
'''<h1>Flask URL Examples</h1>
<ul>
    <li><a href="{{ url_for('user_profile', username='alice') }}">User Profile</a></li>
    <li><a href="{{ url_for('admin_panel') }}">Admin Panel</a></li>
    <li><a href="{{ url_for('api_users') }}">API Users</a></li>
</ul>
''' '''

@app.route("/user/<username>")
def user_profile(username):
    return f"<h1>Profile: {username}</h1>"

@app.route("/admin")
def admin_panel():
    # Redirect to login if not authenticated (simplified)
    authenticated = False  # In real app, check actual authentication
    if not authenticated:
        return redirect(url_for("login"))
    return "<h1>Admin Panel</h1>"

@app.route("/login")
def login():
    return "<h1>Login Page</h1>"

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nURL Building and Redirection:")
print(url_example)

# Flask configuration example
config_example = '''
import os
from flask import Flask

# Method 1: Configuration class
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-string'
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = 'sqlite:///dev.db'

class ProductionConfig(Config):
    DEBUG = False

# Create app with configuration
app = Flask(__name__)

# Load configuration
config_type = os.environ.get('FLASK_ENV', 'development')
if config_type == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

# Method 2: Configuration from file
app.config.from_pyfile('config.cfg', silent=True)

# Method 3: Environment variables
app.config['API_KEY'] = os.environ.get('API_KEY')

@app.route("/")
def home():
    return f"<h1>Debug Mode: {app.config['DEBUG']}</h1>"

if __name__ == "__main__":
    app.run()
'''

print(f"\nFlask Configuration:")
print(config_example)

# Flask extensions example
extensions_example = '''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)

# User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Handle login logic
        pass
    return render_template("login.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
'''

print(f"\nFlask Extensions Example:")
print(extensions_example)

# Practical example: Simple blog application
simple_blog_code = '''
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    """Initialize the database with posts table"""
    conn = sqlite3.connect("blog.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def blog_home():
    conn = sqlite3.connect("blog.db")
    posts = conn.execute(
        "SELECT id, title, content, created_at FROM posts ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return render_template("blog_home.html", posts=posts)

@app.route("/post/<int:post_id>")
def view_post(post_id):
    conn = sqlite3.connect("blog.db")
    post = conn.execute(
        "SELECT id, title, content, created_at FROM posts WHERE id = ?",
        (post_id,)
    ).fetchone()
    conn.close()
    
    if post:
        return render_template("view_post.html", post=post)
    else:
        return "<h1>Post not found</h1>", 404

@app.route("/create", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        
        conn = sqlite3.connect("blog.db")
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content)
        )
        conn.commit()
        conn.close()
        
        return redirect(url_for("blog_home"))
    
    return render_template("create_post.html")

if __name__ == "__main__":
    init_db()  # Initialize database
    app.run(debug=True)
'''

print(f"\nPractical Example: Simple Blog")
print(simple_blog_code)

print(f"\nFlask basics covered:")
print("- Setting up Flask applications")
print("- Creating routes and views")
print("- Handling different HTTP methods")
print("- Working with templates")
print("- Form handling")
print("- Database integration")
print("- Configuration management")
print("- URL building and redirection")
print("- Basic Flask patterns")

print("\nTo run Flask applications:")
print("1. Install Flask: pip install flask")
print("2. Create a Python file with Flask code")
print("3. Run the file: python app.py")
print("4. Visit http://localhost:5000 in your browser")
print("\nFlask basics completed!")