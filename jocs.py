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
#definir funcions
def endivina_un_numero():
    return

