#! /usr/bin/env python3
#_*_ coding: utf8_*_

import hashlib
import urllib.request

def main():
    hash = str(input("HASH --> "))
    passwordlist = urllib.request.urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt').read()
    for x in passwordlist.decode('utf-8').split('\n'):
        z = hashlib.sha224(x.encode('utf-8')).hexdigest()

        if z == hash:
            print('Password --> {}       HASH --> {}'.format(x,z))
            break
    else:
        print('\nCONTRASEÑA NO ENCONTRADA')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nSalida manual ejecutada')
        exit()
