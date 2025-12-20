#!/usr/bin/env python3
"""
案例9：正则表达式
功能：使用正则表达式匹配和处理文本
"""

import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def extract_phone_numbers(text):
    pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    numbers = re.findall(pattern, text)
    return numbers

def replace_urls(text):
    pattern = r'https?://\S+'
    replaced = re.sub(pattern, '[URL]', text)
    return replaced

if __name__ == "__main__":
    emails = ["test@example.com", "invalid-email", "user.name+tag@domain.co"]
    for email in emails:
        print(f"{email}: {validate_email(email)}")
    
    text = "联系电话：123-456-7890 或 987-654-3210"
    print(f"提取的电话号码: {extract_phone_numbers(text)}")
    
    text_with_urls = "访问 https://www.example.com 或 https://www.google.com 获取更多信息"
    print(f"替换后的文本: {replace_urls(text_with_urls)}")