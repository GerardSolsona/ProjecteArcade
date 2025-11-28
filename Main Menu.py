import time 
import jocs
#Main 
while True:
    print("Elegeix un joc")
    print("1.Pedra_Paper_Tisora")
    print("2.endivina el numero")
    print ("s.sortir")

    opcio = input("Sel·leciona un joc: ")

    match opcio:
        case "1": jocs.Pedra_Paper_Tisora()
        case "2": jocs.endivina_un_numero()
        case "s":
            print("sortint.")
            break
        case _: print("Opció no vàlida.")
    time.sleep(3)