vanzare = int(input("Introduceti numarul de unitati vandute: "))
if vanzare > 100:
    print("Vanzarea a fost foarte reusita!")
elif vanzare == 100:
    print("Vanzarea a fost perfecta! S-au vandut exact 100 de unitati.")
elif vanzare > 50 and vanzare <= 100:
    print("Vanzarea este solida, dar ganditi-va la actiuni suplimentare.")
else:
    print("Vanzarea a fost slaba. Propuneti actiuni promotionale urgente.")
# The above code is a simple program that checks the number of units sold and
# provides feedback based on the sales performance.
