# -*- coding: utf-8 -*-


import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr, formatdate


# 发送邮件
"""
hotmail的服务器地址如下：
pop服务器地址：pop-mail.outlook.com   110/995
smtp服务器地址：smtp-mail.outlook.com  25/
imap服务器地址：imap-mail.outlook.com  143/

Google Gmail
IMAP, SMTP, POP3 得設定值, 整理如下:

IMAP
imap.gmail.com
Port: 993
Use SSL: Yes

SMTP
smtp.gmail.com
Port for TLS/STARTTLS: 587
Port for SSL: 465

POP3
pop.gmail.com
Port: 995
Use SSL: Yes


阿里云邮箱
已经支持POP3收信和SMTP发信功能，默认已开启。阿里云邮箱服务器信息：
服务器名称   服务器地址          服务器端口号（非加密）   服务器端口号（SSL加密）
POP3     pop3.aliyun.com       110                      995
SMTP     smtp.aliyun.com       25                       465
IMAP	 imap.aliyun.com	   143	                    993



腾讯企业邮箱
POP3/SMTP协议
接收邮件服务器：pop.exmail.qq.com ，使用SSL，端口号995
发送邮件服务器：smtp.exmail.qq.com ，使用SSL，端口号465
海外用户可使用以下服务器
接收邮件服务器：hwpop.exmail.qq.com ，使用SSL，端口号995
发送邮件服务器：hwsmtp.exmail.qq.com ，使用SSL，端口号465
 
IMAP协议
接收邮件服务器：imap.exmail.qq.com  ，使用SSL，端口号993
发送邮件服务器：smtp.exmail.qq.com ，使用SSL，端口号465
海外用户可使用以下服务器
接收邮件服务器：hwimap.exmail.qq.com ，使用SSL，端口号993
发送邮件服务器：hwsmtp.exmail.qq.com ，使用SSL，端口号465


腾讯QQ邮箱
POP3：pop.qq.com 
SMTP：smtp.qq.com 
IMAP：imap.qq.com 端口：143


网易163免费邮箱
服务器名称   服务器地址          服务器端口号（非加密）   服务器端口号（SSL加密）
IMAP        imap.163.com        143                     993
SMTP        smtp.163.com        25                      465/994
POP3        pop.163.com         110                     995


"""


def _formataddr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(to_addrs, mail_title, mail_content):
    sender = 'opencoding@hotmail.com'
    if isinstance(to_addrs, list):
        receiver = to_addrs
    else:
        receiver = [to_addrs]

    print(receiver)
    mail_host = 'smtp-mail.outlook.com'
    mail_port = 25
    mail_user = 'opencoding@hotmail.com'
    mail_pass = ''

    # msg = MIMEText(mail_content, 'plain', 'utf-8')
    # msg = MIMEText(mail_content, 'html', 'utf-8')

    # 带附件邮件
    # 指定subtype为alternative，同时支持html和plain格式
    msg = MIMEMultipart('alternative')
    # 添加邮件正文
    # 邮件正文中显示图片，同时附件的图片将不再显示
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    msg['From'] = formataddr(['小黑', sender])
    # 接收人为一个
    # msg['To'] = formataddr(['小白', receiver])
    # 接收人为多个
    msg['to'] = '%s' % ','.join([_formataddr('<%s>' % to_addr) for to_addr in receiver])
    msg['Date'] = formatdate()
    msg['Subject'] = Header(mail_title, 'utf-8')

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(r'E:\Photos\新建文件夹\IMG_4532.JPG', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='test.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    smtp = None
    flag_mail_ssl = False
    try:
        if flag_mail_ssl:
            smtp = smtplib.SMTP_SSL(mail_host, mail_port)
        else:
            smtp = smtplib.SMTP(mail_host, mail_port)

        smtp.connect(mail_host, mail_port)
        # 打印与服务器的交互信息
        # smtp.set_debuglevel(1)
        smtp.ehlo()  # 向hotemail发送SMTP 'ehlo' 命令
        smtp.starttls()
        smtp.login(mail_user, mail_pass)
        smtp.sendmail(sender, receiver, msg.as_string())
        return True
    except Exception as e:
        print('error', e)
        return False
    finally:
        smtp.quit()


res = send_mail(['chenhongwu666@163.com', 'chenhongwu1988@126.com'],
                'python email test', '你好，这是一份测试邮件')
if res:
    print('发送成功')
else:
    print('发送失败')

