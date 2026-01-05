meteo = "ploaie"
temperatura = 20
vant = True
if meteo == "ploaie":
    if temperatura > 20:
        print("Ia-ti o umbrela")
    else:
        print("Ploua, dar e cald, nu ainevoie de geaca.")
else:
    if meteo == "soare":
        if temperatura > 25:
            print("Pune-ti ochelari de soare si imbracate ma lejer!")
        else:
            print("Bucura-te de soare, dar imbraca-te confortabil!")
    else:
        print("Este inorat, nu ai nevoie de nimic special!")