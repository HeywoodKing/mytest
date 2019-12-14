# import smtplib
# smtpobj = smtplib.SMTP(host='localhost',port=25,local_hostname='127.0.0.1')
# senmailtest = SMTP.sendmail(from_addr='',to_addrs='',msg=[mail_options,rcpt_options])


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

# 调用第三方SMTP服务
mail_host = "smtp.126.com"
mail_user = "chenhongwu1988@126.com"
mail_pass = "Abcd1234"

sender = mail_user
receivers = 'xuqi@huachunent.com'

message = MIMEText(
    '您之所以收到这封邮件，是因为我调试你的程序给您发的测试邮件',
    'plain',
    'utf-8')
message['Subject'] = Header("自动化测试报告", charset='utf-8')
message['from'] = sender
message['to'] = receivers

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
except KeyboardInterrupt as ex:
    print(ex)
except Exception as ex:
    print(ex)
