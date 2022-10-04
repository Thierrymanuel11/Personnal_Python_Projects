num = input("Entrer une série de nombre de 4 chiffres séparées par des virgules: ")
tab = num.split(",")
tab2 = []

for i in tab:
  if len(i) == 4:
    tab2.append(int(i))

for i in tab2:
  if i%5 == 0:
    print(i)