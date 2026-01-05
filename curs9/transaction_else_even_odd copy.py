transaction = int(input("Enter transaction number: "))
if transaction % 2 == 0:
    print("Transaction is even")
else:
    # This is the else block
    print("Transaction is odd")

print("Good bye")

if (not (transaction % 2 == 0)):
    print("Transaction is odd")
    print("Good bye!!!")

# The above code is a simple program that checks if a transaction number is 
# even or odd.
if transaction % 3 == 0:
    print("Remainder is 0")
elif transaction % 3 == 1:
    print("Remainder is 1")
else:
    # This is the else block
    print("Remainder is 2")
# The above code is a simple program that checks the remainder of a 
# transaction number when divided by 3.
