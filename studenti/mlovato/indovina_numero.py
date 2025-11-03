import random
import os

num_max_range: int = 10
max_tentativi = 5
p2: bool = False
turno = 0
gioca_ancora: str = "y"
tentativiP1 = tentativiP2 = 0

while(gioca_ancora != "n"):
    config_tentativi = input(f"Hai a disposizione {max_tentativi} tentativi, vuoi modificare? (y/n)").lower()
    if(config_tentativi == "y"):
        max_tentativi_str = input("Quanti tentativi vuoi fare? ")
        while(not(max_tentativi_str.isnumeric())):
            max_tentativi_str = input("Inserisci un numero. Quanti tentativi vuoi fare? ")
        max_tentativi = int(max_tentativi_str)
    numero_misterioso = random.randint(0, num_max_range)
    tentativiP1 = max_tentativi
    giocatore2 = input("Vuoi giocare in 2? (y/n)").lower()
    if(giocatore2 == "y"):
        p2 = True
    if(p2):
        tentativiP2 = max_tentativi
    
    print("--------------")
    while(tentativiP1 > 0 or tentativiP2 > 0):
        os.system("clear")
        print(f"P1 hai {"ancora " if tentativiP1 != max_tentativi else ""}{tentativiP1} tentativi")
        tentativiP1 = tentativiP1 - 1
        
        sceltaP1_str = input("Indovina il numero! ")
        while(not(sceltaP1_str.isnumeric())):
            sceltaP1_str = input("Inserisci un numero. Indovina il numero! ")
        sceltaP1 = int(sceltaP1_str)     
        print("--------------")
        if(sceltaP1 == numero_misterioso):
            print("P1 Hai vinto!")
            input("Premi un bottone per continuare.")
            os.system("clear")
            break
        elif sceltaP1 < numero_misterioso:
            if(tentativiP1 == 0):
                print(f"P1 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
            else:
                print("P1 Sei troppo basso, punta più in alto")
        else:
            if(tentativiP1 == 0):
                print(f"P1 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
            else:
                print("P1 Sei troppo alto, abbassa il tiro")
        input("Premi un bottone per continuare.")
        os.system("clear")
        if p2:
            print(f"P2 tocca a te, hai {"ancora " if tentativiP2 != max_tentativi else ""}{tentativiP2} tentativi")
            tentativiP2 = tentativiP2 - 1
            sceltaP2_str = input("Indovina il numero! ")
            while(not(sceltaP2_str.isnumeric())):
                sceltaP2_str = input("Inserisci un numero. Indovina il numero! ")
            sceltaP2 = int(sceltaP2_str)  
            if(sceltaP2 == numero_misterioso):
                print("P2 Hai vinto!")
                input("Premi un bottone per continuare.")
                os.system("clear")
                break
            elif sceltaP2 < numero_misterioso:
                if(tentativiP2 == 0):
                    print(f"P2 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
                else:
                    print("P2 Sei troppo basso, punta più in alto")
            else:
                if(tentativiP2 == 0):
                    print(f"P2 hai perso! Il numero era: {numero_misterioso} sarai più fortunato la prossima volta")
                else:
                    print("P2 Sei troppo alto, abbassa il tiro")
            input("Premi un bottone per continuare.")
            os.system("clear")
    gioca_ancora = input("Vuoi giocare ancora? (y/n)").lower()
    