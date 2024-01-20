#! /usr/bin/env python3
# _*_ coding: utf8_*_

import json
import urllib.request

def main():

    url = 'https://ipinfo.io/185.230.61.211/json'
    v = urllib.request.urlopen(url)
    j = json.loads(v.read())

    for dato in j:
        print(dato + ': ' + j[dato])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
