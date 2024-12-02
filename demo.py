# -*- coding = utf-8 -*-
# @Time : 2024/11/5 22:24
# @Author : Cat_E
# @File : demo.py
# @Software : PyCharm


import smtplib

try:
    # 创建一个 SMTP 连接对象
    server = smtplib.SMTP('smtp.qq.com', 587)

    # 启用 TLS 加密
    server.starttls()

    # 登录 QQ 邮箱
    server.login('3147272673@qq.com', 'dvmilsvbmebyddih')

    # 如果连接成功，则打印成功消息
    print("SMTP connection successful!")

    # 关闭连接
    server.quit()
except Exception as e:
    print("Error:", e)
