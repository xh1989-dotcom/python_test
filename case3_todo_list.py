#!/usr/bin/env python3
"""
案例3：待办事项列表
功能：添加、删除、查看待办事项
"""

class TodoList:
    def __init__(self):
        self.todos = []
    
    def add_todo(self, todo):
        self.todos.append(todo)
        print(f"已添加待办事项: {todo}")
    
    def remove_todo(self, index):
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            print(f"已删除待办事项: {removed}")
        else:
            print("无效的索引")
    
    def show_todos(self):
        if not self.todos:
            print("待办事项为空")
            return
        print("待办事项列表:")
        for i, todo in enumerate(self.todos):
            print(f"{i+1}. {todo}")

if __name__ == "__main__":
    todo_list = TodoList()
    
    while True:
        print("\n待办事项管理器")
        print("1. 添加待办事项")
        print("2. 删除待办事项")
        print("3. 查看待办事项")
        print("4. 退出")
        
        choice = input("请选择操作(1-4): ")
        
        if choice == '1':
            todo = input("请输入待办事项: ")
            todo_list.add_todo(todo)
        elif choice == '2':
            try:
                index = int(input("请输入要删除的待办事项序号: ")) - 1
                todo_list.remove_todo(index)
            except ValueError:
                print("请输入有效的数字")
        elif choice == '3':
            todo_list.show_todos()
        elif choice == '4':
            print("退出程序")
            break
        else:
            print("无效的选择")