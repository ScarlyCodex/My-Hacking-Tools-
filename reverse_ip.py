#! /usr/bin/env python3
#_*_ coding: utf8_*_

import requests
from bs4 import BeautifulSoup

def main():
    site = 'www.cloudflare.com'
    agent = {'User-Agent':'Firefox'}
    a = requests.get(f'https://viewdns.info/reverseip/?host={site}&t=1',headers=agent)
    b = BeautifulSoup(a.text,'html5lib')
    c = b.find(id='null')
    d = c.find(border='1')

    for l in d.find_all('tr'):
        print('Sitio encontrado :' + l.td.string)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
