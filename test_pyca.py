#! /usr/bin/env python3
# _*_coding: utf8_*_

from cryptography.fernet import Fernet
import time


def main():
    # Pon esto en un lugar seguro

    key = Fernet.generate_key()
    f = Fernet(key)

    token = f.encrypt(b'PAPAS FRITAS')
    print(token)

    opcion = str(input("¿Quieres desencriptar el mensaje? > S/n : "))

    if opcion == 'S':
        print(f.decrypt(token))
    else:
        print('Ojos que no ven... ')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
