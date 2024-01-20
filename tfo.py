#! /usr/bin/env python3
#_*_ coding :utf8_*_

import requests
from bs4 import BeautifulSoup

def main():
    a = requests.get('https://who.is/whois/pelis-123.com')
    soup = BeautifulSoup(a.text,'html5lib')

    for i in soup.find_all('pre'):
        print(i.get_text())

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
