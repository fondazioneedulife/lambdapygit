risposta = "si"
while risposta == "si":
    a = eval(input("Inserisci il primo numero: "))
    b = eval(input("Inserisci il secondo numero: "))
    risultato = 0
    c = str(input("Inserisci il simbolo dell'operazione(+,-,*,/,**): "))

    if c == "+":
        risultato = a + b
    elif c == "-":
        risultato = a - b
    elif c == "*":
        risultato = a * b
    elif c == "/":
        if b != 0:
            risultato = a / b
        else:
            print("Non puoi dividere per zero.")
    elif c == "**":
        risultato = a ** b

    if b != 0:
        print("Il risultato è:",risultato)

    risposta = input("Vuoi continuare? (si/no): ")

print("Fine programma")

""""
giorni = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mese1 = eval(input("Inserisci il primo mese: "))
mese2 = eval(input("Inserisci il secondo mese: "))
giorno1 = 0
giorno2 = 0
differenza = 0
i = 0 

for i in range(1,13):
    if giorni[i] == mese1:
        giorno1 = i
    elif giorni[i] == mese2:
        giorno2 = i
i = 0
for g in range(mese1, mese2):
    for i in range(1,13):
        if(i>=mese1 and i<=mese2):
            differenza = differenza + i

print("La differenza dei giorni tra i due mesi è di ", differenza) """