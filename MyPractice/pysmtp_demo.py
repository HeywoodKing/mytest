# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

mail_host = 'smtp.126.com'
mail_user = ['chenhongwu1988@126.com', ]  # 收件人
mail_sender = 'chenhongwu1988@126.com'  # 发件人
mail_pass = 'ching2020'  # 发件人授权码
mail_charset = 'utf-8'

def mail():
    '发送邮件'
    ret = True
    try:
        msg = MIMEText('这是一份测试邮件', 'plain', mail_charset)
        msg['From'] = formataddr(['Turbine', mail_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(['FK', mail_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = 'AForge邮件测试'  # 邮件的主题，也可以说是标题
        server = smtplib.SMTP(mail_host, 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.set_debuglevel(False)  # 设置调试模式
        server.login(mail_sender, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(mail_sender, mail_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except smtplib.SMTPException:
        ret = False
    except Exception:
        ret = False
    return ret


ret = mail()
if ret:
    print('邮件发送成功')
else:
    print('邮件发送失败')





