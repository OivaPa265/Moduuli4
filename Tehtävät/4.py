import random
# antaa satunaisen luvun 1 ja 10 väliltä
luku = random.randint(1,10)
print("arvaa luku 1 ja 10 välillä")
# pyytää käyttäjältä vastauksen
Vastaus = int(input(" kirjoita arvauksesi tähän"))
# tarkistaa jos annetu luku oli satunainen luku
while Vastaus != luku:
    #jos liian suuri
    if Vastaus > luku:
     print(f"vähän Liian suuri luku")
     Vastaus = int(input(" kirjoita arvauksesi tähän"))
     # jos liian pieni
    elif Vastaus < luku:
     print(f" liian pieni luku")
     Vastaus = int(input(" kirjoita arvauksesi tähän"))
        # jos oikea
    if Vastaus == luku:
        print(f"oikea numero oli {luku} arvasit oikein :) jee")
        break






