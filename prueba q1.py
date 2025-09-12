# Prueba 1
# Programación en Python
# Description: Prueba inicial
#
# Author: Javier Rodriguez <javier@javierdz.me>

import signal
from colorama import Fore

# Handler para cuando le das Ctrl+C 
def sig_handler(signal, frame):
    print(Fore.RED + "[!]" + Fore.RESET + " Saliendo...")
    exit(0)

signal.signal(signal.SIGINT, sig_handler)

print("hola clase")
