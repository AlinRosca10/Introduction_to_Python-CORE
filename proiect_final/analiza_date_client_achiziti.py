#   Functie pentru introducerea numelui si prenumelui utilizatorului
def citeste_nume():
    while True:
        nume_utilizator = input("Introduceți numele si prenumele "
                                "utilizatorului: ").strip().split()
        if len(nume_utilizator) < 2:
            print("Avertisment: Numele nu a fost introdus corect! Va rugam sa "
                  "introduceti cel putin 2 cuvinte.")
            continue
        else:
            nume = nume_utilizator[0]
            prenume = ' '.join(nume_utilizator[1:])
            return nume, prenume


#   Functie pentru introducerea daatelor despre achizitii
def nr_achiziti():
    while True:
        nr_total_achiziti = int(input("Introduceti numarul de achizitii din "
                                      "ultimul an: "))
        suma_total_achiziti = 0
        nr_achiziti_mari = 0
        if nr_total_achiziti > 1:
            for achiziti in range(nr_total_achiziti):
                valoare_achizitie = float(input("Introduceti suma pentru "
                                                f"achizitia {achiziti + 1}: "))
                suma_total_achiziti += valoare_achizitie
                if valoare_achizitie > 10000:
                    nr_achiziti_mari += 1
            break
        elif nr_total_achiziti == 1:
            valoare_achizitie = float(input("Introduceti suma pentru singura "
                                            "achizitie: "))
            print(f"A fost efectuata o singura achizitie in ultimul an in "
                  f"valoare de {valoare_achizitie:.2f} lei.")
            suma_total_achiziti = valoare_achizitie
            if suma_total_achiziti > 10000:
                nr_achiziti_mari += 1
                print(f"Si aceasta a fost peste 10.000 lei, respectiv: "
                      f"{suma_total_achiziti:.2f}")
            break
        else:
            print("Numarul de achizitii trebuie sa fie mai mare decat 0.")
            continue
    return suma_total_achiziti, nr_achiziti_mari, nr_total_achiziti


#   Functie pentru determinarea statutului utilizatorului
def determina_statut(suma_total_achiziti, nr_total_achiziti):
    if suma_total_achiziti > 100000 and nr_total_achiziti > 10:
        return "VIP", 0.1
    else:
        return "STANDARD", 0.05


# 1. Citirea si validarea numelui si prenumelui utilizatorului
nume_client, prenume_client = citeste_nume()

# 2. Introducerea datelor despre achizitie:
suma_achiziti_client, nr_achiziti_10000, nr_achiziti_client = nr_achiziti()

# 3. Atribuirea statutului clientului
statut_client, reducere_client = determina_statut(suma_achiziti_client,
                                                  nr_achiziti_client)

# 4. Atribuirea reducerilor pentru urmatoarele achizitii
mesaj = (f"Stimate {prenume_client}, ati cheltuit in total "
         f"{suma_achiziti_client:.2f}, efectuand {nr_achiziti_client}")

if nr_achiziti_10000 > 1 and nr_achiziti_client > 1:
    mesaj += (f" achizitii, dintre care {nr_achiziti_10000} achizitii au fost "
              f"peste 10.000 de lei. Utilizatorul {nume_client} "
              f"{prenume_client} are statut de utilizator {statut_client}.")
elif nr_achiziti_10000 == 1 and nr_achiziti_client > 1:
    mesaj += (" achizitii, dintre care o singura achizitie a fost peste 10.000"
              f"de lei. Utilizatorul {nume_client} {prenume_client} are"
              f" statut de utilizator {statut_client}.")
elif nr_achiziti_10000 == 1 and nr_achiziti_client == 1:
    mesaj += (" achizitie. Atentie: aceasta a fost peste 10.000 de lei. "
              f"Utilizatorul {nume_client} {prenume_client} are"
              f" statut de utilizator {statut_client}.")
else:
    mesaj += (f" achizitie. Utilizatorul {nume_client} {prenume_client} are "
              f"statut de utilizator {statut_client} si nu a efectuat "
              "achizitii peste 10.000 de lei in ultimul an.\n Avertisment: Se "
              "dispune impunerea unor noi oferte si noi promotii personalizate"
              " pentru atragerea si fidelizarea utilizatorului.")
print(mesaj)

while (True):
    pret_articol = float(input(f"Stimate {prenume_client}, introduceti pretul "
                               "articolului dorit: "))
    if pret_articol > 0:
        pret_articol_redus = pret_articol * (1 - reducere_client)
        print(f"Pretul articolului cu reducere este: {pret_articol_redus:.2f}")
        break
    else:
        print("Avertisment: Pretul trebuie sa fie mai mare decat 0.")
        continue
