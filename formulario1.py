#! /usr/bin/env python3
#_*_coding: utf8_*_

import mechanize 
import argparse
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument("-b",'--buscar',help="Opción a buscar")
parser = parser.parse_args()

def main():
	if parser.buscar:
		look_up = mechanize.Browser()
		look_up.set_handle_robots(False)
		look_up.set_handle_equiv(False)
		look_up.addheaders = [('User-Agent','Chrome')]
		look_up.open("https://www.google.com")

		look_up.select_form(nr=0)
		look_up['q'] = parser.buscar

		look_up.submit()
		p = BeautifulSoup(look_up.response().read(),'html5lib')

		for l in p.find_all('a'):
			u = l.get('href')
			u = u.replace('/url?q=','')
			print(u)
			a = l.get('href')
			a = a.replace('/search?hl','')

	else:
		print("Palabra a buscar")



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()