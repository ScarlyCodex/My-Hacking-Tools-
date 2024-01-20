#! /usr/bin/env python3
#_*_ coding: utf8_*_

import sys
import importlib
from shodan import Shodan

def main():
    importlib.reload(sys)

    key = 'QtcX46X6yx81l2EP69fN7EeFB0oLptOE'
    motor = Shodan(key)

    try:
        query = motor.search('struts')
        #total = numero de resultados totales
        #matches = informacion acerca de los resultados

        print('Numero de resultados totales: {}'.format(query['total']))
        for host in query['matches']:
            print('IP: {}'.format(host['ip_str']))
            print('Puerto: {}'.format(host['port']))
            print('ORG: {}'.format(host['org']))

            try:
                print('ASN: {}'.format(host['asn']))
            except:
                print('No se han encontrado resultados para ASN')

            print('Locacion: {}'.format(host['location']))

            for l in host['location']:
                print(l + " : " + str(host['location'][l]))

            #print(host['data']) . esto puede mostrar el banner

    except:
        print('Ocurrio un error')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
