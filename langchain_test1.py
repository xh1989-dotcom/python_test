# 安装依赖（如果还没安装）
# pip install langchain langchain-openai langchain-community

import os
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate

# 设置 DeepSeek 的 API Key 和 Base URL
# 你的 API Key
DEEPSEEK_API_KEY = "sk-80901c2d2c624d63a45a8bb4d1c3c8a3"

# 初始化 DeepSeek 模型（使用 OpenAI 兼容接口）
llm = ChatOpenAI(
    openai_api_key=DEEPSEEK_API_KEY,
    openai_api_base="https://api.deepseek.com/v1",
    model="deepseek-chat",  # 或 "deepseek-coder" 如果你想用代码模型
    temperature=0.7,
    max_tokens=512,
)

# 定义一个模拟的天气查询 Tool
@tool
def get_weather_forecast(city: str) -> str:
    """查询指定城市的天气预报（模拟数据）"""
    # 这里模拟一些天气数据，实际项目可以接入真实 API（如 OpenWeatherMap）
    weather_data = {
        "北京": "今天晴，气温 10-18°C，微风",
        "上海": "今天多云转阴，气温 12-16°C，有小雨",
        "广州": "今天多云，气温 18-25°C，湿度较高",
        "深圳": "今天晴间多云，气温 20-27°C",
        "成都": "今天阴有小雨，气温 8-14°C",
        "纽约": "今天晴，气温 -5-5°C，风大",
    }
    
    city = city.strip()
    if city in weather_data:
        return f"{city} 的天气预报：{weather_data[city]}"
    else:
        return f"抱歉，没有 {city} 的模拟天气数据。你可以试试 北京、上海、广州 等城市。"

# 准备 Prompt（让 Agent 知道如何使用 Tool）
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个有帮助的助手。你可以使用工具来查询天气。"),
    ("placeholder", "{messages}"),  # 占位符，用于存放对话历史
])

# 创建 Agent（使用 Tool Calling）
tools = [get_weather_forecast]
agent = create_agent(llm, tools, system_prompt="你是一个有帮助的助手。你可以使用工具来查询天气。")

# 运行示例
response = agent.invoke({"messages": [{"role": "user", "content": "告诉我明天成都的天气怎么样？"}]})
print("\n最终回答：")
# 提取最后一条AI消息的内容
if response and 'messages' in response and len(response['messages']) > 0:
    last_message = response['messages'][-1]
    if hasattr(last_message, 'content'):
        print(last_message.content)
    else:
        print("无法解析响应内容")
else:
    print("没有收到有效的响应")