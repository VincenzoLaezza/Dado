import random

Prova = 1000
i = 0
lista = [0,0,0,0,0,0]

def dado ():
	return random.randrange (1,7)
for i in range(Prova):
	risultato = dado()
	lista[risultato-1]+=1

print (lista)