#!/usr/bin/env python3
"""
Flask API示例
功能：创建一个简单的HTTP接口返回Hello World
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    print("Hello World")
    return jsonify({'message': 'Hello World'})

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'running', 'message': 'Flask API is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)