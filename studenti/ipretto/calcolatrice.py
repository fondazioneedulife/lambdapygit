
continuare:bool = True

while continuare:

    operazione = input("Inserisci operazione (+, -, *, /, gg): ")   
    
    risposta:str    
    risultato: int

    if operazione == "+":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        risultato = n1+n2
        print(risultato)

    elif operazione == "-":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        risultato = n1-n2
        print(risultato)

    elif operazione == "*":
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))
        risultato = n1*n2
        print(risultato)

    elif operazione == "/":
        controllo_div:bool = True
        n1 = int(input("Inserisci il primo numero: "))

        while controllo_div:
            n2 = int(input("Inserisci il secondo numero: "))
            if n2 == 0:
                print("INSERISCI UN NUMERO DIVERSO DA 0")
            else:
                controllo_div = False

        risultato = n1/n2
        print(risultato)
    
    #da finire!!
    elif operazione == "gg":

        #g1 = int(input("Inserisci il giorno 1: "))
        m1 = str(input("Inserisci il mese 1: "))
        a1 = int(input("Inserisci l'anno 1: "))

        #g2 = int(input("Inserisci il giorno 2: "))
        m2 = str(input("Inserisci il mese 2: "))
        a2 = int(input("Inserisci l'anno 2: "))

        #variabili per salvare il numero del mese partendo dalla parola
        m1n:int
        m2n:int
        
        if(m1 == "gennaio" or m1 == "Gennaio"): m1n=1
        if(m2 == "gennaio" or m2 == "Gennaio"): m2n=1        
        if(m1 == "febbraio" or m1 == "Febbraio"): m1n=2
        if(m2 == "febbraio" or m2 == "Febbraio"): m2n=2
        if(m1 == "marzo" or m1 == "Marzo"): m1n=3
        if(m2 == "marzo" or m2 == "Marzo"): m2n=3
        if(m1 == "aprile" or m1 == "Aprile"): m1n=4
        if(m2 == "aprile" or m2 == "Aprile"): m2n=4
        if(m1 == "maggio" or m1 == "Maggio"): m1n=5
        if(m2 == "maggio" or m2 == "Maggio"): m2n=5
        if(m1 == "giugno" or m1 == "Giugno"): m1n=6
        if(m2 == "giugno" or m2 == "Giugno"): m2n=6
        if(m1 == "luglio" or m1 == "Luglio"): m1n=7
        if(m2 == "luglio" or m2 == "Luglio"): m2n=7
        if(m1 == "agosto" or m1 == "Agosto"): m1n=8
        if(m2 == "agosto" or m2 == "Agosto"): m2n=8
        if(m1 == "settembre" or m1 == "Settembre"): m1n=9
        if(m2 == "settembre" or m2 == "Settembre"): m2n=9
        if(m1 == "ottobre" or m1 == "Ottobre"): m1n=10
        if(m2 == "ottobre" or m2 == "Ottobre"): m2n=10
        if(m1 == "novembre" or m1 == "Novembre"): m1n=11
        if(m2 == "novembre" or m2 == "Novembre"): m2n=11
        if(m1 == "dicembre" or m1 == "Dicembre"): m1n=12
        if(m2 == "dicembre" or m2 == "Dicembre"): m2n=12


        if(a1 <= a2):
            diff_anno = a2-a1
            diff_mese = m2n - m1n
            #if(diff_mese<0):
             #   diff_mese = 12 - diff_mese
           # print(diff_anno)
            print(diff_mese)
        
    
    else:
        print("Scegli un operazione valida!")

#Ciclo di controllo per capire se l'utente vuole continuare, se risponde qualcosa di diverso da si, Si, no, No gli viene
#rifatta la domanda
    controllo:bool = True
    while controllo:
        risposta = input("Vuoi continuare? ")
        if risposta == "Si" or risposta == "si":
            continuare = True
            controllo = False
        elif risposta == "No" or risposta == "no":
            continuare = False
            controllo = False


