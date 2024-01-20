#! /usr/bin/env python3
#_*_coding: utf8_*_

import nmap

def main():
    scaner = nmap.PortScanner()
    ip = input("IP : ")
    scaner.scan(hosts=ip,arguments="--top-ports 1000 -sV --version-intensity 3")
    print('Comando ejecutado: {}'.format(scaner.command_line())) #comand_line devuelve en pantalla el comando que se ejecutó
    #print(scaner.scaninfo()) mostrar informacion del scaneo

    print('Protocolos utilizados: {}'.format(scaner[ip].all_protocols)) #Acceso a todos los protocolos utilizados, cada informacion de cada maquina escaneada se guarda en una key la cual correspodne a la direccion ip
    print('Estado de la maquina: {}'.format(scaner[ip].state)) #Comprobar el estado de la maquina, (apaga, encendida, etc)
    #print(scaner[ip]['tcp'])

    for puerto in scaner[ip]['tcp'].keys(): #funcion keys() es para acceder a las llaves de cualquier diccionario, se usa mucho en diccionarios anidados
        for data in scaner[ip]['tcp'][puerto]:
            print(data + " : " + scaner[ip]['tcp'][puerto][data])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
