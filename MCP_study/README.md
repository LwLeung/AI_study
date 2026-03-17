# MCP 学习指南

> Model Context Protocol —— 让 AI 模型与外部世界对话的桥梁
> 
> 📚 配合 [MCP-notes](https://github.com/LwLeung/MCP-notes) 仓库使用效果更佳！
> 
> 版本：1.0 | 更新日期：2026 年 3 月 17 日

---

## 📖 关于 MCP

**MCP (Model Context Protocol)** 是一个用于连接 AI 应用程序与外部系统的开源标准协议。

简单说：**MCP 让 AI 能够"伸手"到外部世界获取数据和执行操作。**

### 核心概念

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   AI 客户端   │ ──→ │   MCP 协议   │ ←── │  外部服务   │
│  (Claude 等) │     │  (标准化)   │     │ (文件/DB/API)│
└─────────────┘     └─────────────┘     └─────────────┘
```

### 三大原语

| 原语 | 说明 | 示例 |
|------|------|------|
| **Tools** | 可执行的操作 | 查询天气、读写文件 |
| **Resources** | 数据源 | 文件内容、数据库记录 |
| **Prompts** | 提示词模板 | 代码审查、任务指导 |

---

## 📁 项目结构

```
MCP_study/
├── 01_hello_server/       # Hello World 示例（入门）
├── 02_file_manager/       # 文件管理 Server（基础）
├── 03_weather_server/     # 天气查询 Server（API 集成）
├── 04_database_server/    # 数据库查询 Server（数据库）
├── 05_todo_server/        # 待办事项 Server（完整应用）
├── utils/                 # 工具函数库
│   ├── __init__.py
│   └── safety.py         # 安全检查工具
└── requirements.txt       # Python 依赖
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
cd MCP_study
pip install -r requirements.txt
```

### 2. 运行示例

**Hello World:**
```bash
python 01_hello_server/server.py
```

**文件管理:**
```bash
# 设置工作目录
export WORK_DIR="/home/LiangWen"
python 02_file_manager/server.py
```

**天气查询:**
```bash
python 03_weather_server/server.py
```

**数据库查询:**
```bash
# 创建测试数据库
sqlite3 /home/LiangWen/data.db "CREATE TABLE users (id INTEGER, name TEXT);"
sqlite3 /home/LiangWen/data.db "INSERT INTO users VALUES (1, '雯雯'), (2, 'Claw');"

# 运行 Server
python 04_database_server/server.py
```

**待办事项:**
```bash
python 05_todo_server/server.py
```

### 3. 在 Claude Desktop 中使用

编辑配置文件：

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Linux:** `~/.config/claude/claude_desktop_config.json`

添加配置：

```json
{
  "mcpServers": {
    "hello": {
      "command": "python",
      "args": ["/path/to/AI_study/MCP_study/01_hello_server/server.py"]
    },
    "file-manager": {
      "command": "python",
      "args": ["/path/to/AI_study/MCP_study/02_file_manager/server.py"],
      "env": {
        "WORK_DIR": "/home/LiangWen"
      }
    },
    "weather": {
      "command": "python",
      "args": ["/path/to/AI_study/MCP_study/03_weather_server/server.py"]
    },
    "todo": {
      "command": "python",
      "args": ["/path/to/AI_study/MCP_study/05_todo_server/server.py"],
      "env": {
        "TODO_FILE": "/home/LiangWen/todos.json"
      }
    }
  }
}
```

重启 Claude Desktop 后即可使用！

---

## 📚 学习路线

### Week 1: 理解概念

- [ ] 阅读 MCP 官方文档
- [ ] 理解 Resources/Tools/Prompts
- [ ] 运行 Hello World 示例
- [ ] 理解 JSON-RPC 2.0 协议

**推荐文档：**
- [MCP 入门介绍](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP 架构概览](https://modelcontextprotocol.io/docs/learn/architecture)

### Week 2: 动手实践

- [ ] 修改 Hello World，添加新功能
- [ ] 配置文件管理 Server
- [ ] 在 Claude Desktop 中测试
- [ ] 尝试读写文件

**实践任务：**
- 修改 `say_hello` 函数，支持多种语言
- 配置文件管理 Server 的工作目录
- 在 Claude 中测试文件读写

### Week 3: 进阶开发

- [ ] 运行天气查询示例
- [ ] 集成自己的 API
- [ ] 添加错误处理和日志
- [ ] 学习安全最佳实践

**实践任务：**
- 添加更多城市支持
- 添加缓存机制
- 实现日志记录

### Week 4: 项目实战

- [ ] 待办事项 Server 实战
- [ ] 定制自己的 MCP Server
- [ ] 发布到 GitHub
- [ ] 分享给朋友！

**毕业项目：**
- 设计并实现一个自己的 MCP Server
- 可以是：笔记管理、书签管理、个人 API 等
- 发布到 GitHub 并分享

---

## 🔧 调试工具

### MCP Inspector

```bash
# 安装
npx @modelcontextprotocol/inspector

# 运行并检查你的 Server
npx @modelcontextprotocol/inspector python 01_hello_server/server.py
```

Inspector 会打开一个 Web 界面，可以：
- 查看可用的 Tools/Resources/Prompts
- 手动调用工具测试
- 查看日志和错误信息

### 日志调试

在各个 Server 中添加日志：

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@mcp.tool()
def my_tool(arg: str) -> str:
    logger.info(f"调用 my_tool，参数：{arg}")
    # ... 你的代码 ...
```

---

## 🛡️ 安全最佳实践

### 1. 路径安全

```python
from pathlib import Path

def safe_path(user_path: str, base_dir: Path) -> Path:
    """确保路径在允许的范围内"""
    full_path = (base_dir / user_path).resolve()
    try:
        full_path.relative_to(base_dir.resolve())
        return full_path
    except ValueError:
        raise ValueError("路径超出允许范围")
```

### 2. SQL 注入防护

```python
# ❌ 错误做法
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")

# ✅ 正确做法
cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
```

### 3. 权限控制

- 限制工作目录范围
- 只允许 SELECT 查询（数据库）
- 验证所有用户输入

### 4. 错误处理

```python
@mcp.tool()
def read_file(file_path: str) -> str:
    try:
        # ... 文件操作 ...
    except PermissionError:
        return "错误：没有读取权限"
    except UnicodeDecodeError:
        return "错误：文件不是文本格式"
    except Exception as e:
        return f"错误：{str(e)}"
```

---

## 📖 示例代码说明

### 01_hello_server

最简单的 MCP Server，适合入门学习。

**功能：**
- 一个简单的打招呼工具

**学习点：**
- MCP Server 基本结构
- 如何定义工具
- 如何运行 Server

### 02_file_manager

文件管理 MCP Server，可以读写文件。

**功能：**
- 读取文件内容
- 写入文件内容
- 列出目录内容
- 删除文件

**学习点：**
- 路径安全检查
- 文件操作
- Resources 和 Prompts

### 03_weather_server

天气查询 MCP Server，集成外部 API。

**功能：**
- 查询城市天气
- 支持多个城市

**学习点：**
- HTTP API 调用
- 数据格式化
- 错误处理

### 04_database_server

数据库查询 MCP Server，连接 SQLite。

**功能：**
- 执行 SQL 查询（只读）
- 列出所有表
- 查看表结构
- 示例查询

**学习点：**
- 数据库连接
- SQL 安全防护
- 结果格式化

### 05_todo_server

待办事项管理 MCP Server，完整应用示例。

**功能：**
- 添加待办事项
- 列出待办事项
- 标记为完成
- 删除待办事项
- 查看统计

**学习点：**
- 数据持久化（JSON）
- 完整 CRUD 操作
- 数据统计

---

## 📚 相关资源

### 官方资源

| 资源 | 链接 |
|------|------|
| **MCP 官网** | https://modelcontextprotocol.io |
| **GitHub** | https://github.com/modelcontextprotocol |
| **Python SDK** | https://pypi.org/project/mcp/ |
| **规范文档** | https://spec.modelcontextprotocol.io |
| **官方示例** | https://github.com/modelcontextprotocol/servers |

### 学习文档

| 文档 | 说明 |
|------|------|
| [MCP 入门介绍](https://modelcontextprotocol.io/docs/getting-started/intro) | 什么是 MCP |
| [MCP 架构概览](https://modelcontextprotocol.io/docs/learn/architecture) | 核心概念和架构 |
| [构建服务器](https://modelcontextprotocol.io/docs/develop/build-server) | 如何构建 MCP Server |

### 知识库

| 仓库 | 说明 |
|------|------|
| **[MCP-notes](https://github.com/LwLeung/MCP-notes)** | MCP 学习笔记（Obsidian） |

---

## ❓ 常见问题

### Q: MCP 有什么用？
A: MCP 让 AI 能够连接外部系统，比如读取你的文件、查询数据库、调用 API 等。

### Q: 必须用 Claude 吗？
A: 不是，任何支持 MCP 的 AI 应用都可以，比如 ChatGPT、VS Code 等。

### Q: 本地 Server 和远程 Server 有什么区别？
A: 
- **本地 Server**：在你的电脑上运行，使用 Stdio 传输
- **远程 Server**：在服务器上运行，使用 HTTP 传输

### Q: 如何调试？
A: 使用 MCP Inspector，或者在代码中添加日志。

### Q: 安全吗？
A: MCP 本身是安全的，但要注意：
- 限制工作目录
- 验证用户输入
- 使用参数化查询
- 不要暴露敏感信息

---

## 📝 更新日志

### 2026-03-17
- ✨ 创建 MCP_study 文件夹
- 📝 添加本 README
- 🔧 整理所有示例代码

### 2026-03-16
- 🎉 初始提交 5 个 MCP Server 示例
- 📚 包含完整学习路线和文档

---

*整理：Claw🦞*
*最后更新：2026 年 3 月 17 日*

> 雯雯加油学！有问题随时问我～ 📚
