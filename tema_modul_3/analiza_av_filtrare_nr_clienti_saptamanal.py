#   1.Intruducereți nr. de clienți pentru fiecare zi a săptămânii:
clienti_luni = int(input("Introduceti nr. de clienti pentru luni: "))
clienti_marti = int(input("Introduceti nr. de clienti pentru marti: "))
clienti_miercuri = int(input("Introduceti nr. de clienti pentru miercuri: "))
clienti_joi = int(input("Introduceti nr. de clienti pentru joi: "))
clienti_vineri = int(input("Introduceti nr. de clienti pentru vineri: "))
clienti_sambata = int(input("Introduceti nr. de clienti pentru sambata: "))
clienti_duminica = int(input("Introduceti nr. de clienti pentru duminica: "))

# 2. Calculați și afișați nr. total de clienți pentru întreaga săptămână
total_clienti = clienti_luni + clienti_marti + clienti_miercuri + clienti_joi \
    + clienti_vineri + clienti_sambata + clienti_duminica
print(f"Nr. total de clienti pentru intreaga saptamana este: {total_clienti}")

# 3. Afișați nr. total de clienți pentru zile lucrătoare (luni-vineri)
clienti_zile_lucr = clienti_luni + clienti_marti + clienti_miercuri + \
    clienti_joi + clienti_vineri
print(f"Nr. total de clienti pentru zile lucratoare este: {clienti_zile_lucr}")

# 4. Afișați nr. total de clienți pentru weekend (sâmbătă-duminică)
clienti_weekend = clienti_sambata + clienti_duminica
print(f"Nr. total de clienti pentru weekend este: {clienti_weekend}")

# 5. Comparare număr de clienți weekend
if clienti_duminica > clienti_sambata: print("Duminica a fost o zi de vanzari mai buna decat sambata.")
if clienti_sambata > clienti_duminica: print("Sambata a fost o zi de vanzari mai buna decat duminica.")
if clienti_sambata == clienti_duminica: print("Sambata si duminica au avut acelasi numar de clienti.")

# 6. Comparare număr de clienți zile lucrătoare și weekend
if clienti_zile_lucr > clienti_weekend:
    print("Zilele lucratoare au avut mai multi clienti decat weekendul.")
else:
    print("Weekendul a avut mai multi clienti decat zilele lucratoare.")

# 7. Verificare prag individul 100 de clienți pentru zilele de weekend
if clienti_sambata > 100 and clienti_duminica > 100:
    print("Ambele zile de weekend au avut mai mult de 100 de clienti.")
elif clienti_sambata > 100 or clienti_duminica > 100:
    print("Doar o zi de weekend a avut mai mult de 100 de clienti.")
else:
    print("Nici o zi de weekend nu a avut mai mult de 100 de clienti.")
