#!/usr/bin/env python3
"""
Flask API示例
功能：创建一个简单的HTTP接口返回Hello World
"""

import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

app = Flask(__name__)

# 从环境变量获取name，默认值为'World'
name = os.environ.get('name', 'World')

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': f'Hello {name}'})

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'running', 'message': 'Flask API is running'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)