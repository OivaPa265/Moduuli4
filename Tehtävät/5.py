KÄYTTIS ="python"
SALASANA= "rules"
yritys =0
while yritys!=5:
    kays=input("anna käyttäjä")
    salasana=input("anna salasana")
    if kays == KÄYTTIS and salasana == SALASANA :
        print("Tervetuloa")
        if yritys == 5:
         break
    yritys=yritys+1

else:
        print("pääsy evätty")


















