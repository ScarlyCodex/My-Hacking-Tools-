#! /usr/bin/env python3
#_*_ coding: utf8_*_

import shutil
import sys

def main():
    if len(sys.argv) == 2:
        for n in range(0, int(sys.argv[1])):
            shutil.copy(sys.argv[0],sys.argv[0] + str(n)+'.py') #shutil ayuda a interactuar con el sistema de una forma mas compleja y rapida

    else:
        print('Argumentos necesarios')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
