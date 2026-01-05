meteo = input("Cum e vremea? (ploaie/soare): ")
temperatura = int(input("Care este temperatura? (in grade Celsius): "))
vant = input("Este vant? (da/nu): ")
if meteo == "ploaie" and temperatura > 20:
    print("Ia-ti o umbrela!")
    if (vant == "da"):
        print("Afara bate vantul, fi atent!")
elif meteo == "ploaie" and temperatura <= 20:
    # This is the else block
    print("Ploua, dar e cald, nu ai nevoie de geaca.")
    if (vant == "da"):
        print("Afara bate vantul, fi atent!")
elif meteo == "soare" and temperatura > 25:
    print("Pune-ti ochelari de soare si imbracate ma lejer!")
    if (vant == "da"):
        print("Afara bate vantul, fi atent!")
elif meteo == "soare" and temperatura <= 25:
    # This is the else block
    print("Bucura-te de soare, dar imbraca-te confortabil!")
    if (vant == "da"):
        print("Afara bate vantul, fi atent!")
else:
    # This is the else block
    print("Este inorat, nu ai nevoie de nimic special!")
    if (vant == "da"):
        print("Afara bate vantul, fi atent!")