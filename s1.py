#! /usr/bin/env python3
#_*_ coding: utf8_*_

import importlib
import sys
from shodan import Shodan

def main():
    importlib.reload(sys)

    api = Shodan('QtcX46X6yx81l2EP69fN7EeFB0oLptOE') #api pasa a ser un objeto de la clase Shodan del modulo shodan, ahora con api se puede acceder a las funciones que contenga la clase Shodan
    h = api.host('117.48.120.226') #h = host
    #print(h.keys()) este codigo nos ayuda a obtener las llaves de los diccionarios, la funcion keys se aplica a cualquier diccionario

    print('''
    Direccion: {}
    Ciudad: {}
    ISP: {}
    ORG: {}
    ASN: {}
    PORTS: {}

    '''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['asn'],h['ports']))

    archivo = open('scaneo.txt','a+',encoding='utf-8')

    for elemento in h['data']:
        lista = elemento.keys()
        for l in lista:
            archivo.write(str(elemento[l]))

    archivo.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
