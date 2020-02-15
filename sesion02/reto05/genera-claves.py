""" Generador de claves """
import random

numero_de_claves = input('Número de claves a generar: ')
longitud = input('Longitud de claves a generar: ')

if not numero_de_claves.isdigit() and not longitud.is_digit():
    print("Entrada no valida")
else:
    numero_de_claves = int(numero_de_claves)
    longitud = int(longitud)

if longitud <= 3:
    print('La longitud mínima es de 3 caractéres')
    quit()

lowercase_letters = 'qwertyuiopasdfghjklzxcvbnm'
uppercase_letters = lowercase_letters.upper()
digits = '1234567890'
all_elements = lowercase_letters +  uppercase_letters +  digits

for n in range(numero_de_claves):
    lower = random.choice(list(lowercase_letters))
    upper = random.choice(list(uppercase_letters))
    digit = random.choice(list(digits))

    clave = [lower, upper, digit]

    for i in range(longitud - 3):
        clave.append(
            random.choice(list(all_elements))
        )
    random.shuffle(clave)
    print("".join(clave))

