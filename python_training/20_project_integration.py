"""
Python Training - File 20: Project Integration

This file covers:
- Integrating multiple Python concepts
- Building a complete application
- Using web requests, databases, and APIs together
- Error handling in complex applications
- Best practices for larger projects
- Practical example combining all concepts
"""

print("Project Integration - Combining Python Concepts")

# Import necessary modules
import requests
import sqlite3
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import os

# Project: Weather Data Tracker
# This project integrates:
# 1. Web requests (to get weather data)
# 2. Database operations (to store weather history)
# 3. API development (to serve weather data)
# 4. Error handling
# 5. JSON processing

print("\nStep 1: Setting up the database")

# Create database and tables
def setup_database():
    """Set up the database for weather tracking"""
    conn = sqlite3.connect("weather_data.db")
    cursor = conn.cursor()
    
    # Create weather history table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT NOT NULL,
            temperature REAL,
            humidity INTEGER,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database setup completed")

setup_database()

print("\nStep 2: Creating weather data fetcher")

class WeatherTracker:
    """Class to handle weather data operations"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or "fake-key-for-demo"  # In real app, use actual API key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        """Get current weather for a city"""
        try:
            # For this demo, we'll simulate API response
            # In a real application, you would make actual API call:
            # params = {
            #     "q": city,
            #     "appid": self.api_key,
            #     "units": "metric"
            # }
            # response = requests.get(self.base_url, params=params)
            
            # Simulate API response for demo
            simulated_data = {
                "name": city,
                "main": {
                    "temp": 22.5,
                    "humidity": 65
                },
                "weather": [
                    {
                        "description": "clear sky"
                    }
                ]
            }
            
            return {
                "city": simulated_data["name"],
                "temperature": simulated_data["main"]["temp"],
                "humidity": simulated_data["main"]["humidity"],
                "description": simulated_data["weather"][0]["description"],
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None
    
    def save_weather_data(self, weather_data):
        """Save weather data to database"""
        try:
            conn = sqlite3.connect("weather_data.db")
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO weather_history 
                (city, temperature, humidity, description)
                VALUES (?, ?, ?, ?)
            ''', (
                weather_data["city"],
                weather_data["temperature"],
                weather_data["humidity"],
                weather_data["description"]
            ))
            
            conn.commit()
            conn.close()
            print(f"Weather data for {weather_data['city']} saved to database")
        except Exception as e:
            print(f"Error saving weather data: {e}")
    
    def get_weather_history(self, city=None, limit=10):
        """Get weather history from database"""
        try:
            conn = sqlite3.connect("weather_data.db")
            cursor = conn.cursor()
            
            if city:
                cursor.execute('''
                    SELECT * FROM weather_history 
                    WHERE city = ? 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (city, limit))
            else:
                cursor.execute('''
                    SELECT * FROM weather_history 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (limit,))
            
            rows = cursor.fetchall()
            conn.close()
            
            # Convert to list of dictionaries
            columns = ["id", "city", "temperature", "humidity", "description", "timestamp"]
            history = []
            for row in rows:
                history.append(dict(zip(columns, row)))
            
            return history
        except Exception as e:
            print(f"Error retrieving weather history: {e}")
            return []

# Initialize weather tracker
weather_tracker = WeatherTracker()

print("\nStep 3: Simulating weather data collection")

# Simulate collecting weather data
cities = ["New York", "London", "Tokyo", "Sydney", "Paris"]
for city in cities:
    weather_data = weather_tracker.get_weather(city)
    if weather_data:
        weather_tracker.save_weather_data(weather_data)

print("Weather data collection completed")

print("\nStep 4: Creating Flask API for weather data")

# Create Flask application
app = Flask(__name__)

@app.route("/")
def home():
    """Home page with weather data"""
    return '''
    <h1>Weather Data Tracker</h1>
    <p>API Endpoints:</p>
    <ul>
        <li><a href="/api/weather">/api/weather</a> - Get all weather data</li>
        <li><a href="/api/weather/New York">/api/weather/&lt;city&gt;</a> - Get weather for specific city</li>
        <li><a href="/api/history">/api/history</a> - Get weather history</li>
    </ul>
    '''

@app.route("/api/weather")
def get_current_weather():
    """Get current weather data"""
    # For demo, return simulated data
    return jsonify({
        "status": "success",
        "data": [
            {"city": "New York", "temperature": 22.5, "humidity": 65, "description": "clear sky"},
            {"city": "London", "temperature": 15.2, "humidity": 70, "description": "cloudy"},
            {"city": "Tokyo", "temperature": 25.8, "humidity": 60, "description": "sunny"},
        ],
        "timestamp": datetime.now().isoformat()
    })

@app.route("/api/weather/<city>")
def get_weather_for_city(city):
    """Get weather for specific city"""
    try:
        weather_data = weather_tracker.get_weather(city)
        if weather_data:
            return jsonify({
                "status": "success",
                "data": weather_data
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Could not fetch weather data"
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api/history")
@app.route("/api/history/<city>")
def get_weather_history(city=None):
    """Get weather history"""
    try:
        limit = request.args.get("limit", 10, type=int)
        history = weather_tracker.get_weather_history(city, limit)
        
        return jsonify({
            "status": "success",
            "data": history,
            "count": len(history)
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route("/api/add_weather", methods=["POST"])
def add_weather_data():
    """Add weather data via API"""
    try:
        data = request.get_json()
        required_fields = ["city", "temperature", "humidity", "description"]
        
        for field in required_fields:
            if field not in data:
                return jsonify({
                    "status": "error",
                    "message": f"Missing required field: {field}"
                }), 400
        
        # Save to database
        weather_tracker.save_weather_data(data)
        
        return jsonify({
            "status": "success",
            "message": "Weather data added successfully",
            "data": data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Error handling for the API
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

print("\nStep 5: Demonstrating JSON processing")

# Process and analyze weather data
def analyze_weather_data():
    """Analyze weather data from database"""
    history = weather_tracker.get_weather_history(limit=100)
    
    if not history:
        print("No weather data available for analysis")
        return
    
    # Calculate statistics
    temperatures = [item["temperature"] for item in history if item["temperature"] is not None]
    humidities = [item["humidity"] for item in history if item["humidity"] is not None]
    
    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        
        print(f"Temperature Analysis:")
        print(f"  Average: {avg_temp:.2f}°C")
        print(f"  Max: {max_temp}°C")
        print(f"  Min: {min_temp}°C")
    
    if humidities:
        avg_humidity = sum(humidities) / len(humidities)
        print(f"  Average Humidity: {avg_humidity:.2f}%")

analyze_weather_data()

print("\nStep 6: Demonstrating error handling")

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print(f"Error: Cannot divide {a} by zero")
        return None
    except TypeError:
        print(f"Error: Invalid types for division: {type(a)}, {type(b)}")
        return None

print(f"Safe division examples:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")

print("\nStep 7: Demonstrating file operations with weather data")

# Export weather data to JSON file
def export_weather_data():
    """Export weather history to JSON file"""
    try:
        history = weather_tracker.get_weather_history(limit=50)
        
        # Create export data
        export_data = {
            "export_timestamp": datetime.now().isoformat(),
            "total_records": len(history),
            "weather_data": history
        }
        
        # Write to JSON file
        with open("weather_export.json", "w") as f:
            json.dump(export_data, f, indent=2)
        
        print(f"Weather data exported to weather_export.json ({len(history)} records)")
        
        # Read it back to verify
        with open("weather_export.json", "r") as f:
            loaded_data = json.load(f)
        
        print(f"Export file loaded successfully. Records: {len(loaded_data['weather_data'])}")
        
    except Exception as e:
        print(f"Error exporting weather data: {e}")

export_weather_data()

print("\nStep 8: Demonstrating complex data processing")

def process_weather_records(records):
    """Process weather records with complex logic"""
    processed = []
    
    for record in records:
        # Create a processed record with additional computed fields
        processed_record = {
            "id": record["id"],
            "city": record["city"],
            "temperature_celsius": record["temperature"],
            "temperature_fahrenheit": (record["temperature"] * 9/5) + 32,
            "humidity": record["humidity"],
            "description": record["description"],
            "timestamp": record["timestamp"],
            # Add comfort level based on temperature and humidity
            "comfort_level": get_comfort_level(record["temperature"], record["humidity"])
        }
        processed.append(processed_record)
    
    return processed

def get_comfort_level(temp, humidity):
    """Determine comfort level based on temperature and humidity"""
    if temp < 10:
        return "Cold"
    elif 10 <= temp < 20:
        if humidity > 70:
            return "Cool and Humid"
        else:
            return "Cool"
    elif 20 <= temp < 30:
        if humidity > 70:
            return "Warm and Humid"
        else:
            return "Comfortable"
    else:
        if humidity > 70:
            return "Hot and Humid"
        else:
            return "Hot"

# Process some records
recent_history = weather_tracker.get_weather_history(limit=10)
if recent_history:
    processed_data = process_weather_records(recent_history)
    print("Processed weather records with comfort levels:")
    for record in processed_data[:3]:  # Show first 3
        print(f"  {record['city']}: {record['temperature_celsius']:.1f}°C, "
              f"{record['comfort_level']}")

print("\nStep 9: Demonstrating list comprehensions and functional programming")

# Using list comprehensions and functional programming with weather data
history = weather_tracker.get_weather_history(limit=20)

# Get all unique cities
unique_cities = list(set(record["city"] for record in history))
print(f"Unique cities in history: {unique_cities}")

# Filter records for cities with high humidity (> 65)
high_humidity_records = [r for r in history if r["humidity"] and r["humidity"] > 65]
print(f"Records with high humidity: {len(high_humidity_records)}")

# Calculate average temperature per city using dictionary comprehension
city_temps = {}
for record in history:
    city = record["city"]
    if city not in city_temps:
        city_temps[city] = []
    if record["temperature"] is not None:
        city_temps[city].append(record["temperature"])

city_averages = {city: sum(temps)/len(temps) for city, temps in city_temps.items() if temps}
print(f"Average temperatures by city: {city_averages}")

# Using map, filter, and reduce concepts
from functools import reduce

# Filter records with valid temperature
valid_temp_records = list(filter(lambda r: r["temperature"] is not None, history))

# Map to extract temperatures
temperatures = list(map(lambda r: r["temperature"], valid_temp_records))

# Reduce to calculate sum (we'll use this to calculate average)
if temperatures:
    total_temp = reduce(lambda a, b: a + b, temperatures)
    avg_temp = total_temp / len(temperatures)
    print(f"Average temperature (calculated with reduce): {avg_temp:.2f}°C")

print("\nStep 10: Final integration - Running the Flask app")

print("The Flask application is ready to run!")
print("To run the full application:")
print("1. Install Flask: pip install flask")
print("2. Save this code as 'weather_app.py'")
print("3. Run: python weather_app.py")
print("4. Visit: http://localhost:5000")
print("\nThe application demonstrates:")
print("- Web requests (simulated)")
print("- Database operations")
print("- API development")
print("- JSON processing")
print("- Error handling")
print("- File operations")
print("- Complex data processing")
print("- Integration of multiple Python concepts")

# Clean up demo files
def cleanup_demo_files():
    """Clean up files created during the demo"""
    files_to_remove = ["weather_export.json", "weather_data.db"]
    for file in files_to_remove:
        try:
            if os.path.exists(file):
                os.remove(file)
                print(f"Removed {file}")
        except Exception as e:
            print(f"Could not remove {file}: {e}")

print("\nCleaning up demo files...")
cleanup_demo_files()

print("\nProject Integration completed!")
print("This example demonstrates how to integrate multiple Python concepts:")
print("1. Web requests and API calls")
print("2. Database operations with SQLite")
print("3. JSON processing and file handling")
print("4. Flask web framework")
print("5. Error handling and validation")
print("6. List comprehensions and functional programming")
print("7. Object-oriented programming")
print("8. Data analysis and processing")
print("9. Best practices for larger projects")

print("\nIntegration of Python concepts completed!")