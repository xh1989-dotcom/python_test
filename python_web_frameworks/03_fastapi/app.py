from fastapi import FastAPI
import uvicorn

app = FastAPI()

# FastAPI 示例：
# - 现代、高性能
# - 基于 Python 3.7+ 的标准类型提示
# - 自动生成交互式 API 文档 (Swagger UI / ReDoc)
# - 异步支持 (async/await)

@app.get("/")
async def hello_world():
    return {"message": "Hello, FastAPI Training!"}

@app.get("/api/info")
async def get_info():
    return {
        "framework": "FastAPI",
        "type": "Modern API framework",
        "description": "High performance, based on Pydantic and Starlette"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
