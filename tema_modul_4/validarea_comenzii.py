while True:
    # 1.Validarea numarului de produse
    nr_produse_comanda = int(input("Introduceti numarul de produse (1-50): "))
    if not 1 <= nr_produse_comanda <= 50:
        print("Eroare: Numar de produse invalid.")
        continue
    # 2.Validarea pret comanda
    pret_comanda = float(input("Introduceti pretul comenzii (> 0): "))
    if not pret_comanda > 0:
        print("Eroare: Pretul trebuie sa fie mai mare decat 0.")
        continue
    # 3.Statusul platii
    status_plata = input("Introduceti statusul platii (platit/neplatit/in asteptare): ").strip().lower()
    if status_plata == "platit":
        print(f"Comanda a fost procesata cu succes.\n"
              f"Numar produse: {nr_produse_comanda}.\n"
              f"Pret comanda: {pret_comanda}.\n"
              f"Status plata: {status_plata}.")
        break
    elif status_plata in {"neplatit", "in asteptare"}:
        print("Comanda nu este platita, nu poate fi procesata.")
    else:
        print("Eroare: Status de plata necunoscut.")
