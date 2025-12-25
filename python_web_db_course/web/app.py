from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "欢迎来到 Python Web 开发培训！"

@app.route('/api/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
