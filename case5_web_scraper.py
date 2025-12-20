#!/usr/bin/env python3
"""
案例5：网页爬虫
功能：使用requests和BeautifulSoup爬取网页内容
"""

import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取标题
        title = soup.title.string if soup.title else '无标题'
        print(f"网页标题: {title}")
        
        # 提取所有链接
        links = soup.find_all('a')
        print(f"\n找到 {len(links)} 个链接:")
        for i, link in enumerate(links[:10]):  # 只显示前10个链接
            href = link.get('href')
            text = link.get_text(strip=True)
            print(f"{i+1}. {text} - {href}")
            
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
    except Exception as e:
        print(f"爬取网页时出错: {e}")

if __name__ == "__main__":
    url = "https://www.example.com"
    scrape_website(url)