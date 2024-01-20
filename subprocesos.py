#! /usr/bin/env python3
#_*_ coding:utf8_*_

import os
import subprocess

a = open(os.devnull,'w')
p = subprocess.call(['ping','c','2','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT)
if p == 1:
    print('El comando se ejecutó correctamente')
else:
    print('El comando no se ha ejecutado correctamente')
