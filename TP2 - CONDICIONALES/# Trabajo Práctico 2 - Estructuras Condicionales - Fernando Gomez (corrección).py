# Trabajo Práctico 2 - Estructuras Condicionales (Corrección)

#1) Solicitar edad y evaluar si es mayor de edad

edad = int(input("Por favor ingrese su edad a continuación: "))

if edad >= 18:
    print("Es mayor de edad")

#2) Condición de aprobado o desaprobado

calificacion = int(input("Ingrese su calificación para determinar si esta aprobado o no: "))
if calificacion < 6:
    print ("Usted está desaprobado")
else:
    print ("Usted está aprobado, felicitaciones!")

#3) Ingreso de solo numeros pares

num_par = int(input("Ingrese un numero par: "))
if num_par % 2 == 0:
    print ("Usted ingreso un numero par")
else:
    print ("Usted ingreso un numero invalido!") 

#4) Categoría por edad: Niño, Adolescente o Adulto

categoria_edad = int(input("Ingrese su edad para determinar su categoría: "))
if categoria_edad < 12:
    print("Su categoría es Niño")
elif categoria_edad < 18:
    print("Su categoría es Adolescente")
elif categoria_edad < 30:
    print("Su categoría es Adulto Joven")
else:
    print("Su categoría es Adulto")

#5) Contraseña entre 8 y 14 caracteres 

contraseña = (input("Ingrese una contraseña entre 8 a 14 caracteres: "))
if len(contraseña) >= 8 <= 14:
    print ("La contraseña cumple con los requisitos: ", contraseña)
else:
    print ("La contraseña no cumple con los requisitos!")

#6) Consumo mensual de energía

consumo_electrico = int(input("Ingrese su consumo mensual de energía electrica en kilovatios (kWh): "))
if consumo_electrico < 150:
    print ("Consumo eléctrico bajo")
elif consumo_electrico >= 150 and consumo_electrico <= 300:
    print ("Consumo eléctrico medio")
elif consumo_electrico > 300:
    print ("Consumo eléctrico alto")
    if consumo_electrico >= 500:
        print ("Considere medidas de ahorro energético")

#7) Frase o palabra terminada en vocal mas signo de exclamación (!)

frase = input("Ingresá una frase o palabra: ")

vocales = "aeiouAEIOU"

if frase[-1] in vocales:
    print(frase + "!")
else:
    print(frase)

#8) Número y opcion 1, 2 o 3 para MAYÚSCULAS, minúsculas o Primera Letra Mayúscula

nombre = input("Ingresá tu nombre: ")
print("¿Qué querés hacer con tu nombre?")
print("1. Mayúsculas (PEDRO)")
print("2. Minúsculas (pedro)")
print("3. Primera letra mayúscula (Pedro)")

opcion = input("Elegí una opción (1, 2 o 3): ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida.")

#9) Clasificación de magnitud de terremoto en categorías

magnitud = float(input("Ingresá la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#10) Determinar estación del año mas el hemisferio para imprimir en pantalla si se encuentre en otoño, invierno, primavera o verano

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

# Determinar la estación según el hemisferio norte
if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
else:
    estacion_norte = "Otoño"

# En el hemisferio sur las estaciones son opuestas
if hemisferio == "N":
    estacion = estacion_norte
elif hemisferio == "S":
    opuestas = {
        "Invierno": "Verano",
        "Verano": "Invierno",
        "Primavera": "Otoño",
        "Otoño": "Primavera"
    }
    estacion = opuestas[estacion_norte]
else:
    print("Hemisferio inválido.")
    exit()

print(f"Estás en: {estacion}")