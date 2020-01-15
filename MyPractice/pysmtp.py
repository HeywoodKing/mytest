# -*- coding: UTF-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = 'smtp.126.com'
mail_user = ['ching125@126.com']  # 收件人
mail_sender = 'chenhongwu1988@126.com'  # 发件人
mail_pass = 'ching2020'  # 发件人授权码
mail_charset = 'utf-8'

mail_msg = '''
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
'''

message = MIMEText('Python 邮件发送测试。。。1', 'plain', mail_charset)
message['From'] = Header('aforge', mail_charset)
message['To'] = Header('测试', mail_charset)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, mail_charset)

try:
    # smtpObj = smtplib.SMTP('localhost')
    smtpObj = smtplib.SMTP()
    smtpObj.set_debuglevel(False)
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_sender, mail_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
    smtpObj.sendmail(mail_sender, mail_user, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    print('邮件发送成功')
except smtplib.SMTPException:
    print('无法发送邮件')

# smtpObj.close()
smtpObj.quit()
