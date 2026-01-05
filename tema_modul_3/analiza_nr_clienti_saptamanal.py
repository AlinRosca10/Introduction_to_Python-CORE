#   Nr clienti saptamanal
nr_client_luni = int(input("Introduceti nr. de clienti Luni: "))
nr_client_marti = int(input("Introduceti nr. de clienti Marti: "))
nr_client_miercuri = int(input("Introduceti nr. de clienti Miercuri: "))
nr_client_joi = int(input("Introduceti nr. de clienti Joi: "))
nr_client_vineri = int(input("Introduceti nr. de clienti Vineri: "))
nr_client_sambata = int(input("Introduceti nr. de clienti Sambata: "))
nr_client_duminica = int(input("Introduceti nr. de clienti Duminica: "))
# 1 Calculam numarul total de clienti pentru intreaga saptamana
nr_client_total = nr_client_luni + nr_client_marti + nr_client_miercuri \
    + nr_client_joi + nr_client_vineri + nr_client_sambata + nr_client_duminica

# 2 Calculam numarul total de client pentru zilele lucratoare
nr_client_zile_lucr = nr_client_luni + nr_client_marti \
                    + nr_client_miercuri + nr_client_joi + nr_client_vineri

# 3 Calculam numarul total de client pentru weekend
nr_client_weekend = nr_client_sambata + nr_client_duminica

# 4 Verificare daca duminica sunt mai multi clienti decat sambata
compar_dum_sam = nr_client_duminica > nr_client_sambata
print(f"Nr. de clienti Duminica este mai mare decat Sambata: {compar_dum_sam}")

# 5 Verificare daca nr. total de clienti pentru zilele lucratoare
# este mai mare decat nr. total de clienti pentru weekend
compar_zile_lucr = nr_client_zile_lucr > nr_client_weekend
print(f"Nr. de clienti in zile lucr. este mai mare decat in weekend: {compar_zile_lucr}")

# 6 Verificare daca saptamana este un succes
succes_saptamana = nr_client_total > 1000 or nr_client_weekend > 500
print(f"Saptamana este un succes: {succes_saptamana}")

# 7 Afisare nr total de clienti pe intreaga saptamana
print(f"Nr. total de clienti pe intreaga saptamana este: {nr_client_total}")

# 8 Afisare nr total de clienti pe zilele lucratoare
print(f"Nr. total de clienti pe zilele lucratoare este: {nr_client_zile_lucr}")

# 9 Afisare nr total de clienti pe weekend
print(f"Nr. total de clienti pe weekend este: {nr_client_weekend}")
