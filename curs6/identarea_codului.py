def add(a, b):
    return a + b    # return the sum of a and b


def multiply(a, b):
    return a * b    # return the product of a and b


def calculate_sum_upto(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total    # return the sum from 1 to n


# return two sums calculated with different continuations
def calculate_sum_with_continuation():
    sum1 = 1 + 2 + 3 + 4 + 5 + 6 + \
           7 + 8 + 9 + 10
    sum2 = (1 + 2 + 3 + 4 + 5 + 6 +
            7 + 8 + 9 + 10)
    return sum1, sum2


def calculate_large_sum():
    num = (50 + 100 + 150 + 200 + 250 + 300 + 500 + 550 + 600 + 650 +
           700 + 750 + 800 + 850 + 900 + 950 + 1000)
    return num


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Sum of numbers is: {add(a, b)}")
print(f"Result is: {multiply(a, b)}")
n = 10
print(f"Result is: {calculate_sum_upto(n)}")
sum1, sum2 = calculate_sum_with_continuation()
print(f"Result is: {sum1}")
print(f"Result is: {sum2}")
large_sum = calculate_large_sum()
print(f"Sum is: {large_sum}")

x = 5
y = 3
z = x + y
print(f"Sum of numbers is: {z}")