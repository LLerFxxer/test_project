# test_project
![CI](https://github.com/LLerFxxer/test_project/actions/workflows/test.yml/badge.svg)
![Allure 报告](https://LLerFxxer.github.io/test_project/)
![coverage](coverage.svg)

## 接口自动化框架

`apitest/` 用分层方式组织接口用例：

```text
apitest/
├── conftest.py         # 提供client fixture, BASE_URL = "http://127.0.0.1:8000"
├── clients/            # 封装层：会发请求的类（ApiClient）
│   └── api_client.py   # 提供 ApiClient 类，内含 request login get_users 方法
├── data/               # 数据层：用例数据（cases.yml）
│   └── cases.yml       # 三条测试用例: get_user_ok get_user_404 get_user_detail
├── tests/              # 用例层：只写业务动作 + 断言
└── utils/              # 断言与工具：assert_code/assert_key/assert_schema
```

**怎么跑**（必须在 `test_project/` 目录下执行）：

```bash
cd E:\code\test_project
pytest apitest -v
```

> 共收集 6 条用例（3 个测试文件）。


技术栈：
    pytest / Allure / pymysql / GitHub Actions / Docker

项目结构：
    test_project/
    ├── .github/workflows/test.yml  # CI：pytest + Allure 报告部署 GitHub Pages
    ├── fixture_chain/              # 主线练习：fixture 链 + 数据校验
    │   ├── conftest.py             # env→config→db_conn（session 级 fixture 链）
    │   ├── query.py                # SQL 查询函数（查询逻辑集中处）
    │   ├── test_query.py           # SQL 查询测试（sqlite 内存库）
    │   └── test_verify.py          # 数据校验测试（连真实 MySQL）
    ├── apitest/                    # 顶级包
    │   ├── clients/                # 封装层：会发请求的类（ApiClient）
    │   ├── data/                   # 数据层：用例数据（cases.yml）
    │   ├── tests/                  # 用例层：只写业务动作 + 断言
    │   └── utils/                  # 断言与工具：assert_code/assert_key/assert_schema
    ├── data/                       # 测试数据 dev/test/prod.db（gitignore）
    ├── merge.py                    # 历史练习：merge 差异对比（保留）
    ├── test_merge.py               # merge 对比测试
    ├── test_integration.py         # 早期综合测试
    ├── docker-compose.yml          # MySQL 8 服务（3306:3306，root/root）
    ├── Dockerfile                  # 五行骨架：FROM/WORKDIR/COPY/RUN/CMD
    ├── .pre-commit-config.yaml     # commit 前自动跑 ruff
    ├── .gitignore
    ├── README.md                   # CI 徽章 + 覆盖率徽章 + Allure 报告链接
    └── coverage.svg                # 覆盖率徽章（README 引用，需提交）

如何贡献：
    fork → feature 分支 → PR