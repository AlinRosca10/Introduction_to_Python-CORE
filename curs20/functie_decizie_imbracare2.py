def decizie_de_imbracare(meteo):
    if meteo == "ploaie":
        return "Ia-ti  umbrela!"
    elif meteo == "soare":
        return "Pune-ti ochelari de soare!"
    else:
        return "Este inorat, dar nu ai nevoie de nimic special!"


# Exemplu de utilizare
if __name__ == "__main__":
    meteo = "ploaie"
    
    mesaj = decizie_de_imbracare(meteo)
    print(mesaj)  # Ar trebui sa afiseze "Ia-ti  umbrela!"
    
conditii_vreme = ["ploaie", "soare", "innorat"]
for meteo in conditii_vreme:
    mesaj = decizie_de_imbracare(meteo)
    print(f"Pentru vremea '{meteo}', mesajul este: {mesaj}")
