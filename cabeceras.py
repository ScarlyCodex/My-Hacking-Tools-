#! /usr/bin/env python3 
#_*_coding:utf8_*_

import requests
import argparse 

parser = argparse.ArgumentParser(description='Detector de cabeceras') #Se convierte a "parser" en un objeto de la clase ArgumentParser del modulo argparse.
parser.add_argument('-t', '--target', help="Introduce el objetivo")
parser = parser.parse_args()

def main():
	if parser.target: #Esta es la variable que contendra el obejtivo si se usa -t o --target para indicar uno
		 try:
		 	url = requests.get(url=parser.target)
		 	cabeceras = dict(url.headers) # Headers es una clase que nos devuelve un valor con el contenido de la respuesta de aquel sitio web
		 	for x in cabeceras:
		 		print(x + ' : ' + cabeceras[x]) # x será la llave, osea la equivalencia de las solicitudes que estamos pidiendo
		 except:
		 	print('No me pude conectar')
	else:
		print('No hay objetivo')


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Saliendo')