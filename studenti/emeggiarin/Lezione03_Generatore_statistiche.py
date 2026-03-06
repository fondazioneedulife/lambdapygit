import statistics

numeri = []

while True:
    try:
        n = int(input("Inserisci un numero: "))
        numeri.append(n)
    except ValueError:
        print("Inserisci un numero valido.")
        continue

    if input("Continuare? (s/n): ").lower() != "s":
        break

print("Massimo:", max(numeri))
print("Minimo:", min(numeri))

pari = [x for x in numeri if x % 2 == 0]
dispari = [x for x in numeri if x % 2 != 0]

print("Numeri pari:", pari)
print("Numeri dispari:", dispari)

numeri_ordinati_crescente = sorted(numeri) 
print("Lista ordinata crescente:", numeri_ordinati_crescente)

media = sum(numeri) / len(numeri)
print("Media:", media)

mediana = statistics.median(numeri)
print("Mediana:", mediana)
