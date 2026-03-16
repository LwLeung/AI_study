#!/usr/bin/env python3
"""
MCP Server 安全工具函数

提供常用的安全检查功能，防止路径遍历、SQL 注入等攻击。
"""

from pathlib import Path
from typing import Optional
import re


def safe_path(user_path: str, base_dir: Path) -> Optional[Path]:
    """
    确保路径在允许的范围内（防止路径遍历攻击）
    
    Args:
        user_path: 用户提供的路径
        base_dir: 允许的根目录
    
    Returns:
        安全的全路径，如果超出范围则返回 None
    
    示例:
        >>> safe_path("documents/file.txt", Path("/home/user"))
        Path("/home/user/documents/file.txt")
        
        >>> safe_path("../etc/passwd", Path("/home/user"))
        None
    """
    full_path = (base_dir / user_path).resolve()
    try:
        full_path.relative_to(base_dir.resolve())
        return full_path
    except ValueError:
        return None


def is_safe_sql(sql: str, allowed_operations: list = None) -> tuple:
    """
    检查 SQL 语句是否安全
    
    Args:
        sql: SQL 语句
        allowed_operations: 允许的操作类型，默认 ["SELECT"]
    
    Returns:
        (是否安全，错误信息)
    
    示例:
        >>> is_safe_sql("SELECT * FROM users")
        (True, "")
        
        >>> is_safe_sql("DROP TABLE users")
        (False, "禁止使用 DROP 操作")
    """
    if allowed_operations is None:
        allowed_operations = ["SELECT"]
    
    sql_upper = sql.strip().upper()
    
    # 检查是否以允许的操作开头
    allowed = False
    for op in allowed_operations:
        if sql_upper.startswith(op):
            allowed = True
            break
    
    if not allowed:
        return False, f"只允许执行以下操作：{', '.join(allowed_operations)}"
    
    # 检查危险关键字
    dangerous_keywords = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "CREATE", "TRUNCATE"]
    if allowed_operations == ["SELECT"]:
        # 只读模式下，禁止所有写操作
        for keyword in dangerous_keywords:
            if keyword in sql_upper:
                return False, f"禁止使用 {keyword} 操作"
    
    return True, ""


def sanitize_identifier(name: str) -> bool:
    """
    检查标识符是否有效（用于表名、列名等）
    
    Args:
        name: 标识符名称
    
    Returns:
        是否有效
    
    示例:
        >>> sanitize_identifier("users")
        True
        
        >>> sanitize_identifier("users; DROP TABLE--")
        False
    """
    # 只允许字母、数字、下划线
    return bool(re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name))


def limit_string_length(text: str, max_length: int = 10000) -> str:
    """
    限制字符串长度（防止输出过大）
    
    Args:
        text: 原始文本
        max_length: 最大长度
    
    Returns:
        截断后的文本
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + f"\n...（已截断，超出 {max_length} 字符限制）"


if __name__ == "__main__":
    # 测试
    print("安全工具函数测试")
    print("=" * 40)
    
    # 测试 safe_path
    base = Path("/home/user")
    print(f"\nsafe_path 测试:")
    print(f"  'docs/file.txt' -> {safe_path('docs/file.txt', base)}")
    print(f"  '../etc/passwd' -> {safe_path('../etc/passwd', base)}")
    
    # 测试 is_safe_sql
    print(f"\nis_safe_sql 测试:")
    test_sqls = [
        "SELECT * FROM users",
        "DROP TABLE users",
        "SELECT * FROM users; DELETE FROM logs",
    ]
    for sql in test_sqls:
        safe, msg = is_safe_sql(sql)
        print(f"  '{sql}' -> 安全：{safe}, 消息：{msg}")
    
    # 测试 sanitize_identifier
    print(f"\nsanitize_identifier 测试:")
    test_names = ["users", "user_data", "users; DROP TABLE--"]
    for name in test_names:
        print(f"  '{name}' -> {sanitize_identifier(name)}")
