# MCP 示例代码

这里是《MCP 学习指南》中的所有示例代码，按难度递增排列。

## 📁 项目结构

```
code/
├── 01_hello_server/      # Hello World 示例（入门）
├── 02_file_manager/      # 文件管理 Server（基础）
├── 03_weather_server/    # 天气查询 Server（API 集成）
├── 04_database_server/   # 数据库查询 Server（数据库）
├── 05_todo_server/       # 待办事项 Server（完整应用）
├── utils/                # 工具函数
├── requirements.txt      # Python 依赖
└── README.md            # 本文件
```

## 🚀 快速开始

### 1. 安装依赖

```bash
cd /home/LiangWen/AI\ 学习/MCP/code
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
      "args": ["/home/LiangWen/AI 学习/MCP/code/01_hello_server/server.py"]
    },
    "file-manager": {
      "command": "python",
      "args": ["/home/LiangWen/AI 学习/MCP/code/02_file_manager/server.py"],
      "env": {
        "WORK_DIR": "/home/LiangWen"
      }
    },
    "weather": {
      "command": "python",
      "args": ["/home/LiangWen/AI 学习/MCP/code/03_weather_server/server.py"]
    },
    "todo": {
      "command": "python",
      "args": ["/home/LiangWen/AI 学习/MCP/code/05_todo_server/server.py"],
      "env": {
        "TODO_FILE": "/home/LiangWen/todos.json"
      }
    }
  }
}
```

重启 Claude Desktop 后即可使用！

## 📚 学习路线

### Week 1: 理解概念
- [ ] 阅读《MCP 学习指南.md》
- [ ] 理解 Resources/Tools/Prompts
- [ ] 运行 Hello World 示例

### Week 2: 动手实践
- [ ] 修改 Hello World，添加新功能
- [ ] 配置文件管理 Server
- [ ] 在 Claude 中测试

### Week 3: 进阶开发
- [ ] 运行天气查询示例
- [ ] 集成自己的 API
- [ ] 添加错误处理和日志

### Week 4: 项目实战
- [ ] 待办事项 Server 实战
- [ ] 定制自己的 MCP Server
- [ ] 分享给朋友！

## 🔧 调试工具

**MCP Inspector:**
```bash
npx @modelcontextprotocol/inspector python 01_hello_server/server.py
```

Inspector 会打开一个 Web 界面，可以：
- 查看可用的 Tools/Resources/Prompts
- 手动调用工具测试
- 查看日志和错误信息

## 🛡️ 安全提示

1. **路径安全**: 使用 `utils/safety.py` 中的 `safe_path()` 函数
2. **SQL 注入**: 使用参数化查询，禁止危险操作
3. **权限控制**: 限制工作目录范围
4. **输入验证**: 始终验证用户输入

## 📖 相关资源

- [MCP 官方文档](https://modelcontextprotocol.io)
- [MCP GitHub](https://github.com/modelcontextprotocol)
- [Python SDK](https://pypi.org/project/mcp/)

---

*代码整理：Claw🦞*
*最后更新：2026 年 3 月 16 日*
*雯雯加油！有问题随时问我～*
