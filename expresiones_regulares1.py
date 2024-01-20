#! /usr/bin/env python3
#_*_ coding: utf8 _*_

import re
from urllib import request


def parser_3():
    cadena = 'Esta es una cadena de ejemplo para aplicar otra funcion de "re" '
    # Funcion sub() Esta recibe 3 argumentos, nos ayuda a reemplazar valores de una cadena de texto, codigo fuente o datos externos
    cadena1 = re.sub('funcion','categoria',cadena)
    print(cadena1)


def parser_2():
    #Ejemplo 2, funcion findall() esta nos permite encontrar multiples resultados en cadenas de texto enormes
    pagina = open('metasploitable.html','r')
    for l in pagina.readlines():
        b = re.findall('^<html>',l) #^ Si especificamos este caracter al inicio de una string siginifica que la liea de codigo tiene que empezar forzosamente con esa string para que proceda al siguiente paso
        if b:
            print(b)
        b = re.findall('</html>$',l) #$ Simbolo de dolar al final de una string significa que la linea de codigo tiene que terminar forzosamente con esa string o con esa serie de caracteres para proseguir con el siguiente paso
        if b:
            print(b)
        b = re.findall('<li>.*</li>',l) #El dot hace referencia a todo tipo de caracter, y el asterisco hace referencia a que este caracter se pueda repetir n cantidad de veces, el objetivo es que se encuentre cualquier tipo de caracter las veces que sean necesarias siempre y cuando se encuentren dentro de las etiquetas establecidas
        if b:
            for c in b:
                d = re.split('<li>',c) #La funcion split() nos permite cortar un elemento a base de un caracter
                print(d)

def parser_1():
    pagina = open('metasploitable.html','r')
    for l in pagina.readlines():
        #Ejemplo 1, funcion search() nos devuelve un objeto para verificar si la busqueda es econtrada, solo sirve para cantidades pequeñas de texto

        b = re.search('Lorem',l)
        if b:
            print(l)
        else:
            pass
            
def main():
    parser_1()
    parser_2()
    parser_3()
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
