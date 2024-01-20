#! /usr/bin/env python3
#__ coding: utf8__

from scapy.all import *
import sys
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target')
parser.add_argument('-s', '--source', help="-t para setear el objetivo y -s para setear la fuente del paquete")
parser = parser.parse_args()

def main():
    if parser.target:
        if parser.source:
            requests = IP(dst=parser.target, src=parser.source) # NOTE: Mandar un msj a traves de TCP a neustra maquina en windows en la capa IP
            # NOTE: IP tambien puede recibir como parametro la source del paquete (de donde viene ese paquete)
            #Lo cual es interesante ya que puedes falsificar la direccion ip proveniente como por Google, Facebook, etc
            tcp_layer = TCP() # NOTE: En el parametro se puede establecer un puerto en específico, normalmente se evita ya que puede que la maquina no responda
            msg = Raw("Este es un mensaje oculto en el paquete") # NOTE: La capa Raw permite incluir mensajes en una capa de un paquete
            final_packet = [requests/tcp_layer/msg for x in range(0, 1000)] ## NOTE: Para construir un paquete se usa el simbolo de division
            send(final_packet, verbose=False) # NOTE: Verbose unicamente sirve para ver el proceso en pantalla
            print()
            for i in tqdm(range(10)): 
                time.sleep(0.2)
            print('\n <-- Mensajes enviados -->\n')
        else:
            print("--> ",end="")
            for ret in 'IP fuente seleccionada por default\n':
                print(ret, end="")
                sys.stdout.flush()
                time.sleep(0.1)

            requests = IP(dst=parser.target)
            tcp_layer = TCP()
            msg = Raw("Este es un mensaje oculto en el paquete")
            final_packet = [requests/tcp_layer/msg for x in range(0, 1000)]
            send(final_packet, verbose=False)

            for i in tqdm(range(10)): 
                time.sleep(0.2)
            time.sleep(1)
            print('\n <-- Mensajes enviados -->\n')
            
    else:
        print('--> Setea el objetivo')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)


