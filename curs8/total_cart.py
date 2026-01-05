num_10 = int(input("Enter a number of 10 cart: "))
num_20 = int(input("Enter a number of 20 cart: "))
num_50 = int(input("Enter a number of 50 cart: "))      
num_100 = int(input("Enter a number of 100 cart: "))
num_200 = int(input("Enter a number of 200 cart: "))
num_500 = int(input("Enter a number of 500 cart: "))

total_cash = (num_10 * 10) + (num_20 * 20) + (num_50 * 50) \
     + (num_100 * 100) + (num_200 * 200) + (num_500 * 500)
print(f"Total cash: {total_cash}")

total_cart = num_10 + num_20 + num_50 + num_100 + num_200 + num_500
# print(f"Total number of cart: {total_cart}")
print(f"Total number of cart: {total_cart}")