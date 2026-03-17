#!/usr/bin/env python3
"""
待办事项管理 MCP Server

使用方法:
    python server.py

功能:
    - 添加待办事项
    - 列出待办事项
    - 标记为完成
    - 删除待办事项
"""

from mcp.server.fastmcp import FastMCP
from datetime import datetime
import json
import os

mcp = FastMCP("Todo")

# 数据文件路径（从环境变量读取）
TODO_FILE = os.environ.get("TODO_FILE", "/home/LiangWen/todos.json")


def load_todos() -> list:
    """加载待办事项列表"""
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_todos(todos: list):
    """保存待办事项列表"""
    # 确保目录存在
    os.makedirs(os.path.dirname(TODO_FILE) or ".", exist_ok=True)
    
    with open(TODO_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


@mcp.tool()
def add_todo(task: str, priority: str = "medium") -> str:
    """
    添加待办事项
    
    Args:
        task: 任务描述
        priority: 优先级 (high/medium/low)
    
    Returns:
        操作结果
    """
    todos = load_todos()
    todo = {
        "id": len(todos) + 1,
        "task": task,
        "priority": priority,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    todos.append(todo)
    save_todos(todos)
    return f"✅ 已添加：{task}"


@mcp.tool()
def list_todos(show_completed: bool = False, priority: str = None) -> str:
    """
    列出待办事项
    
    Args:
        show_completed: 是否显示已完成的
        priority: 按优先级筛选 (high/medium/low)
    
    Returns:
        待办事项列表
    """
    todos = load_todos()
    
    # 筛选
    if not show_completed:
        todos = [t for t in todos if not t["completed"]]
    
    if priority:
        todos = [t for t in todos if t["priority"] == priority]
    
    if not todos:
        return "🎉 没有待办事项！"
    
    # 格式化输出
    result = []
    for t in todos:
        status = "✅" if t["completed"] else "⬜"
        priority_icon = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(t["priority"], "⚪")
        result.append(f"{status} {priority_icon} #{t['id']} {t['task']}")
    
    return "\n".join(result)


@mcp.tool()
def complete_todo(todo_id: int) -> str:
    """
    标记待办事项为完成
    
    Args:
        todo_id: 待办事项 ID
    
    Returns:
        操作结果
    """
    todos = load_todos()
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            save_todos(todos)
            return f"✅ 已完成：{todo['task']}"
    return f"错误：未找到 ID 为 {todo_id} 的待办事项"


@mcp.tool()
def delete_todo(todo_id: int) -> str:
    """
    删除待办事项
    
    Args:
        todo_id: 待办事项 ID
    
    Returns:
        操作结果
    """
    todos = load_todos()
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted = todos.pop(i)
            save_todos(todos)
            return f"🗑️ 已删除：{deleted['task']}"
    return f"错误：未找到 ID 为 {todo_id} 的待办事项"


@mcp.tool()
def get_stats() -> str:
    """
    获取待办事项统计
    
    Returns:
        统计信息
    """
    todos = load_todos()
    total = len(todos)
    completed = sum(1 for t in todos if t["completed"])
    pending = total - completed
    
    high = sum(1 for t in todos if t["priority"] == "high" and not t["completed"])
    medium = sum(1 for t in todos if t["priority"] == "medium" and not t["completed"])
    low = sum(1 for t in todos if t["priority"] == "low" and not t["completed"])
    
    return f"""
📊 待办事项统计
━━━━━━━━━━━━━━━━
总计：{total}
已完成：{completed}
待完成：{pending}

待完成优先级:
🔴 高：{high}
🟡 中：{medium}
🟢 低：{low}
━━━━━━━━━━━━━━━━
    """.strip()


# ============ Prompts ============

@mcp.prompt()
def todo_instructions() -> str:
    """
    待办事项助手的使用提示词
    """
    return """
你是一个待办事项管理助手。你可以：
1. 添加待办事项（add_todo）
2. 列出待办事项（list_todos）
3. 标记为完成（complete_todo）
4. 删除待办事项（delete_todo）
5. 查看统计（get_stats）

建议用户：
- 给重要任务设置高优先级（high）
- 定期查看统计，保持动力
- 完成任务后及时标记
"""


if __name__ == "__main__":
    mcp.run()
