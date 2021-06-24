# Andrés López Esquivel
# 23/06/2021
# Exception handling in Python


def divisors(number):
    divisors = []
    try:
        if number < 0:
            raise ValueError("Only positive integers are accepted.")
        divisors = [k for k in range(1, number + 1) if number % k == 0]
    except ValueError as value_error_message:
        print(value_error_message)
    finally:
        return divisors


def run():
    try:
        number = int(input("Please, enter a number: "))
        print(f"Its divisors are: {divisors(number)}")
    except ValueError as value_error_message:
        print("Only integers are accepted.")
        print(f"Error message: {value_error_message}")


if __name__ == "__main__":
    run()