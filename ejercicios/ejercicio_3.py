'''
* ejercicio_3.py
* Programación en Python
* Description: If - Else exercises (and a try-except-finally clause, and some requests)
* Created by Javier Rodriguez on 8-10-2025

'''


import os
import requests
import json
from colorama import Fore


try:
    r = requests.get("https://javierdz.dev/api/ping")
    data = json.loads(r.text)
    if r.status_code == 200:
        print(Fore.GREEN + "EXITO")
        print(f"en {r.url}, con status_code {r.status_code} y respuesta PONG {data['pong']}")
    else:
        print("algo ha pasado que no ha funcionado")
except Exception as e:
    print("Algo ha pasado...", Fore.RED, e, Fore.RESET)
finally:
    print(Fore.RESET, "Runtime ended")

