# actividad1.py
# Modulo Profesinal Optativo: Programación en Pyhton
# 
# Creado por Javier Rodriguez el 24/09/2025



# 1.	Declara una variable entera con valor 10 y muÃ©strala por pantalla.

# 2.	Declara una variable decimal con valor 5.5 y muÃ©strala.

# 3.	Declara dos variables enteras y sÃºmalas, guarda el resultado en otra variable y muÃ©stralo.

# 4.	Declara dos variables decimales y rÃ©stalas, muestra el resultado.

# 5.	Convierte un nÃºmero entero en decimal y muÃ©stralo.

# 6.	Convierte un nÃºmero decimal en entero y muÃ©stralo.

# 7.	Declara un entero y un decimal, sÃºmalos y muestra el resultado.

# 8.	Resta un decimal a un entero y muestra el resultado.

# 9.	Guarda el resultado de 15 + 4.7 en una variable y muÃ©strala.

# 10.	Declara tres enteros y muestra su suma total.

# 11.	Declara tres decimales y muestra su resta total.

# 12.	Convierte el entero 25 en decimal, sÃºmalo a 2.5 y muestra el resultado.

# 13.	Convierte el decimal 7.9 en entero, rÃ©stalo a 20 y muestra el resultado.

# 14.	Declara dos enteros, convierte uno a decimal y sÃºmalos.

# 15.	Declara dos decimales, convierte uno a entero y rÃ©stalos.

# 16.	Suma 10, 2.5 y el entero convertido de 3.8 y muestra el resultado.

# 17.	Resta 50 con el decimal convertido de 12 y muestra el resultado.

# 18.	Guarda en una variable el resultado de convertir 9.99 en entero y sÃºmalo con 1.

# 19.	Multiplica un entero por un decimal y muestra el resultado.

# 20.	Divide un entero por un decimal y guarda el resultado en otra variable, luego muÃ©stralo.

# Primer ejercicio
variable1 = 10
print(variable1)

# Segundo ejercicio
variable2 = 5.5
print(variable2)

# Tercer ejercicio
varA = 3
varB = 7
suma = varA + varB
print(suma)

# Cuarto ejercicio
decA = 8.5
decB = 2.3
resta = decA - decB
print(resta)

# Quinto ejercicio
entero = 15
decimal_from_int = float(entero)
print(decimal_from_int)

# Sexto ejercicio
decimal = 9.8
int_from_decimal = int(decimal)
print(int_from_decimal)

# Septimo ejercicio
entero2 = 4
decimal2 = 6.2
suma2 = entero2 + decimal2
print(suma2)


# Octavo ejercicio
entero3 = 10
decimal3 = 3.5
resta2 = entero3 - decimal3
print(resta2)

# Noveno ejercicio
resultado = 15 + 4.7
print(resultado)

# Decimo ejercicio
ent1 = 1
ent2 = 2
ent3 = 3
suma_total = ent1 + ent2 + ent3
print(suma_total)

# Undecimo ejercicio
dec1 = 10.5
dec2 = 4.2
dec3 = 1.3
resta_total = dec1 - dec2 - dec3
print(resta_total)

# Duodecimo ejercicio
ent4 = 25
dec4 = 2.5
suma3 = float(ent4) + dec4
print(suma3)

# Decimotercer ejercicio
dec5 = 7.9
ent5 = 20
resta3 = ent5 - int(dec5)
print(resta3)

# Decimocuarto ejercicio
ent6 = 5
ent7 = 10
suma4 = float(ent6) + ent7
print(suma4)

# Decimoquinto ejercicio
dec6 = 8.4
dec7 = 3.2
resta4 = dec6 - int(dec7)
print(resta4)

# Decimosexto ejercicio
suma5 = 10 + 2.5 + int(3.8)
print(suma5)

# Decimoséptimo ejercicio
resta5 = 50 - float(12)
print(resta5)

# Decimoctavo ejercicio
var_result = int(9.99) + 1
print(var_result)

# Decimonoveno ejercicio
ent8 = 4
dec8 = 2.5
multiplicacion = ent8 * dec8
print(multiplicacion)

# Vigésimo ejercicio
ent9 = 10
dec9 = 2.0
division = ent9 / dec9
print(division)
print(type(division)) # Si sale float esta bien, sino la jodimos