#! /usr/bin/env python3
#_*_ coding: utf8_*_

import re
import urllib.request

def get_li():
    code = urllib.request.urlopen('https://lorem2.com/')
    code = code.read()
    todo = re.findall('<li>(.+?)</li>', str(code)) # El parentesis le da prioridad al contenido que se encuentre dentro y no a las etiquetas, el simbolo de suma especifica el numero de veces que se repetira el patron, tiene que ser mayor a 0

    for t in todo:
        if not 'a href=' in t: # Si no se encuentra la etiqueta en la variable t, se imprime el contenido, es un filtro
            print(t + '\n')

def main():
    get_li()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Salida manual ejecutada')
        exit()
