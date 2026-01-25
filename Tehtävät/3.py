# määritää suuriman ja pienimän luvun tyhjiksi
pienin = None
suurin = None
while True:
#Pyytää käyttäjältä numeroita
    Syote = input ("Anna Numero tyhjä lopettaa: ")
#lopetaa ohjelman jos käyttäjä antaa tyhjää
    if Syote== "":
        break
    #tarkistaa pienimän numeron
    if pienin is None or Syote < pienin:
        pienin = Syote
    #tarkistaa suuriman numeron
    if suurin is None or Syote > suurin:
         suurin = Syote
    #printaa vastaukset
print (f"pienin numero oli {pienin} ja suurin numero oli {suurin}")