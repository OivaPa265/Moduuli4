Numero = int(input ("anna tuumien määrä"))
while Numero != 0:
    if Numero >= 0:
        Sentti = Numero * 2.54
        print(f"{Numero} tuumaa on {Sentti} cm")
        Numero = int(input("anna tuumien määrä"))
    else:
     print("Annoit negatiivisen luvun :( ohjelma piti lopetaa ")
     break


