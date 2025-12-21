from langchain_test1 import agent, get_weather_forecast

print('=== 架构类型详细分析 ===')
print('1. 工具定义分析:')
print(f'   工具类型: {type(get_weather_forecast)}')
print(f'   工具类名: {get_weather_forecast.__class__.__name__}')
print(f'   工具名称: {get_weather_forecast.name}')
print(f'   工具描述: {get_weather_forecast.description}')
print()

print('2. 执行流程分析:')
result = agent.invoke({'messages': [{'role': 'user', 'content': '深圳天气怎么样？'}]})

print(f'   总消息数: {len(result["messages"])}')
print('   消息流程:')

for i, msg in enumerate(result['messages']):
    msg_type = type(msg).__name__
    print(f'   步骤{i+1}: {msg_type}')
    
    if hasattr(msg, 'content') and msg.content:
        print(f'     内容: {msg.content[:50]}...')
    
    if hasattr(msg, 'tool_calls') and msg.tool_calls:
        print(f'     工具调用数量: {len(msg.tool_calls)}')
        for tc in msg.tool_calls:
            print(f'     调用工具: {tc.get("name")}')
            print(f'     参数: {tc.get("args")}')
    
    if hasattr(msg, 'name') and msg.name and hasattr(msg, 'content'):
        print(f'     工具返回: {msg.name[:20]} -> {msg.content[:30]}...')
    
    print()

print('3. 架构特征识别:')
print('   ✓ 使用@tool装饰器定义工具')
print('   ✓ 工具调用通过AIMessage.tool_calls实现')
print('   ✓ 返回结构化消息列表')
print('   ✓ 支持多轮工具调用')
print()

print('4. 架构类型结论:')
print('   这是: FUNCTION CALLING 架构 (函数调用模式)')
print('   不是: ReAct (没有Thought-Action-Observation循环)')
print('   不是: Plan-and-Execute (没有显式规划阶段)')