#!/usr/bin/env python3
"""
文件管理 MCP Server
功能：读取、写入、列出、删除文件

使用方法:
    python server.py

在 Claude Desktop 配置中添加:
{
  "mcpServers": {
    "file-manager": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "WORK_DIR": "/home/LiangWen"
      }
    }
  }
}
"""

from mcp.server.fastmcp import FastMCP
from pathlib import Path
from typing import Optional
import os

# 创建 Server
mcp = FastMCP("File Manager")

# 配置工作目录（从环境变量读取，默认 /home/LiangWen）
WORK_DIR = Path(os.environ.get("WORK_DIR", "/home/LiangWen"))

# ============ Tools ============

@mcp.tool()
def read_file(file_path: str) -> str:
    """
    读取文件内容
    
    Args:
        file_path: 文件路径（相对于工作目录）
    
    Returns:
        文件内容
    """
    full_path = WORK_DIR / file_path
    
    # 安全检查：确保路径在工作目录内
    try:
        full_path.resolve().relative_to(WORK_DIR.resolve())
    except ValueError:
        return "错误：文件路径超出工作目录范围"
    
    if not full_path.exists():
        return f"错误：文件不存在 - {file_path}"
    
    return full_path.read_text(encoding="utf-8")


@mcp.tool()
def write_file(file_path: str, content: str, overwrite: bool = False) -> str:
    """
    写入文件内容
    
    Args:
        file_path: 文件路径（相对于工作目录）
        content: 要写入的内容
        overwrite: 是否覆盖已存在的文件
    
    Returns:
        操作结果
    """
    full_path = WORK_DIR / file_path
    
    # 安全检查
    try:
        full_path.resolve().relative_to(WORK_DIR.resolve())
    except ValueError:
        return "错误：文件路径超出工作目录范围"
    
    if full_path.exists() and not overwrite:
        return f"错误：文件已存在，设置 overwrite=True 覆盖"
    
    # 创建父目录
    full_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 写入文件
    full_path.write_text(content, encoding="utf-8")
    
    return f"成功：文件已写入 - {file_path}"


@mcp.tool()
def list_files(directory: str = "") -> str:
    """
    列出目录中的文件
    
    Args:
        directory: 目录路径（相对于工作目录）
    
    Returns:
        文件列表
    """
    full_path = WORK_DIR / directory if directory else WORK_DIR
    
    # 安全检查
    try:
        full_path.resolve().relative_to(WORK_DIR.resolve())
    except ValueError:
        return "错误：目录路径超出工作目录范围"
    
    if not full_path.exists():
        return f"错误：目录不存在 - {directory}"
    
    if not full_path.is_dir():
        return f"错误：路径不是目录 - {directory}"
    
    # 列出文件
    files = []
    for item in full_path.iterdir():
        file_type = "📁" if item.is_dir() else "📄"
        files.append(f"{file_type} {item.name}")
    
    return "\n".join(files)


@mcp.tool()
def delete_file(file_path: str) -> str:
    """
    删除文件
    
    Args:
        file_path: 文件路径（相对于工作目录）
    
    Returns:
        操作结果
    """
    full_path = WORK_DIR / file_path
    
    # 安全检查
    try:
        full_path.resolve().relative_to(WORK_DIR.resolve())
    except ValueError:
        return "错误：文件路径超出工作目录范围"
    
    if not full_path.exists():
        return f"错误：文件不存在 - {file_path}"
    
    if full_path.is_dir():
        return "错误：不能删除目录，请使用其他工具"
    
    full_path.unlink()
    
    return f"成功：文件已删除 - {file_path}"


# ============ Resources ============

@mcp.resource("file://{file_path}")
def get_file_content(file_path: str) -> str:
    """
    以资源形式获取文件内容
    """
    full_path = WORK_DIR / file_path
    
    if not full_path.exists():
        return f"文件不存在：{file_path}"
    
    return full_path.read_text(encoding="utf-8")


# ============ Prompts ============

@mcp.prompt()
def file_editor_instructions() -> str:
    """
    文件编辑器的使用提示词
    """
    return """
你是一个文件编辑助手。你可以：
1. 读取文件内容（使用 read_file）
2. 写入/修改文件（使用 write_file）
3. 列出目录内容（使用 list_files）
4. 删除文件（使用 delete_file）

操作前请确认：
- 文件路径正确
- 有权限操作该文件
- 重要文件修改前建议先备份
"""


# ============ 运行 ============

if __name__ == "__main__":
    mcp.run()
