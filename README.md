# AI 学习资源库

> 雯雯的 AI 学习与探索之旅
> 
> 整理：Claw🦞
> 
> 创建日期：2026 年 3 月
> 更新日期：2026 年 3 月 17 日

---

## 📖 关于本仓库

这是一个**AI 学习资源的集合仓库**，用于整理和保存各种 AI 相关的学习资料、代码示例和项目实践。

仓库会持续更新，记录雯雯在 AI 领域的学习历程～

---

## 📁 项目结构

```
AI_study/
├── MCP_study/                  # 📚 Model Context Protocol 学习
│   ├── 01_hello_server/        # Hello World 示例
│   ├── 02_file_manager/        # 文件管理 Server
│   ├── 03_weather_server/      # 天气查询 Server
│   ├── 04_database_server/     # 数据库查询 Server
│   ├── 05_todo_server/         # 待办事项 Server
│   ├── utils/                  # 工具函数
│   ├── requirements.txt        # Python 依赖
│   └── README.md              # MCP 学习详细说明
├── [未来其他项目]/              # TODO: 等待添加
└── README.md                   # 本文件
```

---

## 🗂️ 学习内容

### 当前学习

| 项目 | 说明 | 难度 | 状态 |
|------|------|------|------|
| **[MCP](./MCP_study/)** | Model Context Protocol - AI 与外部系统的连接协议 | ⭐⭐⭐ | 📖 学习中 |

### 计划学习

| 方向 | 可能内容 | 状态 |
|------|----------|------|
| **LLM 应用开发** | LangChain、LlamaIndex 等 | 📅 计划中 |
| **AI Agent** | 智能体开发、多 Agent 协作 | 📅 计划中 |
| **RAG 系统** | 检索增强生成、向量数据库 | 📅 计划中 |
| **微调部署** | 模型微调、本地部署 | 📅 计划中 |
| **其他** | 雯雯感兴趣的方向... | 💭 待讨论 |

---

## 🚀 快速开始

### MCP 学习

```bash
# 进入 MCP 学习目录
cd MCP_study

# 安装依赖
pip install -r requirements.txt

# 运行 Hello World 示例
python 01_hello_server/server.py
```

详细学习路线请查看：**[MCP_study/README.md](./MCP_study/README.md)**

---

## 📚 学习路线

### 第一阶段：MCP 基础

```
Week 1: 理解概念
├── 阅读 MCP 官方文档
├── 理解 Resources/Tools/Prompts
└── 运行 Hello World 示例

Week 2: 动手实践
├── 修改 Hello World，添加新功能
├── 配置文件管理 Server
└── 在 Claude Desktop 中测试

Week 3: 进阶开发
├── 运行天气查询示例
├── 集成自己的 API
└── 添加错误处理和日志

Week 4: 项目实战
├── 待办事项 Server 实战
├── 定制自己的 MCP Server
└── 发布到 GitHub
```

### 后续阶段

*根据雯雯的兴趣和学习进度动态调整～*

---

## 🛠️ 开发环境

### 基础要求

- Python 3.8+
- Git
- 代码编辑器（VS Code / Cursor 等）

### 可选工具

- **Claude Desktop** - 测试 MCP 集成
- **MCP Inspector** - 调试 MCP Server
- **Obsidian** - 知识管理（配合 MCP-notes 仓库）

---

## 📦 依赖管理

每个项目都有自己的 `requirements.txt`，安装时请进入对应项目目录：

```bash
# MCP 示例
cd MCP_study
pip install -r requirements.txt
```

---

## 🔧 常用命令

### MCP Inspector

```bash
# 调试 MCP Server
npx @modelcontextprotocol/inspector python MCP_study/01_hello_server/server.py
```

### Git 同步

```bash
# 提交更改
git add -A
git commit -m "描述你的更改"
git push

# 拉取更新
git pull
```

---

## 🛡️ 安全提示

1. **路径安全**: 使用 `utils/safety.py` 中的 `safe_path()` 函数
2. **SQL 注入**: 使用参数化查询，禁止危险操作
3. **权限控制**: 限制工作目录范围
4. **输入验证**: 始终验证用户输入
5. **API Key**: 不要将敏感信息提交到仓库

---

## 📖 相关资源

### MCP 相关

| 资源 | 链接 |
|------|------|
| MCP 官方文档 | https://modelcontextprotocol.io |
| MCP GitHub | https://github.com/modelcontextprotocol |
| Python SDK | https://pypi.org/project/mcp/ |
| 规范文档 | https://spec.modelcontextprotocol.io |

### AI 学习

| 资源 | 链接 |
|------|------|
| LangChain | https://python.langchain.com |
| Hugging Face | https://huggingface.co |
| LlamaIndex | https://docs.llamaindex.ai |

### 知识库

| 仓库 | 说明 |
|------|------|
| **[MCP-notes](https://github.com/LwLeung/MCP-notes)** | MCP 学习笔记（Obsidian） |

---

## 📝 更新日志

### 2026-03-17
- ✨ 整理仓库结构，将所有 MCP 相关内容移至 `MCP_study/` 文件夹
- 📝 更新 README，使其适用于多个 AI 学习项目
- 🔧 更新路径引用

### 2026-03-16
- 🎉 初始提交 MCP 示例代码
- 📚 包含 5 个完整的 MCP Server 示例

---

## 💡 使用建议

1. **按顺序学习**: 从 `01_hello_server` 开始，逐步深入
2. **动手实践**: 不要只看不做，运行代码并修改
3. **记录笔记**: 配合 MCP-notes 仓库记录学习心得
4. **定期同步**: 多台设备记得 `git pull/push`

---

## 🎯 下一步

- [ ] 完成 MCP 学习
- [ ] 确定下一个学习方向
- [ ] 添加新的学习项目
- [ ] 持续更新...

---

*整理：Claw🦞*
*最后更新：2026 年 3 月 17 日*

> 雯雯加油！AI 学习是一场马拉松，不是百米冲刺。
> 有问题随时问我，我会一直陪着你～ 💕
