# entrada_menu.py
import random
def selecionar_nivel():
    print("Selecciona un nivel de dificultad:")
    print("1. Nivel simple (entre 0 y 100)")
    print("2. Nivel intermedio 0)")
    print("3. Nivel avanzado (entre 0 y 1.000.000)")
    print("4. Nivel experto (entre 0 y 1.000.000.000.000)")


    opcion = int(input("Ingresa el número correspondiente al nivel deseado (1-4): "))

    if opcion == 1:
        return 0, 100
    elif opcion == 2:
        return 0, 1000
    elif opcion == 3:
        return 0, 1000000
    elif opcion == 4:
        return 0, 1000000000000
    else:
        print("Opción no válida. Seleccionando nivel simple por defecto.")
        return 0, 100
selecionar_nivel()

# juego.py 
def num_intentos():
    while True:
        intentos = input("Cuantos intentos quieres: ")
        try: 
            intentos = int(intentos)
            if intentos <= 0:
                print("son muy pocos intentos")
                continue
            else:
                break 
        except:
            print("eso no es una opcion posible")
    return intentos 

numero_de_intentos = num_intentos() 
if (selecionar_nivel == 1):
    num = int(input("adivina un numero del 0 al 99"))
    while (num < 0) or (num > 99):
        print("ese numero no es valido")
    num = int(input("dime un numero del 0 al 99"))
    ale = int(random.random()*100)
elif (selecionar_nivel == 2):
    num = int()(input("adivina un numero del 0 al 999"))
    while (num < 0) or (num > 999):
        print ("ese numero no es valido")
    num = int(input("dime un numero del 0 al 999"))
    ale = int(random.random()*1000)
elif (selecionar_nivel == 3):
    num = int()(input("adivina un numero del 0 al 999999"))
    while (num < 0) or (num > 999999):
        print ("ese numero no es valido")
    num = int(input("dime un numero del 0 al 999999"))
    ale = int(random.random()*1000000)
elif (selecionar_nivel == 4):
    num = int()(input("adivina un numero del 0 al 999999999999"))
    while (num < 0) or (num > 999999999999):
        print ("ese numero no es valido")
    num = int(input("dime un numero del 0 al 999999999999"))
    ale = int(random.random()*1000000000000)

intentos = 0

while intentos<numero_de_intentos -1:
    
    intentos += 1

    if num < ale:
        print("el numero es mayor") 

    if num > ale: 
        print("el numero es menor")

    elif num == num:
        print("Has adivinado")
        print("has ganado en:", intentos, "intentos")
        break
    
    print("llevas:", intentos, "intentos")
    num = int(input("intenta de nuevo"))

if (intentos == numero_de_intentos -1):
    print("has perdido, el numero era:", ale)
