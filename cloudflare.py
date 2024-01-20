#! /usr/bin/env python3
#_*_coding: utf8_*_

import requests

def main():
    word = 'cloudflare'
    url = requests.get('https://www.cloudflare.com/es-es/')
    cabeceras = dict(url.headers)
    verify = False
    for c in cabeceras:
        if word in cabeceras[c].lower():
            verify = True
            break
    if verify == True:
        print('Cloudflare presente')
    else:
        print('El sitio no tiene Cloudflare')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
