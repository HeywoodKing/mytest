import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.settimeout(1)
port = 80
try:
    sk.connect(('192.168.10.96',port))
    print("Server port "+port+" OK!")
except Exception:
    print("Server port "+port+" not connect!")
sk.close()