suma_achizitiei = float(input("Introduceti suma achizitiei: "))
if suma_achizitiei < 100:
    reducere = 0
    print("Fara reducere.")
else:
    if suma_achizitiei < 500:
        reducere = 0.05
        print("Reducere de 5%.")
    elif suma_achizitiei < 1000:
        reducere = 0.1
        print("Reducere de 10%.")
    elif suma_achizitiei < 2000:
        reducere = 0.15
        print("Reducere de 15%.")
    else:
        reducere = 0.2
        print("Reducere de 20%.")
            
pret_final = suma_achizitiei - (suma_achizitiei * reducere)
print(f"Pretul final este: {pret_final:.2f} lei.")