import os
import signal
from colorama import Fore

def handler(sig, frame):
    try:
        print(Fore.RED + "\n[!] Saliendo...\n")
        os._exit(1)
    except Exception as e:
        print(Fore.RED + "\n[!] Saliendo...\n")
        print(e)

signal.signal(signal.SIGINT, handler)

def ejercicios():
    print("comillas dobles")
    print('comillas simples')

    """ Comentario
    de varias
    lineas"""
    print("hola")
    
    print("esto es una linea \n esta es otra \n y esta es otra")
    
    print("Te llamas javier y tienes \t 20 años")
    
    edad = 16
    nombre = "Javier"
    print(f"me llamo {nombre} y tengo {edad} años")
    
    n1 = 2
    n2 = 6
    print(f"El resultado de la multiplicacion de {n1} * {n2} es igual a {n1*n2}")

    print("\thola\n\tmundo")
    print("""
          hola
          mundo
          """)
    
    """ No se este es un comentario de varias
    lineas"""
    print(f"hola como \nestas ")



if __name__ == "__main__":
    ejercicios()