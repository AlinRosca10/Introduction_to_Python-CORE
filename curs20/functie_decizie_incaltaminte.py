def decizie_incaltaminte(meteo, temperatura, umiditate, vant):
    if meteo == "ploaie" or umiditate > 70:
        return "Trebuie sa porti incaltaminte impermeabila!"
    elif temperatura < 10 and vant > 20:
        return "Trebuie sa porti incaltaminte calduroasa!"
    elif temperatura < 15 and umiditate > 80:
        return "Trebuie sa porti incaltaminte calduroasa!"
    else:
        return "Nu trebuie sa porti incaltaminte speciala!"
    
# Exemplu de utilizare
if __name__ == "__main__":
    meteo = "ploaie"
    temperatura = 8
    umiditate = 75
    vant = 15
    
    mesaj = decizie_incaltaminte(meteo, temperatura, umiditate, vant)
    print(mesaj)  # Ar trebui sa afiseze "Trebuie sa porti incaltaminte impermeabila!"