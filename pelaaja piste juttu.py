pelaajat = []
piste = []

while True:

    pelaaja = input("Anna pelaaja: ")
    if pelaaja.lower() == "lopeta":
        break
    pisteet = input("Anna pisteet: ")

    pelaajat.append(pelaaja)
    piste.append(int(pisteet))

print(pelaajat[piste.index(max(piste))] + ", " + str(piste[piste.index(max(piste))]))

