#! /usr/bin/env python3
#_*_ coding: utf8_*_

from bs4 import BeautifulSoup
import mechanize

def main():
    nav = mechanize.Browser()
    nav.set_handle_robots(False)
    nav.set_handle_equiv(False)

    nav.addheaders = [('User-Agent','Firefox')]
    nav.open('inserte url') #Cualquier url
    nav.select_form(nr=0)

    #Se identifica por medio del objeto de mechanize las etiquetas con el conetnido de texto corresponiente
    nav['username'] = 'admin'
    nav['password'] = 'password'

    nav.submit() #Aqui se suben los datos dados
    nav.select_form(nr=0)

    nav['id']= "'" #La comilla en este caso mandaba un error de tipo sql, nosotros buscamos detectar ese error e imprimirlo en pantalla

    nav.submit()
    soup = BeautifulSoup(nav.response().read(),'html5lib')
    print(soup.pre.string) #Declaramos que la etiqueta a borrar será pre, y el tipo de contenigo que se encuentra en ella que en este caso es una string

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
