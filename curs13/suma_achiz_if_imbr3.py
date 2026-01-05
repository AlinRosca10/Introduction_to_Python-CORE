suma_achizitiei = float(input("Introduceti suma achizitiei: "))
client = input("Client sau membru al programului de loialitate: ")

if client == "client":
    if suma_achizitiei < 100:
        reducere = 0
        print("Fara reducere.")
    else:
        if suma_achizitiei < 500:
            reducere = 0.05
            print("Reducere de 5%.")
        else:
            if suma_achizitiei < 1000:
                reducere = 0.1
                print("Reducere de 10%.")
            else:
                reducere = 0.15
                print("Reducere de 15%.")
else:
    if suma_achizitiei < 100:
        reducere = 0.05
        print("Reducere de 5%.")
    else:
        if suma_achizitiei < 500:
            reducere = 0.10
            print("Reducere de 10%.")
        else:
            if suma_achizitiei < 1000:
                reducere = 0.15
                print("Reducere de 15%.")
            else:
                reducere = 0.2
                print("Reducere de 20%.")        
pret_final = suma_achizitiei - (suma_achizitiei * reducere)
print(f"Pretul final este: {pret_final:.2f} lei.")