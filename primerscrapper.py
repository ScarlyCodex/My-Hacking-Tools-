#! /usr/bin/env python3
#_*_ coding: utf8_*_

import urllib.request

def main():
    file_web = open('metasploitable.html','w+')
    consulta = urllib.request.urlopen('https://lorem2.com/')
    consulta = consulta.read().decode('utf8')
    file_web.write(consulta)
    file_web.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
