#! /usr/bin/env python3
#_*_ coding: utf8_*_

import hashlib
from urllib.request import urlopen

def main():
    hash = str(input('HASH --> '))
    wordlist = open('C:/Users/laure/Documents/pass.txt','r')

    for x in wordlist.readlines(): #readlines tambien lee todo el contenido de un archivo pero lo retorna como lista en lkugar de str, readline lo lee linea por linea y retorna str
        n = x.strip("\n") #la funcion strip limpia el caracter dado como parametro de una lista, es como el split de las strings
        n = hashlib.sha1(n.encode('utf8')).hexdigest()

        if n == hash:
            print(f'''Password --> {x}
HASH --> {n}''') # NOTE: x es la contraseña en texto plano y n es la contraseña cifrada
            break
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nSalida manual ejecutada')
        exit()
