import os
from colorama import Fore
import signal


def handler(sig, frame):
    try:
        print(Fore.RED + "\n[!] Saliendo...\n")
        os._exit(1)
    except Exception as e:
        print(Fore.RED + "\n[!] Saliendo...\n")
        print(e)

signal.signal(signal.SIGINT, handler)

# print("esta \" palabra \" se encuentra \n escrita entre comillas dobles")
# print("salto de linea \t otra linea")
# print(' ' ' Una linea con espacios al inicio y al final ' ' ')
# print("""
#       una liena
#       con salto de linea
#       y espacios al inicio
#       """)


print("aaaaaaaaaaaaaaa \rhola")
n1=3
n2=5
print(f"la suma de {n1} + {n2} es igual a", float(n1+n2))
n3 = 2.6843252
print(f"el numero {n3} redondeado a 2 decimales es {n3:.2f}")


# Entrada de valores por teclado

a = input("ingresa un valor: ")
try:
    print(f"el valor ingresado es: {a} y su tipo es {type(a).__name__} y si sumamos 3 es igual a {int(a)+3}")
except  ValueError as e:
    print(f"el valor ingresado es: {a} y su tipo es {type(a).__name__} y no se puede sumar 3 por " + Fore.RED + f"{e}")


while(1):
    print("hola")