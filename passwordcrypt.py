#! /usr/bin/env python3
#_*_ coding: utf8_*_

import hashlib
import time
import sys

def main():
    password = str(input("Palabra --> "))
    md5pass = hashlib.md5(password.encode('UTF-8')).hexdigest()
    md5 = 'MD5: ' + md5pass
    for x in md5:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.02)

    sha1pass = hashlib.sha1(password.encode('utf8')).hexdigest()
    sha1 = '\nSHA1: ' + sha1pass
    for x in sha1:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.02)

    sha224pass = hashlib.sha224(password.encode('utf8')).hexdigest()
    sha224 = '\nSHA224: ' + sha224pass
    for x in sha224:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.02)

    sha256pass = hashlib.sha256(password.encode('utf8')).hexdigest()
    sha256 = '\nSHA256: ' + sha256pass
    for x in sha256:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.02)

    sha384pass = hashlib.sha384(password.encode('utf8')).hexdigest()
    sha384 = '\nSHA384: ' + sha384pass
    for x in sha384:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.01)

    sha512pass = hashlib.sha512(password.encode('utf8')).hexdigest()
    sha512 = '\nSHA512: ' + sha512pass
    for x in sha512:
        print(x, end="")
        sys.stdout.flush()
        time.sleep(0.01)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nSalida manual ejecutada')
        exit()
