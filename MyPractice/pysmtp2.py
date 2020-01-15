# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方SMTP服务
mail_host = 'smtp.126.com'
mail_user = ['ching125@126.com']
mail_sender = 'chenhongwu1988@126.com'
mail_pass = 'ching2020'
mail_charset = 'utf-8'


# 创建一个带附件的示例
message = MIMEMultipart()
message['From'] = Header('aforge', mail_charset)
message['To'] = Header('测试', mail_charset)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, mail_charset)

# 邮件正文
message.attach(MIMEText('这是aforge邮件测试。。。', 'plain', mail_charset))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', mail_charset)
att1['Content-Type'] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1['Content-Disposition'] = 'attachment; filename="test.txt"'
message.attach(att1)


# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('test.txt', 'rb').read(), 'base64', mail_charset)
att2['Content-Type'] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment; filename="test2.txt"'
message.attach(att2)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.set_debuglevel(True)
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_sender, mail_pass)
    smtpObj.sendmail(mail_sender, mail_user, message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('无法发送邮件')

smtpObj.close()
smtpObj.quit()




