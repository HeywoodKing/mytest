from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# 实例化DummyAuthorizer来创建ftp用户
authoorizer = DummyAuthorizer()

# 参数：用户名，密码，目录，权限
authoorizer.add_user('admin', '123456', r'E:\test', perm='elradfmwMT')

# 匿名登录
handler = FTPHandler
handler.authorizer = authoorizer

# 参数：IP,端口，handler
server = FTPServer(('0.0.0.0', 2121), handler)
server.serve_forever()

"""
FTP对象常用方法

ftp.cwd(path)                    设置FTP当前操作的路径，同linux中的cd

ftp.dir()                             显示目录下所有信息

ftp.nlst()                            获取目录下的文件，显示的是文件名列表

ftp.mkd(directory)             新建远程目录

ftp.rmd(directory)              删除远程目录

ftp.rename(old, new)         将远程文件old重命名为new

ftp.delete(file_name)          删除远程文件

ftp.storbinary(cmd, fp, bufsize)             上传文件，cmd是一个存储命令，可以为"STOR filename.txt"， fp为类文件对象（有read方法），bufsize设置缓冲大小

ftp.retrbinary(cmd, callback, bufsize)              下载文件，cmd是一个获取命令，可以为"RETR filename.txt"， callback是一个回调函数，用于读取获取到的数据块

"""
