#JOC 1 Pedra_Paper_Tisora
#Definir funcions
import robot

def Pedra_Paper_Tisora():
    r=robot.robot()
    opcio_robot=r.playing()
    opcio_jugador= input ("tria pedra, paper o tisora")
    print(f"el robot tria {opcio_robot}")

    #determinar el guanyador
    if opcio_robot =="pedra" and opcio_jugador == "tisora":
        print ("guanya robot")
    if opcio_robot =="paper" and opcio_jugador == "pedra":
        print ("guanya robot")
    if opcio_robot =="tisora" and opcio_jugador == "paper":
        print ("guanya robot")
    if opcio_jugador =="pedra" and opcio_robot == "tisora":
        print ("guanya usuari")
    if  opcio_jugador =="paper" and opcio_robot == "pedra":
        print ("guanya usuari")
    if opcio_jugador =="tisora" and opcio_robot == "paper":
        print ("guanya usuari")
    if opcio_jugador == opcio_robot:
        print( "empat")

#JOC 2 endivina un numero
import random

# Definim la funció
def endivina_un_numero():
    # Generem un número aleatori entre 1 i 100
    numero_secret = random.randint(1, 100)
    intent = None
    
    print("endivina el numero")
    
    # Bucle fins que l'usuari encerti
    while intent == numero_secret:
        try:
            intent = int(input("Introdueix un número: "))
            
            if intent < numero_secret:
                print("Massa petit! ")
            elif intent > numero_secret:
                print("Massa gran!")
            else:
                print("Correcte! Has endevinat el número.")
        except ValueError:
            print("Si us plau, introdueix un número vàlid.")

# Cridem la funció
endivina_un_numero()


