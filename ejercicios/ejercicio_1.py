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
    #     1. Declara una variable entera con valor 10 y muéstrala por pantalla.
    entero = 10
    print(entero)

    # 2. Declara una variable decimal con valor 5.5 y muéstrala.
    decimal = 5.5
    print(decimal)

    # 3. Declara dos variables enteras y súmalas, guarda el resultado en otra variable y muéstralo.
    entero2 = 20
    suma = entero + entero2
    print(suma)

    # 4. Declara dos variables decimales y réstalas, muestra el resultado.
    decimal2 = 10.5
    resta = decimal - decimal2
    print(resta)

    # 5. Convierte un número entero en decimal y muéstralo.
    entero_decimal = float(entero)
    print(entero_decimal)

    # 6. Convierte un número decimal en entero y muéstralo.
    decimal_entero = int(decimal)
    print(decimal_entero)

    # 7. Declara un entero y un decimal, súmalos y muestra el resultado.
    entero3 = 30
    suma2 = entero3 + decimal
    print(suma2)

    # 8. Resta un decimal a un entero y muestra el resultado.
    resta2 = entero3 - decimal2
    print(resta2)

    # 9. Guarda el resultado de 15 + 4.7 en una variable y muéstrala.
    resultado = 15 + 4.7
    print(resultado)
    # 10. Declara tres enteros y muestra su suma total.
    entero4 = 5
    entero5 = 10
    entero6 = 15
    suma_total = entero4 + entero5 + entero6
    print(suma_total)

    # 11. Declara tres decimales y muestra su resta total.
    decimal3 = 1.5
    decimal4 = 2.5
    decimal5 = 3.5
    resta_total = decimal3 - decimal4 - decimal5
    print(resta_total)

    # 12. Convierte el entero 25 en decimal, súmalo a 2.5 y muestra el resultado.
    entero7 = 25
    resultado2 = float(entero7) + 2.5
    print(resultado2)

    # 13. Convierte el decimal 7.9 en entero, réstalo a 20 y muestra el resultado.
    decimal6 = 7.9
    resultado3 = 20 - int(decimal6)
    print(resultado3)

    # 14. Declara dos enteros, convierte uno a decimal y súmalos.
    entero8 = 12
    entero9 = 8
    resultado4 = float(entero8) + entero9
    print(resultado4)

    # 15. Declara dos decimales, convierte uno a entero y réstalos.
    decimal7 = 5.5
    decimal8 = 2.2
    resultado5 = int(decimal7) - decimal8
    print(resultado5)

    # 16. Suma 10, 2.5 y el entero convertido de 3.8 y muestra el resultado.
    resultado6 = 10 + 2.5 + int(3.8)
    print(resultado6)

    # 17. Resta 50 con el decimal convertido de 12 y muestra el resultado.
    resultado7 = 50 - float(12)
    print(resultado7)

    # 18. Guarda en una variable el resultado de convertir 9.99 en entero y súmalo con 1.
    resultado8 = int(9.99) + 1
    print(resultado8)
    # 19. Multiplica un entero por un decimal y muestra el resultado.
    resultado9 = 5 * 2.5
    print(resultado9)
    # 20. Divide un entero por un decimal y guarda el resultado en otra variable, luego muéstralo.
    resultado10 = 10 / 2.5
    print(resultado10)

if __name__ == "__main__":
    ejercicios()