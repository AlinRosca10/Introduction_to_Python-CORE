from proiect_final.analiza_date_client_achiziti import nr_achiziti

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
              "dispune impunerea unor noi oferte si promotii personalizate "
              "pentru utilizator pentru atragerea acestuia.")
print(mesaj)


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
              "dispune impunerea unor noi oferte si promotii personalizate "
              "pentru utilizator pentru atragerea acestuia.")
print(mesaj)