nume_utilizator = input("Introduceti numele utilizatorului: ")
print(nume_utilizator[0])
print(nume_utilizator[-1])
print(nume_utilizator[-2])
print(nume_utilizator[-3])

for litere in nume_utilizator:
    print(f"Litera este : {litere}")
    
    
print(f"Lungimea numelui este: {len(nume_utilizator)}")

print(nume_utilizator[:4])
print(nume_utilizator[:5])
print(nume_utilizator[4:])
print(nume_utilizator[5:])
print(nume_utilizator[2:6])
print(nume_utilizator[-3:])
print("Alin este cel mai bun programator din toate timpurile")
print(nume_utilizator[-7::3])
