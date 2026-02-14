#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
梦想屋AI日报自动生成脚本
"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import datetime

# 配置
SMTP_HOST = os.getenv('SMTP_HOST', 'smtp.163.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', '465'))
SMTP_USER = os.getenv('SMTP_USER', '')
SMTP_PASS = os.getenv('SMTP_PASS', '')
TO_EMAIL = os.getenv('TO_EMAIL', '')
FROM_EMAIL = os.getenv('FROM_EMAIL', SMTP_USER)

def generate_daily_report():
    """生成每日AI日报"""
    today = datetime.now().strftime('%Y/%m/%d')

    # 这里是示例内容，实际需要从资讯源获取
    # 暂时用固定模板，后续可以接入新闻源
    report = f"""梦想屋AI日报

📅 {today}

------------------

**1. [新闻标题示例]**

📅 2026-02-14

💡 要点：[简明扼要的新闻说明]

👀 AI小白怎么理解：[用大白话解释这个新闻对你有什么意义]


**2. [新闻标题示例]**

📅 2026-02-14

💡 要点：[简明扼要的新闻说明]

👀 AI小白怎么理解：[用大白话解释这个新闻对你有什么意义]


**3. [新闻标题示例]**

📅 2026-02-14

💡 要点：[简明扼要的新闻说明]

👀 AI小白怎么理解：[用大白话解释这个新闻对你有什么意义]


**4. [新闻标题示例]**

📅 2026-02-14

💡 要点：[简明扼要的新闻说明]

👀 AI小白怎么理解：[用大白话解释这个新闻对你有什么意义]


**5. [新闻标题示例]**

📅 2026-02-14

💡 要点：[简明扼要的新闻说明]

👀 AI小白怎么理解：[用大白话解释这个新闻对你有什么意义]


---
"""

    return report

def send_email(report_content):
    """发送邮件"""
    if not all([SMTP_USER, SMTP_PASS, TO_EMAIL]):
        print("❌ 邮件配置不完整，跳过发送")
        print("请在 GitHub Secrets 中配置：SMTP_USER, SMTP_PASS, TO_EMAIL")
        return False

    try:
        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = Header(f'梦想屋AI日报 <{FROM_EMAIL}>', 'utf-8')
        msg['To'] = Header(TO_EMAIL, 'utf-8')
        msg['Subject'] = Header(f'梦想屋AI日报 {datetime.now().strftime("%Y-%m-%d")}', 'utf-8')

        msg.attach(MIMEText(report_content, 'plain', 'utf-8'))

        # 发送邮件
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(FROM_EMAIL, TO_EMAIL, msg.as_string())
            server.quit()

        print("✅ 邮件发送成功")
        return True

    except Exception as e:
        print(f"❌ 邮件发送失败: {e}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("梦想屋AI日报生成器")
    print("=" * 50)
    print(f"⏰ 运行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 生成日报
    report = generate_daily_report()
    print("\n📰 日报生成成功")
    print("-" * 50)

    # 发送邮件
    send_email(report)
