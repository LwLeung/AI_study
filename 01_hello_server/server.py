#!/usr/bin/env python3
"""
最简单的 MCP Server - Hello World

使用方法:
    python server.py

在 Claude Desktop 配置中添加:
{
  "mcpServers": {
    "hello-server": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
"""

from mcp.server.fastmcp import FastMCP

# 创建 MCP Server 实例
mcp = FastMCP("Hello Server")

# 定义一个工具
@mcp.tool()
def say_hello(name: str) -> str:
    """向指定的人打招呼"""
    return f"你好，{name}！👋"

# 运行 Server
if __name__ == "__main__":
    mcp.run()
