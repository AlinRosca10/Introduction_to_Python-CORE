while True:
    # 1.Introducerea si validarea numelui si prenumelui clientului
    nume_utilizator = input("Introduceți numele si prenumele utilizatorului"
                            "(< 2 cuvinte): ").split()
    if len(nume_utilizator) < 2:
        print("Avertisment: Nume introdus incorect!")
        continue
    elif len(nume_utilizator) == 2:
        nume_client = nume_utilizator[0]
        prenume_client = nume_utilizator[1]
    else:
        nume_client = nume_utilizator[0]
        prenume_client = ' '.join(nume_utilizator[1:])

    # 2. Introducerea datelor despre achizitie:
    nr_total_achiziti = int(input("Introduceti numarul de achizitii din "
                                  "ultimul an: "))
    if nr_total_achiziti <= 0:
        print("Numarul de achizitii trebuie sa fie mai mare decat 0.")
        continue
    elif nr_total_achiziti == 1:
        valoare_achizitie = float(input("Introduceti suma pentru singura "
                                        "achizitie: "))
        print(f"A fost efectuata o singura achizitie in ultimul an in valoare "
              f"de {valoare_achizitie} lei")
    else:
        suma_total_achiziti = 0
        contor_achizitii_mari = 0
        for achizitie in range(nr_total_achiziti):
            valoare_achizitie = float(input("Introduceti suma pentru achzitia "
                                            f"{achizitie + 1}: "))
            suma_total_achiziti += valoare_achizitie
            if valoare_achizitie > 10000:
                contor_achizitii_mari += 1
        if suma_total_achiziti > 100000 and nr_total_achiziti > 10:
            status_utilizator = "VIP"
            reducere_utilizator = 0.1
        else:
            status_utilizator = "STANDARD"
            reducere_utilizator = 0.05
        print(f"Stimate {prenume_client}, ati cheltuit in total "
              f"{suma_total_achiziti}, dintre care {contor_achizitii_mari} au "
              f"fost peste 10.000 de lei. Utilizatorul {prenume_client} are "
              f"statut de utilizator {status_utilizator}.\n")
        pret_articol = float(input(f"Stimate {prenume_client},Introduceti "
                                   "pretul articolului dorit: "))
        pret_articol_redus = pret_articol * (1 - reducere_utilizator)
        print(f"Pretul articolului cu reducere este: {pret_articol_redus}")
    break
