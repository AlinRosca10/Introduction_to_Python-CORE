mesaj = "Aceasta este o sarcina pentru exersare"
print(mesaj)
pozitie = mesaj.find("sarcina")
print(f"Indexul este {pozitie}")
lungime = len(mesaj)
print(f"Lungimea mesajului este {lungime}")
subsir = mesaj[0:15]
print(f"Subsirul este {subsir}")
lista_cuvinte = mesaj.split()
print(f"Lista de cuvinte este {lista_cuvinte}")
index_ultim = mesaj.rfind("e")
print(f"Ultima aparitie a literei e este la indexul {index_ultim}")
cuvant_nou = mesaj.replace("exersare", "testare")
print(cuvant_nou)
