import time
from test import *
text = """
Bienvenue dans ton convertisseur personnel M.Djeumen Manuel.
Ici tu pourras effectuer tes converions de la base 10 vers une base de ton choix.
Entrer le nombre en base 10 a convertir :
"""
num = int(input(text))
num2 = int(input("Entre la base dans laquelle tu veux convertir ce nombre: "))
while num2 > num or num2 < 0:
    num2 = int(input("La base doit etre plus petite que le nombre en question et positive. Entre encore une base: "))

conv = decimal_to_n(num, num2)
#print(f"La conversion de "+str(num)+ " en la base "+str(num2) +" est " + str(conv))
print(f"La convrsion de {num} en la base {num2} est {conv}")
time.sleep(5)