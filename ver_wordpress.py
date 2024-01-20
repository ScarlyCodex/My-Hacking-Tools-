#! /usr/bin/env python3
#_*_ coding: utf8_*_

import requests
from bs4 import BeatifulSoup

def main():
	url = 'https://conectome.odoo.com/?'
	cabecera = {'User-Agent':'Chrome'}
	pet = requests.get(url=url, headers=cabecera)
	print(pet.text)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Saliendo')
