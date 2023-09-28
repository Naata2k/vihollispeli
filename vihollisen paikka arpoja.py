import random
lista = []
for x in range(1001):
    lista.append(str(random.randint(1,100)) + "." + str(random.randint(1,100)))
print(random.choice(lista))
