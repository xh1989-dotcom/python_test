#!/usr/bin/env python3
"""
Flask API示例
功能：创建一个包含多个HTTP接口的Flask应用
包含10个新增API接口：用户CRUD、产品CRUD、健康检查、时间接口、计算器接口
"""

import os
from datetime import datetime
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# 加载.env文件中的环境变量
load_dotenv()

app = Flask(__name__)

# 从环境变量获取name，默认值为'World'
name = os.environ.get('name', 'World')

# 模拟用户数据存储
users_db = {
    1: {'id': 1, 'name': '张三', 'email': 'zhangsan@example.com', 'age': 25},
    2: {'id': 2, 'name': '李四', 'email': 'lisi@example.com', 'age': 30},
    3: {'id': 3, 'name': '王五', 'email': 'wangwu@example.com', 'age': 28}
}
user_id_counter = 4

# 模拟产品数据存储
products_db = {
    1: {'id': 1, 'name': '笔记本电脑', 'price': 5999.00, 'stock': 100},
    2: {'id': 2, 'name': '智能手机', 'price': 3999.00, 'stock': 200},
    3: {'id': 3, 'name': '无线耳机', 'price': 299.00, 'stock': 500}
}
product_id_counter = 4


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': f'Hello {name}'})


@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'running', 'message': 'Flask API is running'})


# ============= 新增API接口 1: 获取用户列表 =============
@app.route('/users', methods=['GET'])
def get_users():
    """获取所有用户列表"""
    users_list = list(users_db.values())
    return jsonify({
        'success': True,
        'data': users_list,
        'total': len(users_list)
    })


# ============= 新增API接口 2: 获取单个用户 =============
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """根据ID获取单个用户"""
    user = users_db.get(user_id)
    if user:
        return jsonify({
            'success': True,
            'data': user
        })
    return jsonify({
        'success': False,
        'message': f'用户ID {user_id} 不存在'
    }), 404


# ============= 新增API接口 3: 创建用户 =============
@app.route('/users', methods=['POST'])
def create_user():
    """创建新用户"""
    global user_id_counter
    data = request.get_json()
    
    if not data:
        return jsonify({
            'success': False,
            'message': '请提供用户数据'
        }), 400
    
    # 验证必填字段
    required_fields = ['name', 'email']
    for field in required_fields:
        if field not in data:
            return jsonify({
                'success': False,
                'message': f'缺少必填字段: {field}'
            }), 400
    
    new_user = {
        'id': user_id_counter,
        'name': data['name'],
        'email': data['email'],
        'age': data.get('age', 0)
    }
    users_db[user_id_counter] = new_user
    user_id_counter += 1
    
    return jsonify({
        'success': True,
        'message': '用户创建成功',
        'data': new_user
    }), 201


# ============= 新增API接口 4: 更新用户 =============
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """更新用户信息"""
    if user_id not in users_db:
        return jsonify({
            'success': False,
            'message': f'用户ID {user_id} 不存在'
        }), 404
    
    data = request.get_json()
    if not data:
        return jsonify({
            'success': False,
            'message': '请提供更新数据'
        }), 400
    
    user = users_db[user_id]
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
    if 'age' in data:
        user['age'] = data['age']
    
    return jsonify({
        'success': True,
        'message': '用户更新成功',
        'data': user
    })


# ============= 新增API接口 5: 删除用户 =============
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """删除用户"""
    if user_id not in users_db:
        return jsonify({
            'success': False,
            'message': f'用户ID {user_id} 不存在'
        }), 404
    
    deleted_user = users_db.pop(user_id)
    return jsonify({
        'success': True,
        'message': '用户删除成功',
        'data': deleted_user
    })


# ============= 新增API接口 6: 获取产品列表 =============
@app.route('/products', methods=['GET'])
def get_products():
    """获取所有产品列表"""
    products_list = list(products_db.values())
    return jsonify({
        'success': True,
        'data': products_list,
        'total': len(products_list)
    })


# ============= 新增API接口 7: 创建产品 =============
@app.route('/products', methods=['POST'])
def create_product():
    """创建新产品"""
    global product_id_counter
    data = request.get_json()
    
    if not data:
        return jsonify({
            'success': False,
            'message': '请提供产品数据'
        }), 400
    
    # 验证必填字段
    required_fields = ['name', 'price']
    for field in required_fields:
        if field not in data:
            return jsonify({
                'success': False,
                'message': f'缺少必填字段: {field}'
            }), 400
    
    new_product = {
        'id': product_id_counter,
        'name': data['name'],
        'price': float(data['price']),
        'stock': data.get('stock', 0)
    }
    products_db[product_id_counter] = new_product
    product_id_counter += 1
    
    return jsonify({
        'success': True,
        'message': '产品创建成功',
        'data': new_product
    }), 201


# ============= 新增API接口 8: 健康检查接口 =============
@app.route('/health', methods=['GET'])
def health_check():
    """健康检查接口，用于监控服务状态"""
    return jsonify({
        'success': True,
        'status': 'healthy',
        'service': 'Flask API',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    })


# ============= 新增API接口 9: 获取当前时间 =============
@app.route('/time', methods=['GET'])
def get_current_time():
    """获取服务器当前时间"""
    now = datetime.now()
    return jsonify({
        'success': True,
        'data': {
            'datetime': now.isoformat(),
            'date': now.strftime('%Y-%m-%d'),
            'time': now.strftime('%H:%M:%S'),
            'timestamp': int(now.timestamp()),
            'weekday': now.strftime('%A'),
            'timezone': 'Local'
        }
    })


# ============= 新增API接口 10: 计算器接口 =============
@app.route('/calculate', methods=['POST'])
def calculate():
    """计算器接口，支持加减乘除运算"""
    data = request.get_json()
    
    if not data:
        return jsonify({
            'success': False,
            'message': '请提供计算数据'
        }), 400
    
    required_fields = ['num1', 'num2', 'operation']
    for field in required_fields:
        if field not in data:
            return jsonify({
                'success': False,
                'message': f'缺少必填字段: {field}'
            }), 400
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({
                    'success': False,
                    'message': '除数不能为零'
                }), 400
            result = num1 / num2
        else:
            return jsonify({
                'success': False,
                'message': f'不支持的运算符: {operation}，支持的运算符: add, subtract, multiply, divide'
            }), 400
        
        return jsonify({
            'success': True,
            'data': {
                'num1': num1,
                'num2': num2,
                'operation': operation,
                'result': result
            }
        })
    except ValueError:
        return jsonify({
            'success': False,
            'message': '无效的数字格式'
        }), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)