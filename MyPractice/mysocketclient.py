# Filename: mysocketclient.py

import socket

HOST = '192.168.1.99'
PORT = 8000

request = 'can you hear me?'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(HOST, PORT)

s.sendall(request)
reply = s.recv(1024)
print 'rely is:',reply

s.close()
