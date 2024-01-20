#! /usr/bin/env python3
#_*_ coding: utf8_*_

import dns.resolver

def main():
    consultas = ['A','AAAA','NS','MD','MF','CNAME','SOA','MX','TXT','HINFO']
    try:
        for x in consultas:
            a = dns.resolver.resolve('10fastfingers.com',x)
            for i in a:
                print(i)

    except:
        print('No se ha podido concluir la consulta con exito')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
