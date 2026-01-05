name_user1 = input("Introduceti numele utilizatorului: ")
print(f"Salut, {name_user1} !")
no_achizitii1 = int(input("Introduceti numarul de achizitii: "))
varsta_user1 = int(input("Introduceti varsta utilizatorului: "))
if varsta_user1 < 18:
    print("Clientul este minor.")
    if varsta_user1 >= 18:
        print("Clientul este major.")
        if no_achizitii1 > 0:
            print(f"Clientul {name_user1} in varsta de {varsta_user1} \
                a facut {no_achizitii1} achizitii.")
        else:
            print(f"Clientul {name_user1} in varsta de {varsta_user1} \
                nu a facut achizitii.")


name_user2 = input("Introduceti numele utilizatorului: ")
print(f"Salut, {name_user2} !")
no_achizitii2 = int(input("Introduceti numarul de achizitii: "))
varsta_user2 = int(input("Introduceti varsta utilizatorului: "))
if varsta_user2 < 18:
    print("Clientul este minor.")
    if varsta_user2 >= 18:
        print("Clientul este major.")
        if no_achizitii2 > 0:
            print(f"Clientul {name_user2} in varsta de {varsta_user2} \
                a facut {no_achizitii2} achizitii.")
        else:
            print(f"Clientul {name_user2} in varsta de {varsta_user2} \
                nu a facut achizitii.")

suma_achizitii = no_achizitii1 + no_achizitii2
print(f"Clienții {name_user1} și {name_user2} au realizat împreună {suma_achizitii} de achiziții.")
