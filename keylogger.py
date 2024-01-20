#! /usr/bin/env python3
# _*_ coding: utf8_*_

import pynput.keyboard  # modulo pynput y clase keyboard

def presiona(key):  # Funcion para tecla presionada
    key1 = convertir(key)
    print('Tecla presionada: {}'.format(key1))


def libera(key):  # Funcion para cuando el usuario deja de presionar la tecla
    key1 = convertir(key)
    print('Tecla liberada: {}'.format(key1))

    if str(key) == 'Key.esc':
        print('Salida por comando de teclado ejecutada')
        return False


def convertir(key):  # Funcion para convertir los caracteres que se pasen a traves del argumento key en string --caracteres tipo unicode
    if isinstance(key, pynput.keyboard.KeyCode): #Si la variable key es de tipo pynput.keyboard.KeyCode, entonces retorna un carácter
        return key.char #No es necesario usar la funcion string ya que key es una subclase de KeyCode y por lo tanto posee unos metodos de la misma por lo que solo con char returna el valor deseado 
    else:
        return str(key)

with pynput.keyboard.Listener(on_press=presiona, on_release=libera) as listen:  # Este modulo es key sensitive, distingue entre mayusculas y minusculas
    listen.join()  # Se pone a la escucha con la funcion join que es propia del modulo pynput
