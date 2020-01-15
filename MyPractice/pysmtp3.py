# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

# 第三方SMTP服务
mail_host = 'smtp.126.com'
mail_user = ['ching125@126.com']
mail_sender = 'chenhongwu1988@126.com'
mail_pass = 'ching2020'
mail_charset = 'utf-8'


# 创建一个带图片的示例
message = MIMEMultipart('related')
message['From'] = Header('aforge', mail_charset)
message['To'] = Header('测试', mail_charset)

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, mail_charset)

messageAlternative = MIMEMultipart('alternative')
message.attach(messageAlternative)

mail_msg = '''
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
'''
messageAlternative.attach(MIMEText(mail_msg, 'html', mail_charset))

# 指定图片为当前目录
fp = open('test.png', 'rb')
messageImage = MIMEImage(fp.read())

# 定义图片 ID，在 HTML 文本中引用
messageImage.add_header('Content-ID', '<image1>')
message.attach(messageImage)

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




