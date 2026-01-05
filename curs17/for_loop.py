cene = [340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470]
for i in range(len(cene)):
    if cene[i] > 400:
        print(f"cene[{i}] = {cene[i]}")  # Print the index and value of cene
    else:
        print(f"cene[{i}] = {cene[i]} is not greater than 400")  
        # Print the index and value of cene
    
print(range(len(cene)))
print((len(cene)))

print(f"The length of cene is: {len(cene)}")    
print("The range of cene is: ", list(range(len(cene))))