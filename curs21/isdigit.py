cod = "123456"
print("Your code is: ", cod)
is_digital = cod.isdigit()
print("Is your code digital?", is_digital)
if is_digital:
    print("Thank you!")
else:
    print("Please enter digits only.")
    
nume = "Alina90"
is_letter = nume.isalpha()
print("Is your name a letter?", is_letter)
is_alnum = nume.isalnum()
print("Is your name alphanumeric?", is_alnum)
if is_alnum:
    print("Thank you!")
else:
    print("Please enter letters and numbers only.")
    
text = "Python este distractiv"


if text.startswith("Python") and text.endswith("distractiv"):
    print("Textul incepe cu Python si se termina cu distractiv")
else:
    print("Textul nu incepe cu Python si nu se termina cu distractiv")

