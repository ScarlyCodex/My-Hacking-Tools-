#! /usr/bin/env python3
#_*_ coding: utf8_*_

import dns.resolver
from os import path

def main():
    if path.exists('subdominios.txt'):
        wordlist = open('subdominios.txt','r')
        wordlist = wordlist.read().split('\n')
        sub_dominios = []

        for x in wordlist:
            try:
                a = dns.resolver.resolve(f'{x}.google.com','A')
                sub_dominios.append('{}.google.com'.format(x))
            except:
                pass

        if len(lista) > 0:
            print('Numero de subdominios posbiles: {}'.format(len(sub_dominios)))

            for e in sub_dominios:
                print(e)
        else:
            print('No se encontraron subdominios')

    else:
        print('No existe el archivo')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
