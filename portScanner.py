import pyfiglet
import sys
import socket
import colorama
from colorama import Fore, Back, Style, init
init()
from datetime import datetime

ascci_banner = pyfiglet.figlet_format("VICKY CODEX")
print(Fore.RED + ascci_banner + Fore.BLUE)

#DEFINIR EL OBJETIVO
if len(sys.argv) == 2:

    #TRADUCIR HOSTNAME A IPV4
    objetivo = socket.gethostbyname(sys.argv[1])

else: 
    print("Cantidad inválida de argumentos")

#AÑADIR BANNER
print("-" * 50)
print("Escaneando objetivo: " + objetivo)
print('Escaneo empezado en: '+str(datetime.now()))
print("-" * 50)

try:
    #Escanear todos los puertos desde 1 - 65,535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        #Retornar un indicador de error
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print(f'Puerto -> {port} está abierto')
            s.close()


except KeyboardInterrupt:
    print('\n Saliendo del programa')
    sys.exit()

except socket.gaierror:
    print('\nEl Hostname no pudo ser resuelto')

except socket.error:
    print('\nEl servidor no está respondiendo')
    sys.exit()
