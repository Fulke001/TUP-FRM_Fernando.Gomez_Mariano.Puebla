# Ejercicio N°1 (Hola Mundo!)

print ("Hola mundo!")

# Ejercicio N°2 ("Hola X ")

nombre = input ("Ingrese a continuación su nombre: ")
print (f"Hola {nombre}!")

# Ejercicio N°3 (Nombre, Apellido, Edad, Lugar)


nombre1 = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
lugar = input ("Ingrese su lugar de residencia: ")

print (f"Soy {nombre1} {apellido}, tengo {edad} y vivo en {lugar}")

# Ejercicio N°4 (Area y perimetro de un círculo)

radio = float(input("ingrese el radio del círculo: "))

area = 3.1416 * radio**2
perimetro = 2 * 3.1416 * radio

print(f"El área del circulo es: {area} y su perímetro es: {perimetro}")

# Ejercicio N°5 (Equivalentes de Segundos a Horas)

segundos = int(input("Ingrese una cantidad de segundos: "))

horas = segundos / 3600 # 1 Hora = 3600 segundos

print(f"{segundos} segundos equivalen a {horas}.")


# Ejercicio N°6 (Tabla de Multiplicar)

numero = int(input("ingrese un número: "))
print(f"Tabla de multiplicar del {numero}")

print(f"{numero} * 0 = {numero * 0}")
print(f"{numero} * 1 = {numero * 1}")
print(f"{numero} * 2 = {numero * 2}")
print(f"{numero} * 3 = {numero * 3}")
print(f"{numero} * 4 = {numero * 4}")
print(f"{numero} * 5 = {numero * 5}")
print(f"{numero} * 6 = {numero * 6}")
print(f"{numero} * 7 = {numero * 7}")
print(f"{numero} * 8 = {numero * 8}")
print(f"{numero} * 9 = {numero * 9}")
print(f"{numero} * 10 = {numero * 10}")

# Ejercicio N°7 (Operaciones Aritméticas)

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

print(f"Operaciones aritméticas entre {numero_1} y {numero_2}")

print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")
print(f"{numero_1} // {numero_2} = {numero_1 // numero_2}")
print(f"{numero_1} ** {numero_2} = {numero_1 ** numero_2}")

# Ejercicio N°8 (IMC)

peso = float(input("Ingrese a continuación su peso en kilogramos: "))
altura = float(input("Ingrese a continuación su altura en metros: "))

imc = peso / (altura ** 2)

print (f"Su IMC es: {imc}")

# Ejercicio N°9 ()

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius * 9/5 + 32

print(f"{celsius}°C equivalen a {fahrenheit}°F")

# Ejercicio N°10 (Promedio entre 3 números)

num1 = float(input("ingrese el primer número: "))
num2 = float(input("ingrese el segundo número: "))
num3 = float(input("ingrese el tercer número: "))

promedio = (num1 + num2 + num3) / 3

print("El promedio de los tres números es:", promedio)

#Saludos!!!