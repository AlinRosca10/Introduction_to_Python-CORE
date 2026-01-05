clienti = ["Marco", "Giovanni", "Magda", "Luca", "Alessandro", "Francesco", "Anna", "Leva", "Tom"]
clienti_loiali = ["Marco", "Giovanni", "Tom", "Alessandro"]

for client in clienti:
    if client not in clienti_loiali:
        print(f"Stimate {client}, avem o oferta speciala pentru dumneavoastra pentru a deveni membru loial!")
    else:
        print(f"Stimate {client}, va multumim ca sunteti client loial, aveti reducere 25%!")
        
print("Va multumim pentru comanda!")
