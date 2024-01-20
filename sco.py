#! /usr/bin/env python3
#_*_ coding: utf8_*_

import socket #importar modulo de socket

def main():
    s = socket.socket() #convertir una variable en un objeto del modulo socket, accediendo a la clase socket del modulo socket y convirtiendo a "s" en un objeto
    try:
        s.connect(("dlptest.com",21)) #connect recibe dos parametros, el primero es el target al que nos queremos conectar y el segundo es el puerto por el cual nos queremos conectar
        banner = s.recv(1024) #buffer de 24, igualar el resultado de recv a la variable banner con un tamaño de 1024 bytes en el buffer
        print(banner)

    except:
        print('Ocurrio un error en la conexión')

if __name__ == '__main__':
    main()
