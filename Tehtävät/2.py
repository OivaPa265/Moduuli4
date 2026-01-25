#pyytää käyttäjältä tuumien määrän
Numero = int(input ("anna tuumien määrä"))
#pyöritää ohjelmaa kun numero ei ole 0
while Numero != 0:
# tekee lasku muunoksen ja printaa annetun määrän seka määrän senttimetreinä
    if Numero >= 0:
        Sentti = Numero * 2.54
        print(f"{Numero} tuumaa on {Sentti} cm")
        # pyytää uuden numeron
        Numero = int(input("anna tuumien määrä"))
        # jos käyttäjä antaa negatiivisen numeron lopetaa ohjelman ja antaa tuon tekstin
    else:
     print("Annoit negatiivisen luvun :( ohjelma piti lopetaa ")
     break


