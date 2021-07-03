# Andrés López Esquivel
# 03/07/2021
# Example of exhaustive enumeration algorithm

number = int(input("Enter a number to check if it has an exact square root: "))
sqrt_attempt = 0

while sqrt_attempt**2 < number:
    sqrt_attempt += 1

if sqrt_attempt**2 == number:
    print(f"{number} has an exact square root, which is: {sqrt_attempt}.")
else:
    print(f"{number} doesn't have an exact square root.")