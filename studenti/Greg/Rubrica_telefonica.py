#Rubrica telefonica 
rubrica = {}
def mostra_menu(): 
    """Mostra menu opzioni disponibili"""
    print("1. aggiungi contatto")
    print("2. cerca contatto")
    print("3. mostra tutti i contatti") 
    print("4. elimina contatto")
    print("5. esci")
while True:
    mostra_menu()
    scelta = input ("scegli opzione:")
    if scelta == "1":
        nome = input ("inserisci nome contatto:")
        numero = input ("inserisci numero contatto:")
        rubrica[nome] = numero
        print(f"contatto {nome} aggiunto.")
    elif scelta == "2":
        nome = input("inserisci nome contatto:")
        if nome in rubrica:
            print(f"numero di {nome}: {rubrica[nome]}")
        else:
            print(f"contatto {nome} non trovato")
    elif scelta == "3":
        if rubrica:
            for nome, numero in rubrica.items():
                print(f"{nome}: {numero}")
        else:
            print("rubrica vuota")
    elif scelta == "4":
        nome = input("inserisci contatto da eliminare:")
        if nome in rubrica:
            del rubrica[nome]
            print(f"contatto {nome} eliminato")
        else:
            print(f"contatto {nome} non trovato")
    elif scelta == "5":
        print("uscita...")
        break
    else:
        print("opzione non valida, riprova.")
#Rubrica telefonica

