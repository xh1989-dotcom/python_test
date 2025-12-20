#!/usr/bin/env python3
"""
案例6：数据可视化
功能：使用matplotlib绘制图表
"""

import matplotlib.pyplot as plt
import numpy as np

def plot_line_chart():
    # 生成数据
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    # 创建图表
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.title('正弦函数曲线')
    plt.xlabel('x轴')
    plt.ylabel('y轴')
    plt.legend()
    plt.grid(True)
    plt.savefig('sin_wave.png')
    print("折线图已保存为 sin_wave.png")

def plot_bar_chart():
    # 生成数据
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [23, 45, 56, 78, 32]
    
    # 创建图表
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='green')
    plt.title('柱状图示例')
    plt.xlabel('类别')
    plt.ylabel('数值')
    plt.savefig('bar_chart.png')
    print("柱状图已保存为 bar_chart.png")

if __name__ == "__main__":
    plot_line_chart()
    plot_bar_chart()