# Filename: mysubprocess.py
# coding: gbk

import subprocess
#rc = subprocess.call(["cmd","10"])
#out = subprocess.call("ls -l",shell=True)
#out = subprocess.call("cd ..",shell=True)

child = subprocess.Popen(["ping", "-c","5","www.google.com"])
child.wait()
#child.poll()           # 检查子进程状态
#child.kill()           # 终止子进程
#child.send_signal()    # 向子进程发送信号
#child.terminate()      # 终止子进程
print("parent process: " + str(child.pid))
print(child.stdin)
print(child.stdout)
print(child.stderr)

#child1 = subprocess.Popen(["ls","-l"], stdout=subprocess.PIPE)
#child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE)

child1 = subprocess.Popen(["cmd","-l"], stdout=subprocess.PIPE)
child2 = subprocess.Popen(["calc"], stdin=child1.stdout,stdout=subprocess.PIPE)
out = child2.communicate()
print(out)

child3 = subprocess.Popen(["cmd"],stdin=subprocess.PIPE)
out = child3.communicate("ching")
print(out)

#subprocess.call()
#父进程等待子进程完成

#subprocess.check_call()
#父进程等待子进程完成
#返回0

#subprocess.check_output()
#父进程等待子进程完成
#返回子进程向标准输出的输出结果






