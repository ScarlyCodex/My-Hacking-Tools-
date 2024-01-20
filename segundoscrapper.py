#! /usr/bin/env python3
#_*_ coding: utf8_*_

def main():
    web = open('metasploitable.html','r')
    inicio = '<li>'
    final = '</li>'

    for l in web.readlines():
        if inicio in l:
            if not "a href=" in l:    
                beginning = l.find(inicio)
                beginning = beginning + len(inicio)
                end = l.find(final)
                print(l[beginning:end])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
