#oikeat käyttäjä ja salasanan vastaukset
KÄYTTIS ="python"
SALASANA = "rules"
# määritää kuinkamonta yritystä on tehty
yritys =0
while yritys!=5:
#pyytää käyttäjälätä käyttäjän seka salasanan
    kays=input("anna käyttäjä")
    salasana=input("anna salasana")
# tarkistaa jos käyttäjä ja salasana ovat oikeat
    if kays == KÄYTTIS and salasana == SALASANA :
        print("Tervetuloa")
#lopetaa ohjelamn jos yritysten määr on 5
        if yritys == 5:
         break
    yritys=yritys+1

else:

        print("pääsy evätty")
