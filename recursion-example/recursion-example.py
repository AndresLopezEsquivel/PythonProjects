# Andrés López Esquivel
# 05/06/2021
# Topic: Recursion

def factorial(number):
    """
    Calculates the factorial of a given number
    number int > 0
    return number!
    """
    try:
        if number <= 0:
            raise ValueError("Only positive integers are accepted.")
        else:
            if number == 1:
                return 1
            return number * factorial(number - 1)
    except ValueError as value_error_message:
        print(f"Error message: {value_error_message}")
        return "Error"


def run():
    
    try:
        number = int(input('Write a positive integer: '))
        print(f"The factorial of {number} is {factorial(number)}")
    except ValueError as value_error_message:
        print("Only integers are accepted.")
        print(f"Error message: {value_error_message}")

if __name__ == "__main__":
    run()