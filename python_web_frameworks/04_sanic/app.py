from sanic import Sanic, response

app = Sanic("MyHelloWorldApp")

# Sanic 示例：
# - 专注于速度
# - 类似 Flask 的 API 风格，但支持异步
# - 适合高性能服务

@app.get("/")
async def hello_world(request):
    return response.text("Hello, Sanic Training!")

@app.get("/api/info")
async def get_info(request):
    return response.json({
        "framework": "Sanic",
        "type": "Async Web framework",
        "description": "Built for speed and performance"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
