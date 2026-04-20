import os
os.system("clear")
gimnacio = True
while gimnacio: 
    print("Gimnacio Py\n")
    #!-------------- Datos del usuario  -------------------!
    nombre = input("Ingrese su nombre: ")
    if len(nombre) <= 3:
        print("Nombre demasiado corto! ingresa otro nombre")
        continue
    #!---------------- Evaluar nombre ---------------------!
    peso = input(f"{nombre} ingrese su peso: ")
    try:
        peso = float(peso)
    except ValueError:
        print("Error en la validacion de peso")
        continue
    #!------------------- Evaluar peso ---------------------! 
    altura = input(f"{nombre} ingrese su altura: ")
    try:
        altura = float(altura)
    except ValueError:
        print("Error: Ingresa un numero valido")
        continue #Hace regresar al bucle principal
    #!------------------ Evaluar altura --------------------!
    edad = input(f"{nombre} ingrese su edad: ")
    try:
        edad = int(edad)
    except ValueError:
        print("Error en la validacion de edad")
        continue
    #Peso = Float
    #Altura = Float
    #Edad = int
    #!-------------Fin en la Validacion de datos -----------!
    #!-------------------- ---IMC --------------------------!
    imc = peso / (altura ** 2)
    #!-------------------- Resultados ----------------------!
    if imc < 18.5:
        categoria = "Bajo peso"
        print(f"{nombre} tienes bajo peso, tu IMC es {round(imc,2)}")
    elif imc < 25:
        categoria = "Normal"
        print(f"{nombre} tienes peso normal, tu IMC es {round(imc,2)}")
    elif imc < 30:
        categoria = "Sobrepeso"
        print(f"{nombre} tienes soprepeso, tu IMC es {round(imc,2)}")
    else:
        categoria = "Obesidad"
        print(f"{nombre} tienes obesidad, tu IMC es {round(imc,2)}")
    #!------------------- Fin de los resultados -------------!
    #!-------------------------Pregunta ---------------------!
    pregunta = True
    while pregunta:
        
        print("\n{0} ¿Cuál es tu nivel de actividad?\n".format(nombre))
    
        print("1. Sedentario (casi no hago ejercicio")
        print("2. Moderado (ejercicio 3 veces por semana)")
        print("3. Activo (ejercicio todos los días)")
        opcion = input(f"\n{nombre} por favor escriba su nivel de actividad: ").lower()
        if opcion == "sedentario":
            calorias = (peso * 25)
            pregunta = False
        elif opcion == "moderado":
            calorias = (peso * 30)
            pregunta = False
        elif opcion == "activo":
            calorias = (peso * 35)
            pregunta = False
        else:
            print("Error respuesta incorrecta")
    #!--------------------- Fin de la pregunta --------------!
    #!--------------------- Reporte / info ------------------!
    print(f"{nombre} Tu informe acuerdo los datos correpondidos\n")
    
    print(f"Nombre: {nombre}")
    print(f"Peso: {peso}Kg")
    print(f"Altura: {altura}")
    print(f"IMC: {round(imc,2)} y tu categoria es {categoria}")
    print(f"Calorias recomendadas: {calorias}\n")
    
    confirmar = True
    while confirmar:
        print(f"{nombre} Desea calcular a otra persona?")
        responder = input("Confirmar S/N: ").lower()
        if responder == "si" or responder == "s" or responder == "yes":
            confirmar = False
        elif responder == "no" or responder == "n":
            print("Saliendo del programa....")
            confirmar = False
            gimnacio = False
        else:
            print("{0} elija una opcion correcta!".format(nombre))
print("Fin.")
#!---------------------- FIN DEL PROGRAMA -------------------!