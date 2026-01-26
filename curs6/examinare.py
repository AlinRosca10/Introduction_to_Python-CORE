# Să examinăm următoarele nume care au fost folosite în cod. 
# Sarcina noastră este să evaluăm care dintre aceste nume respectă regulile de denumire 
# și care nu. Vom folosi următoarele criterii:
# snake_case pentru variabile şi funcţii;
# PascalCase pentru clase;
# litere mari pentru constante, cu liniuţa de subliniere între cuvinte.
# Îl vom ajuta pe Alex să clasifice următoarele nume:

# numarUtilizator
# calculeaza_suma
# VALOARE_Maxima
# Masina
# constanta_Numar
# afiseazaInformatii
# PI
# Persoana


# Care nume sunt corect formatate conform regulilor pe care le-am învățat?
# Îl putem ajuta pe Alex să corecteze numele incorecte? 
# Să le redenumim folosind regulile de denumire pentru variabile, funcții și clase.
# Sarcină bonus: Alex a cerut ajutor în crearea a trei noi nume pentru variabile, 
# funcții și clase. Să încercăm să venim cu trei nume care sunt clare, 
# semnificative și conforme cu regulile pe care le-am învățat.

#  Întrebare pentru reflecție: 
# Cum va îmbunătăți denumirea consecventă lizibilitatea codului 
# și va facilita munca în echipă pe proiecte?

numar_utilizator = input("Introduceti un numar: ")


def calculeaza_suma(a, b):
    return a + b


calculeaza_suma

VALOARE_MAXIMA = 1000
masina = "BMW"
CONSTANTA_NUMAR = 3.1415926536


def afiseaza_informatii(nume, prenume):
    print(f"Numele este: {nume}, Prenumele este: {prenume}")
    

afiseaza_informatii
PI = 3.14
persoana = "Ion Popescu"


class Persoana:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume


class PersoanaInterimara:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
         
    def afiseaza_informatii(self):
        print(f"Numele este: {self.nume}, Prenumele este: {self.prenume}")

# Nume corecte:
# numar_utilizator
# calculeaza_suma
# VALOARE_MAXIMA
# PI
# PersoanaInterimara
# Nume incorecte:
# Masina
# constanta_Numar
# afiseazaInformatii
# Nume corecte:
# masina
# constanta_numar
# afiseaza_informatii
# Nume incorecte:
# numarUtilizator
# calculeaza_suma
# VALOARE_Maxima


class MasinaSuperioara:
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model
        
    def afiseaza_informatii(self):
        print(f"Marca este: {self.marca}, Modelul este: {self.model}")
        

class ConstantaValoare:
    VALOARE_MAXIMA = 1000
    
    def __init__(self, valoare):
        self.valoare = valoare
    
    def afiseaza_informatii(self):
        print(f"Valoarea maxima este: {self.VALOARE_MAXIMA}, Valoarea este: {self.valoare}")


class LaptopSeller:
    
    def __init__(self, marca, model):
        self.marca = marca
        self.model = model
        
    def afiseaza_informatii(self):
        print(
            f"Marca laptopului este: {self.marca},"
            f"Modelul laptopului este: {self.model}"
            )


CONSTANTA_IMPERMEABILITATE = 0.8


def calculeaza_impermeabilitate(valoare):
    return valoare * CONSTANTA_IMPERMEABILITATE


CONSTANTA_VITEZA_LUMINA = 299792458  # in metri pe secunda


def calculeaza_timpul_luminii(distanta):
    return distanta / CONSTANTA_VITEZA_LUMINA


CONSTANTA_PLANK = 6.62607015e-34  # in Joule*secunda


def calculeaza_energie(frecventa):
    return CONSTANTA_PLANK * frecventa


nume_locatie = "Bucuresti"


def calculeaza_distanta(locatie1, locatie2):
    return abs(locatie1 - locatie2)


nume_locatie2 = "Cluj"


def calculeaza_distanta2(locatie1, locatie2):
    return abs(locatie1 - locatie2)


nume_locatie3 = "Timisoara"


def calculeaza_distanta3(locatie1, locatie2):
    return abs(locatie1 - locatie2)
