import requests
import argparse
from os import path
 
 
parser = argparse.ArgumentParser(description="Post Web")
parser.add_argument('-f','--file',help="Indica el archivo a subir")
parser = parser.parse_args()
URL = 'https://curso--python-0-prueba-pentest.000webhostapp.com'
 
 
def main():
    if parser.file:
        if path.exists(parser.file):
            archivo = open(parser.file,'rb')
            headers = {'Users-Agent':'Firefox'}
            peticion = requests.post(url=URL,files={'uploaded_file':archivo},headers=headers)
            print(parser.file[2:]) # compruebo el nombre
            # if peticion.status_code == 200:
            if(parser.file[2:] in peticion.text): #corregido
                print(peticion.text)
                print("Archivo subido con éxito")
            else:
                print("Fallo la subida")
        else:
            print("No existe el archivo")
    else:
        print("Necesito un archivo para subir")
 
if __name__=='__main__':
    main()