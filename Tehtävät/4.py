import random
luku = random.randint(1,10)
print("arvaa luku 1 ja 10 välillä")
Vastaus = int(input(" kirjoita arvauksesi tähän"))
while Vastaus != luku:
    if Vastaus > luku:
     print(f"vähän Liian suuri luku")
     Vastaus = int(input(" kirjoita arvauksesi tähän"))
    elif Vastaus < luku:
     print(f" liian pieni luku")
     Vastaus = int(input(" kirjoita arvauksesi tähän"))
    if Vastaus == luku:
        print(f"oikea numero oli {luku} arvasit oikein :) jee")
        break






