#! /usr/bin/env python3
#_*_ coding: utf8_*_

def title():
    archivo = open('metasploitable.html','r')
    inicio = '<title>'
    final = '</title>'

    for l in archivo.readlines():
        if inicio in l:
            if not "a href=" in l:
                t = l.find(inicio)
                print(l[t+len(inicio) : -len(final) -1]) #La salida en pantalla empieza despues de la longitud completa de la etiqueta <title> hasta menos la longitud de la etiqueta </title> y el menos uno es para quitar la primer llave html de dicha etiqueta

def main():
    title()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
