# Codex Python Starter Repository

这是一个面向新人友好的 Python 项目基础骨架，目标是提供：

- 清晰的目录结构
- 一键运行测试与基础检查
- 明确的贡献与提交流程

## 快速开始

### 1) 环境要求

- Python 3.10+

### 2) 运行测试

```bash
make test
```

### 3) 运行示例代码

```bash
python -m src.main
```

## 目录结构

```text
.
├── src/                    # 业务代码
│   ├── __init__.py
│   ├── main.py             # 程序入口示例
│   └── math_utils.py       # 示例模块
├── tests/                  # 单元测试
│   ├── __init__.py
│   └── test_math_utils.py
├── docs/
│   └── onboarding.md       # 新人上手文档
├── .github/workflows/
│   └── ci.yml              # CI 配置
├── CONTRIBUTING.md         # 协作规范
├── Makefile                # 常用命令入口
└── pyproject.toml          # Python 项目基础配置
```

## 开发命令

- `make test`：运行单元测试
- `make check`：运行基础检查（语法编译 + 测试）
- `make run`：运行示例入口

