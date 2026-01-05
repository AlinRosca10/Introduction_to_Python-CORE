nume = input("Cum te numesti ? ")
print("Salut, " + nume + " !")
# print("Hello! How are you?")
print(f"Salut, {nume} !")

primul_numar = input("Introdu primul numar: ")
al_doilea_numar = input("Introdu al doilea numar: ")

suma=primul_numar + al_doilea_numar # logica il concateneaza ca este string
print(f"Suma este: {suma}")

suma = int(primul_numar) + int(al_doilea_numar) # logica il concateneaza ca este string
print(f"Suma este: {suma}")