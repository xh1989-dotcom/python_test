from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Flask 示例：
    - 轻量级，易于上手
    - 基于 Werkzeug WSGI 工具箱和 Jinja2 模板引擎
    - 灵活性高，插件丰富
    """
    return "Hello, Flask Training!"

@app.route('/api/info')
def get_info():
    return jsonify({
        "framework": "Flask",
        "type": "Microframework",
        "description": "Flexible and lightweight"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
