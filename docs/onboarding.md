# 新人上手指南

## 目标

在 10 分钟内完成：

1. 拉取代码并查看目录结构
2. 运行测试，确保本地环境可用
3. 运行示例入口，理解最小开发流程

## 步骤

### 1. 检查 Python 版本

```bash
python --version
```

建议 Python 3.10+。

### 2. 运行测试

```bash
make test
```

如果通过，说明基础环境正常。

### 3. 运行示例程序

```bash
make run
```

你会看到示例输出，帮助理解项目执行路径：`src/main.py` -> `src/math_utils.py`。

## 建议学习顺序

1. `README.md`：了解项目目标与结构
2. `src/main.py`：理解入口与调用关系
3. `src/math_utils.py`：阅读最小业务逻辑
4. `tests/test_math_utils.py`：理解测试写法
5. `CONTRIBUTING.md`：遵循协作规范
