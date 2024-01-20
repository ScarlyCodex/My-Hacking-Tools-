#! /usr/bin/env python3
#_*_ coding: utf8_*_

from Wappalyzer import WebPage, Wappalyzer


def main():
	wap = Wappalyzer.latest()
	try:
		web = WebPage.new_from_url('https://www.example.com')
		tec = wap.analyze(web)
		for x in tec:
			print('Tecnologia detectada: {}'.format(x))
	except:
		print('Ha ocurrido un error')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Saliendo')
		exit()