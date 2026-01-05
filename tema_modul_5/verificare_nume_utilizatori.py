def numar_vocale(nume):
    vocale = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    contor_vocale = 0
    for caracter in nume:
        if caracter in vocale:
            contor_vocale += 1

    return contor_vocale


while True:
    nume_client = input("Introduceti numele clientului: ")
    numar_vocale_client = numar_vocale(nume_client)
    if numar_vocale_client == 0:
        print("Clientul nu are vocale in nume. Programul se inchide.")
        break
    elif numar_vocale_client == 1:
        print(f"Numele {nume_client} contine o singura vocala.")
    else:
        print(f"Numele {nume_client} contine {numar_vocale_client} vocale.")
