# Prueba 1
# Programación en Python
# Description: Prueba inicial
#
# Author: Javier Rodriguez <javier@javierdz.me>
# Created: 2024-10-01
import signal
from colorama import Fore

# Handler para cuando le das Ctrl+C 
def sig_handler(signal, frame):
    print(Fore.RED + "\n[!]" + Fore.RESET + " Saliendo...")
    exit(0)

signal.signal(signal.SIGINT, sig_handler)
# Costumbre
def main():
    a = None
# lo que hacemos en clase
def pruebas():
    cadenaTexto = None
    cadenaTexto = input("Dime tu nombre: ")
    numeroEntero = None
    numeroEntero = 42
    numeroDecimal = None
    numeroDecimal = 3.14
    print(cadenaTexto)
    print(cadenaTexto, numeroEntero)
    print("me llamo " + cadenaTexto)
    print(4+3+2)
    try:
        print(numeroEntero + int(cadenaTexto))
    except ValueError as e:
        print("No se puede convertir a entero", e)
    number_as_text = "5"
    try:
        print(1!=1)
    except Exception as e:
        print("Error inesperado", e)
    
    print(1>1)

if __name__ == "__main__":
    main()
    pruebas()