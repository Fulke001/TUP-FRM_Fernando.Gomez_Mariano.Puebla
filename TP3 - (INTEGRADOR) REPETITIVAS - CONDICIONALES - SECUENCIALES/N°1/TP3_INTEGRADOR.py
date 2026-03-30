#trabajo Integrador repetitivas/condicionales/secuenciales Fernando Gomez

#Ejercicio Nº1) Caja de kiosco + validaciones

#Ingreso de nombre del cliente

nombre_cliente = input ("Ingrese su nombre en el sistema de compra: ")
while nombre_cliente == "" or not nombre_cliente.isalpha():
    print ("Nombre inválido")
    nombre_cliente = input("Ingrese su nombre nuevamente: ")
print ("Bienvenido", nombre_cliente,"!")

#Ingreso de cantidad de productos

cantidad_productos = (input("Ingrese la cantidad de productos: "))
while cantidad_productos == "" or not cantidad_productos.isdigit() or int(cantidad_productos) == 0:
    print ("Cantidad de productos inválida")
    cantidad_productos = (input("Ingrese nuevamente la cantidad de productos: "))
cantidad_productos = int(cantidad_productos)

total_sin_descuento = 0
total_con_descuento = 0

for i in range (1, cantidad_productos + 1):
    precio = (input("Ingrese el precio de los productos: "))
    while precio == "" or not precio.isdigit() or int(precio) == 0:
        print ("Precio inválido")
        precio = (input("Ingrese nuevamente el precio de los productos"))
    precio = int(precio)
    descuento = input("El producto tiene deescuento? (S/N) ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print ("Opción inválida")
        descuento = input ("Ingrese nuevamente S/N: ")
    total_sin_descuento = total_sin_descuento + precio
    if descuento.lower() == "s":
        precio = precio - precio * 0.10
    total_con_descuento = total_con_descuento + precio

print (f"Total sin descuentos: ${total_sin_descuento}")
print (f"Total con descuentos: ${total_con_descuento:.2f}")
print (f"Ahorro: ${total_sin_descuento - total_con_descuento:.2f}")
print (f"Promedio por producto: ${total_con_descuento / cantidad_productos:.2f}")

# Ejercicio N°2) — Acceso al Campus y Menú Seguro


usuario_correcto   = "alumno"
contraseña_correcta = "python123"

for i in range(1, 4):
    print(f"Ingrese el usuario: Intento {i}/3")
    usuario    = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        print("Bienvenido al campus")
        while True:
            print("1) Estado")
            print("2) Cambiar clave")
            print("3) Mensaje")
            print("4) Salir")
            opcion = input("Opción: ")
            if not opcion.isdigit():
                print("Error: ingrese un número válido")
            elif int(opcion) < 1 or int(opcion) > 4:
                print("Error: opción fuera de rango")
            elif int(opcion) == 4:
                print("Cerrando sesión... ¡Hasta pronto!")
                break
            elif int(opcion) == 1:
                print("Inscripto")
            elif int(opcion) == 2:
                nueva_clave = input("Ingrese la nueva clave, la misma debe ser de mínimo 6 caracteres: ")
                if len(nueva_clave) < 6:
                    print("Error: Mínimo de 6 caracteres")
                else:
                    confirmacion = input("Confirma la clave: ")
                    if nueva_clave == confirmacion:
                        contraseña_correcta = nueva_clave
                        print("Contraseña cambiada con éxito")
                    else:
                        print("Error: las claves no coinciden")
            elif int(opcion) == 3:
                print("¡Metele que son pasteles!")
        break  # salió del menú → no seguir el for
    else:
        print("Error: credenciales inválidas")

# Ejercicio N°3) - Agenda de Turnos con nombres (sin listas)

#Turnos

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

nombre_operador = input("Ingrese el nombre del operador: ")
while nombre_operador == "" or not nombre_operador.isalpha():
    print ("Nombre inválido")
    nombre_operador = input ("Ingrese el nombre nuevamente: ")

while True:
    print ("Opción 1: Reservar turno ")
    print ("Opción 2: Cancelar turno (Por nombre de paciente)")  
    print ("Opción 3: Ver agenda del día")   
    print ("Opción 4: Ver resumen general")
    print ("Opción 5: Cerrar sistema")
    print ("")
    opcion = input ("Opción: ")
    if not opcion.isdigit():
        print ("Error: ingrese un numero válido")
    elif int (opcion) < 1 or int(opcion) > 5:
        print ("Error: opción fiera de rango, por favor seleccione nuevamente: " )
    elif int(opcion) == 5:
        break
    elif int(opcion) == 1:
        dia_turno = input ("Ingrese el dia que desea tener el turno: Lunes (1) - Martes (2): ")
        while not dia_turno.isdigit() or int (dia_turno) < 1 or int(dia_turno) >2:
            print ("Día inválido")
            dia_turno = input ("Ingrese el día nuevamente: ")
        dia_turno = int(dia_turno)

        nombre_paciente = input ("Ingrese el nombre del paciente: ")
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print ("Nombre de paciente inválido")
            nombre_paciente = input ("Ingrese nuevamente el nombre del paciente: ")

        if dia_turno == 1:
            if lunes1 == "":
                lunes1 = nombre_paciente
        elif lunes2 == "":
                lunes2 = nombre_paciente
        elif lunes3 == "":
                lunes3 = nombre_paciente
        elif lunes4 == "":
                lunes4 = nombre_paciente
        else:
                print("No hay turnos disponibles para el día Lunes")
    
        if dia_turno == 2:
            if martes1 == "":
                martes1 = nombre_paciente
        elif martes2 == "":
                martes2 = nombre_paciente
        elif martes3 == "":
                martes3 = nombre_paciente
        else:
                print("No hay turnos disponibles para el día Martes")
    elif int(opcion) == 2:
        dia_turno = input ("Ingrese el día del turno a cancelar: Lunes (1) - Martes (2): ")
        while not dia_turno.isdigit() or int (dia_turno) < 1 or int(dia_turno) > 2:
            print ("Día inválido")
            dia_turno = input ("Ingrese el día nuevamente: ")
        dia_turno = int(dia_turno)

        nombre_paciente = input ("Ingrese el nombre del paciente a cancelar: ")
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print ("Nombre de paciente inválido")
            nombre_paciente = input ("Ingrese nuevamente el nombre del paciente: ")

        if dia_turno == 1:
            if nombre_paciente == lunes1:
                lunes1 = ""
                print ("Turno cancelado correctamente")
            elif nombre_paciente == lunes2:
                lunes2 = ""
                print ("Turno cancelado correctamente")
            elif nombre_paciente == lunes3:
                lunes3 = ""
                print ("Turno cancelado correctamente")
            elif nombre_paciente == lunes4:
                lunes4 = ""
                print ("Turno cancelado correctamente")
            else:
                print ("No se encontró el paciente en el día Lunes")
        elif dia_turno == 2:
            if nombre_paciente == martes1:
                martes1 = ""
                print ("Turno cancelado correctamente")
            elif nombre_paciente == martes2:
                martes2 = ""
                print ("Turno cancelado correctamente")
            elif nombre_paciente == martes3:
                martes3 = ""
                print ("Turno cancelado correctamente")
            else:
                print ("No se encontró el paciente en el día Martes")

    elif int(opcion) == 3:
        dia_turno = input ("Ingrese el día a consultar: Lunes (1) - Martes (2): ")
        while not dia_turno.isdigit() or int (dia_turno) < 1 or int(dia_turno) > 2:
            print ("Día inválido")
            dia_turno = input ("Ingrese el día nuevamente: ")
        dia_turno = int(dia_turno)

        if dia_turno == 1:
            print ("Agenda del día Lunes:")
            if lunes1 == "":
                print ("Turno 1: (libre)")
            else:
                print ("Turno 1: " + lunes1)
            if lunes2 == "":
                print ("Turno 2: (libre)")
            else:
                print ("Turno 2: " + lunes2)
            if lunes3 == "":
                print ("Turno 3: (libre)")
            else:
                print ("Turno 3: " + lunes3)
            if lunes4 == "":
                print ("Turno 4: (libre)")
            else:
                print ("Turno 4: " + lunes4)
        elif dia_turno == 2:
            print ("Agenda del día Martes:")
            if martes1 == "":
                print ("Turno 1: (libre)")
            else:
                print ("Turno 1: " + martes1)
            if martes2 == "":
                print ("Turno 2: (libre)")
            else:
                print ("Turno 2: " + martes2)
            if martes3 == "":
                print ("Turno 3: (libre)")
            else:
                print ("Turno 3: " + martes3)

    elif int(opcion) == 4:
        ocupados_lunes = 0
        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1
        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1

        ocupados_martes = 0
        if martes1 != "":
            ocupados_martes = ocupados_martes + 1
        if martes2 != "":
            ocupados_martes = ocupados_martes + 1
        if martes3 != "":
            ocupados_martes = ocupados_martes + 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print ("Resumen general:")
        print ("Lunes - Ocupados: " + str(ocupados_lunes) + " | Disponibles: " + str(disponibles_lunes))
        print ("Martes - Ocupados: " + str(ocupados_martes) + " | Disponibles: " + str(disponibles_martes))

        if ocupados_lunes > ocupados_martes:
            print ("El día con más turnos ocupados es: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print ("El día con más turnos ocupados es: Martes")
        else:
            print ("Ambos días tienen la misma cantidad de turnos ocupados")

print ("Sistema cerrado. Hasta luego, " + nombre_operador + "!")

#Ejercicio N°4) - Escape Room

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""


nombre = input("Ingresá tu nombre de agente: ")
while not nombre.isalpha():
    print("Error: el nombre solo puede contener letras, sin espacios ni números.")
    nombre = input("Ingresá tu nombre de agente: ")

print(f"\n¡Bienvenido/a, agente {nombre}! Tenés {energia} de energía y {tiempo} minutos.")
print("Objetivo: abrir las 3 cerraduras antes de quedarte sin recursos.\n")

racha_forzar = 0  # contador de veces seguidas que se eligió opción 1

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):


    print("=" * 45)
    print(f"  Agente : {nombre}")
    print(f"  Energía: {energia}   |   Tiempo: {tiempo}   |   Cerraduras: {cerraduras_abiertas}/3")
    print(f"  Alarma : {'ACTIVA' if alarma else 'inactiva'}   |   Código parcial: '{codigo_parcial}' (largo: {len(codigo_parcial)})")
    print("=" * 45)
    print("  1. Forzar cerradura  (-20E, -2T)")
    print("  2. Hackear panel     (-10E, -3T)")
    print("  3. Descansar         (+15E, -1T)")
    print("-" * 45)


    opcion = input("Elegí una opción (1/2/3): ")
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Opción inválida. Ingresá 1, 2 o 3.")
        opcion = input("Elegí una opción (1/2/3): ")

    opcion = int(opcion)


    if opcion == 1:
        energia -= 20
        tiempo  -= 2
        if energia < 0:
            energia = 0
        if tiempo < 0:
            tiempo = 0

        # Regla anti-spam: 3 veces seguidas forzando
        if racha_forzar + 1 >= 3:
            racha_forzar = 0
            alarma = True
            print(">>> ¡La cerradura se trabó! Alarma activada automáticamente. NO se abrió la cerradura.")
        else:
            racha_forzar += 1

            # Riesgo de alarma si energía < 40
            if energia < 40:
                print(f"  Energía baja ({energia}). Riesgo de alarma. Elegí un número del 1 al 3:")
                num = input("Número (1/2/3): ")
                while not num.isdigit() or num not in ("1", "2", "3"):
                    print("Número inválido. Ingresá 1, 2 o 3.")
                    num = input("Número (1/2/3): ")

                if int(num) == 3:
                    alarma = True
                    print(">>> Elegiste 3 → ¡ALARMA ACTIVADA!")
                else:
                    cerraduras_abiertas += 1
                    print(f">>> Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}/3")
            else:
                cerraduras_abiertas += 1
                print(f">>> Cerradura forzada con éxito. Cerraduras abiertas: {cerraduras_abiertas}/3")


    elif opcion == 2:
        racha_forzar = 0   # corta la racha
        energia -= 10
        tiempo  -= 3
        if energia < 0:
            energia = 0
        if tiempo < 0:
            tiempo = 0

        print(">>> Hackeando el panel...")
        letras = ["A", "B", "C", "D"]
        mensajes = [
            "Paso 1/4 — Analizando circuitos...",
            "Paso 2/4 — Bypaseando firewall...",
            "Paso 3/4 — Inyectando código...",
            "Paso 4/4 — Acceso completado."
        ]
        for i in range(4):
            codigo_parcial += letras[i]
            print(f"    {mensajes[i]}  [código parcial: '{codigo_parcial}']")

        print(f">>> Hackeo terminado. Código acumulado: '{codigo_parcial}' (largo: {len(codigo_parcial)})")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print(f">>> ¡Código suficiente! Cerradura desbloqueada automáticamente. {cerraduras_abiertas}/3")


    elif opcion == 3:
        racha_forzar = 0   # corta la racha
        tiempo -= 1
        if tiempo < 0:
            tiempo = 0

        if alarma:
            energia += 15 - 10   # ganancia neta: +5
            print(">>> Descansás, pero la alarma activa drena 10 de energía extra. Ganancia neta: +5E, -1T.")
        else:
            energia += 15
            print(">>> Descansás. +15E, -1T.")

        if energia > 100:
            energia = 100

    print()   # línea en blanco entre turnos


print("\n" + "=" * 45)

if cerraduras_abiertas == 3:
    print(f"  *** VICTORIA ***")
    print(f"  ¡Agente {nombre}, abriste la bóveda!")

elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print(f"  *** DERROTA — SISTEMA BLOQUEADO ***")
    print(f"  La alarma activa con {tiempo} min restantes bloqueó la bóveda.")

elif energia <= 0:
    print(f"  *** DERROTA — SIN ENERGÍA ***")
    print(f"  Agente {nombre}, te quedaste sin energía.")

else:   # tiempo <= 0
    print(f"  *** DERROTA — TIEMPO AGOTADO ***")
    print(f"  Agente {nombre}, se acabó el tiempo.")
print(f"\n  Energía final: {energia}   |   Tiempo restante: {tiempo}")
print(f"  Cerraduras abiertas: {cerraduras_abiertas}/3")
print("=" * 45)


#Ejercicio N°5) - Gladiador

print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador: int     = 100
vida_enemigo: int     = 100
pociones: int         = 3
danio_base: int       = 15
danio_enemigo: int    = 12
turno_gladiador: bool = True
juego_activo: bool    = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("  1. Ataque Pesado")
    print("  2. Ráfaga Veloz")
    print("  3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion == 1:
        if vida_enemigo < 20:
            danio_final: float = danio_base * 1.5
            print(f">> ¡GOLPE CRÍTICO! Dañas al enemigo por {danio_final} puntos.")
        else:
            danio_final = float(danio_base)
            print(f">> ¡Atacaste al enemigo por {int(danio_final)} puntos de daño!")
        vida_enemigo -= int(danio_final)

    elif opcion == 2:
        print(">> ¡Iniciás una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("  > Golpe conectado por 5 de daño")

    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones -= 1
            print(f">> Usaste una poción. HP restaurado a {vida_jugador}. Pociones restantes: {pociones}")
        else:
            print(">> ¡No quedan pociones! Perdiste el turno.")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

    turno_gladiador = not turno_gladiador

    if vida_jugador > 0 and vida_enemigo > 0:
        print("\n=== NUEVO TURNO ===")

print("\n" + "=" * 40)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

print(f"HP final: {max(vida_jugador, 0)} | Enemigo: {max(vida_enemigo, 0)} | Pociones: {pociones}")
print("=" * 40)