nr_articole_ramase = 50
timp_livrare = 48

while nr_articole_ramase > 0 and timp_livrare > 0:
    if nr_articole_ramase >= 10:
        print(f"Mai sunt {nr_articole_ramase} articole de livrat.")
        nr_articole_ramase -= 1
    elif nr_articole_ramase < 10:
        print("Avertisment: Nivel critic scazut al stocului!")
        print(f"Mai sunt {nr_articole_ramase} articole de livrat.")
        nr_articole_ramase -= 1
    else:
        print("Nu mai sunt articole de livrat.")
    
    if timp_livrare > 0:
        print(f"Timpul de livrare este {timp_livrare} ore.")
        timp_livrare -= 1
    else:
        print("Timpul de livrare a expirat - comenzile sunt inchise.")