#!/usr/bin/env python3
"""
SQLite 数据库查询 MCP Server

使用方法:
    python server.py

注意:
    - 只允许执行 SELECT 查询（安全限制）
    - 默认数据库路径：/home/LiangWen/data.db
    - 可以通过环境变量 DB_PATH 修改
"""

from mcp.server.fastmcp import FastMCP
import sqlite3
import os

mcp = FastMCP("Database")

# 数据库路径（从环境变量读取）
DB_PATH = os.environ.get("DB_PATH", "/home/LiangWen/data.db")


@mcp.tool()
def query_database(sql: str) -> str:
    """
    执行 SQL 查询（只读）
    
    Args:
        sql: SQL 查询语句
    
    Returns:
        查询结果（表格格式）
    """
    # 安全限制：只允许 SELECT
    sql_upper = sql.strip().upper()
    if not sql_upper.startswith("SELECT"):
        return "错误：只允许执行 SELECT 查询"
    
    # 额外安全检查：禁止危险操作
    dangerous_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "CREATE", "TRUNCATE"]
    for keyword in dangerous_keywords:
        if keyword in sql_upper:
            return f"错误：禁止使用 {keyword} 操作"
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()
        
        if not rows:
            return "查询结果为空"
        
        # 计算列宽
        col_widths = []
        for i, col in enumerate(columns):
            max_width = len(col)
            for row in rows:
                if row[i] is not None:
                    max_width = max(max_width, len(str(row[i])))
            col_widths.append(min(max_width + 2, 50))  # 最大宽度 50
        
        # 格式化输出
        result = []
        
        # 表头
        header = " | ".join(col.ljust(col_widths[i]) for i, col in enumerate(columns))
        result.append(header)
        result.append("-" * len(header))
        
        # 数据行
        for row in rows:
            line = " | ".join(
                str(val if val is not None else "NULL").ljust(col_widths[i]) 
                for i, val in enumerate(row)
            )
            result.append(line)
        
        return "\n".join(result)
    
    except Exception as e:
        return f"查询错误：{str(e)}"


@mcp.tool()
def list_tables() -> str:
    """列出数据库中的所有表"""
    return query_database("SELECT name FROM sqlite_master WHERE type='table'")


@mcp.tool()
def get_table_schema(table_name: str) -> str:
    """
    获取表结构
    
    Args:
        table_name: 表名
    """
    # 安全检查：防止 SQL 注入
    if not table_name.isidentifier():
        return "错误：无效的表名"
    
    return query_database(f"PRAGMA table_info({table_name})")


@mcp.tool()
def sample_query(table_name: str, limit: int = 5) -> str:
    """
    查询表的前 N 行数据
    
    Args:
        table_name: 表名
        limit: 返回行数
    """
    # 安全检查：防止 SQL 注入
    if not table_name.isidentifier():
        return "错误：无效的表名"
    
    return query_database(f"SELECT * FROM {table_name} LIMIT {limit}")


if __name__ == "__main__":
    mcp.run()
