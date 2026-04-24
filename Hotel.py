import os

# ------------------- LIMPIAR PANTALLA ------------------- #
os.system("clear")

# ------------------- CONFIGURACIÓN INICIAL ------------------- #
recepcionistas = ["juan", "carlos", "alex"]
intentos = 0

# ------------------- MENÚ PRINCIPAL ------------------- #
menu = True
while menu:

    print("Bienvenido al sistema de Hotel.py")

    # -------- VALIDACIÓN DE RECEPCIONISTA -------- #
    nombre_resepcionista = input("Por favor resepcionista ingrese su nombre: ").strip().lower()

    if nombre_resepcionista in resepcionistas:
        print(f"Bienvenido {nombre_resepcionista.title()}")

        # -------- VALIDACIÓN DE PIN -------- #
        pin = True
        while pin:
            print(f"\nPor medidas de seguridad {nombre_resepcionista.title()}, Debes colocar tu PIN de seguridad")

            pin_secreto = input("Ingrese su pin de seguridad: ").strip()

            if pin_secreto == "1234" or pin_secreto == "4321":
                print("Datos validos!")
                print("Entrando al hotel.....")
                pin = False
            else:
                print("Pin invalido!")
                intentos += 1

                # Control de intentos máximos
                if intentos >= 3:
                    raise TypeError("Intentos maximos! saliendo del sistema")

                continue

    else:
        print("\nNombre invalido! intentalo de nuevo\n")
        continue

    # ========================================================== #
    #                REGISTRO DE HUÉSPED                        #
    # ========================================================== #

    print("\n\tBienvenido Al Hotel Py!")

    # -------- NOMBRE DEL CLIENTE -------- #
    nombre = True
    while nombre:
        print("Por favor complete los datos\n")

        nombre_cliente = input("Ingrese su nombre: ").strip()

        if not nombre_cliente.replace(" ", "").isalpha():
            print("Nombre invalido! 𝘵𝘶 𝘯𝘰𝘮𝘣𝘳𝘦 𝘥𝘦𝘣𝘦 𝘵𝘦𝘯𝘦𝘳 𝘴𝘰𝘭𝘢𝘮𝘦𝘯𝘵𝘦 𝘭𝘦𝘵𝘳𝘢𝘴!")
            continue

        nombre = False

    # -------- DNI DEL CLIENTE -------- #
    print(f"Excelente {nombre_cliente.title()} Ahora introduce tu DNI\n")

    dni_validar = True
    while dni_validar:
        dni = input(f"{nombre_cliente.capitalize().split()[0]} Introduce tu dni: ")

        if not dni.isdigit() or len(dni) != 8:
            print("Error: TYPE DNI! 𝘵𝘶 𝘥𝘯𝘪 𝘥𝘦𝘣𝘦 𝘴𝘦𝘳 𝘷𝘢𝘭𝘪𝘥𝘰")
            continue

        dni_validar = False

    # -------- EDAD DEL CLIENTE -------- #
    print(f"\n{nombre_cliente.title()} Ahora indiquenos su edad")

    edad = True
    while edad:
        edad_cliente = input(f"{nombre_cliente.title()} Ingrese su edad: ").strip()

        try:
            edad_cliente = int(edad_cliente)
        except ValueError:
            print("Error: TYPE EDAD: 𝘪𝘯𝘨𝘳𝘦𝘴𝘢 𝘶𝘯𝘢 𝘦𝘥𝘢𝘥 𝘷𝘢𝘭𝘪𝘥𝘢")
            continue

        edad = False

    # ========================================================== #
    #                RESERVA DE HABITACIÓN                      #
    # ========================================================== #

    print("\n\tHabitaciones disponibles\n")
    print("Simple: S/50 por noche")
    print("Doble: S/80 Por noche")
    print("Suite: S/150 por noche")

    reservar = True
    while reservar:
        reservar_room = input("Ingrese el tipo de room").strip().lower()

        # -------- ROOM SIMPLE -------- #
        if reservar_room == "simple":
            print(f"{nombre_cliente.title()} Usted elegio Simple Room\n")

            noche_room = True
            while noche_room:
                print("Cuantas noches desea quedarse?")
                noches = input("Ingrese la cantidad de noches: ").strip()

                try:
                    noches = int(noches)
                    cantidad_de_noches = noches
                    subtotal = cantidad_de_noches * 50

                    print("HECHO!")

                    noche_room = False
                    reservar = False

                except ValueError:
                    print("Error: TYPE ROOM: 𝘪𝘯𝘨𝘳𝘦𝘴𝘦 𝘶𝘯𝘢 𝘤𝘢𝘯𝘵𝘪𝘥𝘢𝘥 𝘷𝘢𝘭𝘪𝘥𝘢")
                    continue

        # -------- ROOM DOBLE -------- #
        elif reservar_room == "doble":
            print(f"{nombre_cliente.title()} Usted elegio Doble Room\n")

            noche_room = True
            while noche_room:
                print("Cuantas noches desea quedarse?")
                noches = input("Ingrese la cantidad de noches: ").strip()

                try:
                    noches = int(noches)
                    cantidad_de_noches = noches
                    subtotal = cantidad_de_noches * 80

                    print("HECHO!")

                    noche_room = False
                    reservar = False

                except ValueError:
                    print("Error: TYPE ROOM: 𝘪𝘯𝘨𝘳𝘦𝘴𝘦 𝘶𝘯𝘢 𝘤𝘢𝘯𝘵𝘪𝘥𝘢𝘥 𝘷𝘢𝘭𝘪𝘥𝘢")
                    continue

        # -------- ROOM SUITE -------- #
        elif reservar_room == "suite":
            print(f"{nombre_cliente.title()} Usted elegio Suite Room\n")

            noche_room = True
            while noche_room:
                print("Cuantas noches desea quedarse?")
                noches = input("Ingrese la cantidad de noches: ").strip()

                try:
                    noches = int(noches)
                    cantidad_de_noches = noches
                    subtotal = cantidad_de_noches * 150

                    print("HECHO!")

                    noche_room = False
                    reservar = False

                except ValueError:
                    print("Error: TYPE ROOM: 𝘪𝘯𝘨𝘳𝘦𝘴𝘦 𝘶𝘯𝘢 𝘤𝘢𝘯𝘵𝘪𝘥𝘢𝘥 𝘷𝘢𝘭𝘪𝘥𝘢")
                    continue

        else:
            print("Elija una Room valida!")
            continue

    # ========================================================== #
    #                      DESCUENTOS                           #
    # ========================================================== #

    total_final = subtotal

    # Descuento por edad
    if edad_cliente > 60:
        descuento_edad = subtotal * 0.15
        total_final -= descuento_edad
        print(f"¡Descuento de Adulto Mayor aplicado! (-S/ {round(descuento_edad, 2)})")

    # Descuento por consumo alto
    if total_final > 300:
        descuento_alto_consumo = total_final * 0.10
        total_final -= descuento_alto_consumo
        print(f"¡Descuento por Consumo Alto aplicado! (-S/ {round(descuento_alto_consumo, 2)})")

    # ========================================================== #
    #                      TICKET FINAL                         #
    # ========================================================== #

    print("-" * 30)
    print("        TICKET DE VENTA      ")
    print("-" * 30)
    print(f"Huesped: {nombre_cliente.upper()}")
    print(f"Room: {reservar_room}")
    print(f"Subtotal: {round(subtotal, 2)}")
    print("-" * 30)

    # -------- PROCESO DE PAGO -------- #
    pagar = True
    while pagar:
        pago = input("Ingrese el pago: ")

        try:
            pago = int(pago)
        except ValueError:
            print("Error pago invalido")
            continue

        if pago == total_final:
            print("Pago Completado!", f"Pagaste => {total_final}", sep=" | ")
            break

        elif pago > total_final:
            vuelto = pago - total_final
            print("Pago Completado!", f"Pagaste => {total_final} Vuelto de {round(vuelto, 2)}", sep=" | ")
            pagar = False

        else:
            print("Saldo insuficiente! Intentalo de nuevo")
            continue

    # ========================================================== #
    #                REGISTRAR OTRO CLIENTE                     #
    # ========================================================== #

    print("Desea registrar otro cliente?")

    registrar_validacion = True
    while registrar_validacion:
        registrar = input("Ingreso S/N: ")

        if not registrar.isupper():
            print("Repuesta incorrecta! Intentalo de nuevo")

        elif registrar == "S":
            registrar_validacion = False

        elif registrar == "N":
            registrar_validacion = False
            menu = False

# ------------------- FIN DEL PROGRAMA ------------------- #
print("Fin del programa..... ")
