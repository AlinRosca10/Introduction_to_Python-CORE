#   Numarul maxim de cupoane si durata de timp a promotiei in zile
max_cupoane = 100
durata_timp = 3
#   Starea curenta
cupoane_utilizate = 0
zilele_ramase = durata_timp

while cupoane_utilizate < max_cupoane or zilele_ramase > 0:
    #   Cererea de cupoane
    cupoane = int(input(f"Introduceti numarul de cupoane pentru ziua {durata_timp - zilele_ramase + 1}: "))

    #   Verificarea cererii
    if cupoane > max_cupoane:
        print("Cererea depaseste limita maxima de cupoane!")
        continue

    #   Actualizarea starii
    cupoane_utilizate += cupoane
    zilele_ramase -= 1

    #   Afisarea starii curente
    print(f"Numarul total de cupoane utilizate: {cupoane_utilizate}")
    print(f"Zilele ramase: {zilele_ramase}")
#   Verificarea starii finale
if cupoane_utilizate >= max_cupoane:
    print("Promotia s-a incheiat! Numarul maxim de cupoane a fost atins.")
