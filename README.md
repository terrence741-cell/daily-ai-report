# 梦想屋AI日报自动发送

每天自动生成 AI 资讯日报并发送到邮箱。

---

## 功能

- 📅 每天 21:00 自动运行（北京时间）
- 📰 生成 5 条精选 AI 资讯
- 📧 自动发送到邮箱
- 👀 用"AI小白怎么理解"解释每条资讯

---

## 配置步骤

### 1. 创建 GitHub 仓库

1. 登录 GitHub
2. 创建新仓库，命名为 `daily-ai-report`（或你喜欢的名字）
3. 设置为 **Public**（私有仓库 Actions 分钟数有限）

### 2. 上传代码

把这个文件夹里的所有文件上传到 GitHub 仓库：
```
.github/workflows/daily-report.yml
generate_report.py
README.md
```

### 3. 配置 163 邮箱

#### 第一步：开启 SMTP 服务

1. 登录 163 邮箱网页版
2. 点击「设置」→「POP3/SMTP/IMAP」
3. 开启「SMTP 服务」
4. 记录下「授权密码」（不是你的登录密码！）

#### 第二步：配置 GitHub Secrets

在 GitHub 仓库中配置 Secrets：

1. 进入仓库 → Settings → Secrets and variables → Actions
2. 点击「New repository secret」
3. 添加以下 4 个 secrets：

| Name | Value | 说明 |
|------|--------|------|
| `SMTP_HOST` | `smtp.163.com` | 163 邮箱 SMTP 服务器 |
| `SMTP_PORT` | `465` | SMTP 端口 |
| `SMTP_USER` | 你的163邮箱地址 | 例如：yourname@163.com |
| `SMTP_PASS` | 授权密码 | 在邮箱设置中获取 |
| `TO_EMAIL` | 你的邮箱地址 | 收件人，可以是同一地址 |
| `FROM_EMAIL` | 你的邮箱地址 | 发件人，可以和 SMTP_USER 相同 |

### 4. 测试运行

1. 进入仓库 → Actions
2. 选择「梦想屋AI日报自动发送」工作流
3. 点击「Run workflow」手动运行测试
4. 检查邮箱是否收到邮件

---

## 发送时间

当前设置为：**每天北京时间 21:00**

如果需要修改时间，编辑 `.github/workflows/daily-report.yml` 文件：

```yaml
schedule:
  - cron: '0 13 * * *'  # UTC 13:00 = 北京 21:00
```

时间格式说明：
- `0` = 分钟
- `13` = 小时（UTC，北京时间 = UTC + 8）
- `*` = 每天

示例：
```yaml
'0 5 * * *'   # 每天 13:00
'0 9 * * *'   # 每天 17:00
'0 13 * * *'  # 每天 21:00（当前）
```

---

## 当前状态

**⚠️ 注意：** 当前日报内容是示例模板，需要接入真实的资讯源。

后续需要实现：
- [ ] 接入新闻 API 或爬取新闻网站
- [ ] 自动筛选和排序新闻
- [ ] 生成"AI小白怎么理解"部分

目前每天会发送固定的示例内容。

---

## 目录结构

```
公众号日报/
├── .github/
│   └── workflows/
│       └── daily-report.yml    # GitHub Actions 配置
├── generate_report.py              # 日报生成脚本
└── README.md                     # 本文件
```

---

## 故障排查

### 邮件发送失败

检查以下内容：
1. GitHub Secrets 是否正确配置
2. 163 邮箱 SMTP 服务是否开启
3. 授权密码是否正确（不是登录密码）

### Actions 运行失败

1. 进入仓库 → Actions
2. 点击失败的运行记录
3. 查看日志，找到错误信息

---

## 后续优化

- [ ] 接入真实新闻源
- [ ] 自动生成"AI小白怎么理解"
- [ ] 支持手动触发生成指定日期的日报
- [ ] 添加发送到微信群的功能（通过机器人）
