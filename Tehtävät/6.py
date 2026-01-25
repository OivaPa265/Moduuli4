import random
#pyytää käyttäjältä määrn
Maara = int(input("Määrä"))
#määritää kuinka moni piste päätyy ypyrän sisälle
sijainti = 0
#Tarkistaa kuinka monta kertaa ohjelma on pyöritetty
numero = 0
while numero < Maara:
#Muodostaa suorakulmion
    x = random.randint(-1,1)
    y = random.randint(-1,1)
#tarkista jos sijainti on ympyrän sisällä
    if x*x + y*y<1:
        sijainti = sijainti + 1
    numero  = numero + 1
# laskee ympyrän sisälle saadusita pisteitä piin
pii = 3.14 * sijainti/Maara
print("pii on noin;" , pii)

