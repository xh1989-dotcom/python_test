import requests

# 发送HTTP GET请求
response = requests.get('https://api.github.com')

# 打印响应状态码
print(f"Status Code: {response.status_code}")

# 打印响应内容的前500个字符
print("Response Content:")
print(response.text[:500])