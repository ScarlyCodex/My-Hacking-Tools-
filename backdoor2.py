from socket import *
import socket

target = input()
targetIP = socket.gethostbyname(target)
portmax = 5000 

port = []

for i in range(1, portmax -1):
    port.append(i)

print('Scanning ports...')

for number in port:

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        result = s.connect_ex((targetIP, number))
        if result == 0:
            print(number)

        s.close()

    except:
        print('Error de escaneo')
    