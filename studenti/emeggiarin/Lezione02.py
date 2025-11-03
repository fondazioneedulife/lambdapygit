

while True:
   try:
      num1 = float(input("Inseirsci numero 1: "))
      num2 = float(input("Inserisci numero 2: "))
   except ValueError:
       print("Input non valido. Per favore inserisci dei numeri.")
   operazione = input("Inserisci operazione (+,-,*,/): ")

   if operazione == "+":
      risultato = num1 + num2
      print(risultato)
   elif operazione == "-":
      risultato = num1 - num2
      print(risultato)
   elif operazione == "*":
      risultato = num1 * num2
      print(risultato)
   elif operazione == "/":
      risultato = num1 / num2
      print(risultato)
   else:
      risultato = "Operazione non valida"
      print(risultato)

   continua = input("Vuoi fare un'altra operazione? (s/n): ")

   if continua.lower() != "s":
      print("Programma terminato.")
      break
