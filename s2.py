#! /usr/bin/env python3
#_*_ coding: utf8_*_

import sys
import importlib
from shodan import Shodan
import argparse

importlib.reload(sys)

parser = argparse.ArgumentParser()
parser.add_argument('-q','--query',help="Consulta")
parser.add_argument('-a','--api',help="Tu api")
parser = parser.parse_args()

def main():
    if parser.query:

        if parser.api:
            api = Shodan(parser.api)

            try:
                b = api.search(parser.query)
                print('Total de targets: {}'.format(b['total']))

                for y in b['matches']:
                    print('Target encontrado: {}'.format(y['ip_str']))
            except:
                print('Error de consulta')
        else:
            print('Introduce tu api')
    else:
        print('Introduce un caracter de búsqueda')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
