# Filename: mysubprocess.py
# coding: gbk

import subprocess
#rc = subprocess.call(["cmd","10"])
#out = subprocess.call("ls -l",shell=True)
#out = subprocess.call("cd ..",shell=True)

child = subprocess.Popen(["ping", "-c","5","www.google.com"])
child.wait()
#child.poll()           # ����ӽ���״̬
#child.kill()           # ��ֹ�ӽ���
#child.send_signal()    # ���ӽ��̷����ź�
#child.terminate()      # ��ֹ�ӽ���
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
#�����̵ȴ��ӽ������

#subprocess.check_call()
#�����̵ȴ��ӽ������
#����0

#subprocess.check_output()
#�����̵ȴ��ӽ������
#�����ӽ������׼�����������






