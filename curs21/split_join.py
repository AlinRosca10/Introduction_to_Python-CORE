mesaj = "Astazi este o zi minunata"
mesaj_lista = mesaj.split()
print(mesaj_lista) 
# ['Astazi', 'este', 'o', 'zi', 'minunata']

print(" ".join(mesaj_lista))

my_string = "Welcome to Python course!"
print(my_string.lower())
print(my_string.upper())
print(my_string.capitalize())
print(my_string.title())
print(my_string.swapcase())
print(my_string.replace("Python", "Java"))
print(my_string.startswith("Welcome"))
print(my_string.endswith("!"))
print(my_string.find("."))

print(f"Python starts in my_string at position {my_string.find('Python')}")
data = my_string.split(" ")
for d in data:
    print(d)