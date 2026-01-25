
pienin = None
suurin = None
while True:
    Syote = input ("Anna Numero tyhjä lopettaa: ")
    if Syote== "":
        break
    if pienin is None or Syote < pienin:
        pienin = Syote
    if suurin is None or Syote > suurin:
         suurin = Syote
print (f"pienin numero oli {pienin} ja suurin numero oli {suurin}")