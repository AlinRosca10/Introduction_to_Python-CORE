def decizie_de_imbracare(temperatura, umiditate, vant):
    if temperatura < 10 and umiditate > 70:
        return "Trebuie sa te imbraci mai gros!"
    elif temperatura < 15 and vant > 20:
        return "Trebuie sa te imbraci mai gros!"
    elif temperatura < 20 and umiditate > 80:
        return "Trebuie sa te imbraci mai gros!"
    else:
        return "Nu trebuie sa te imbraci mai gros!" 
# Exemplu de utilizare
if __name__ == "__main__":
    temperatura = 8
    umiditate = 75
    vant = 15
    
    mesaj = decizie_de_imbracare(temperatura, umiditate, vant)
    print(mesaj)  # Ar trebui sa afiseze "Trebuie sa te imbraci mai gros!"