from ftplib import FTP
import time, tarfile, os


# ftp用户连接登录
def connect(host, port, user, password):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(user, password)
    return ftp


# 用户上传文件
def upload(ftp, server_path, client_path):
    bufsize = 1024
    fp = open(client_path, "rb")
    ftp.storbinary('STOR ' + server_path, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


# 用户下载文件
def download(ftp, server_path, client_path):
    bufsize = 1024
    fb = open(client_path, "wb")
    ftp.retrbinary('RETR ' + server_path, fb.write, bufsize)
    ftp.set_debuglevel(0)
    fb.close()


if __name__ == "__main__":
    ftp = connect("127.0.0.1", 2121, "admin", "123456")
    # ftp.dir()
    # ftp.nlst()
    # upload(ftp, "/1.txt", r"E:\1.txt")
    download(ftp, "/1.txt", r"E:\down.txt")

    # print(ftp.getwelcome())
    ftp.quit()
