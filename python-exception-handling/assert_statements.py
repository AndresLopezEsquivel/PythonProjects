# Andrés López Esquivel
# 23/06/2021
# Assert statements


def divisors(number):
    divisors = []
    assert number > 0, "Only positive integers are accepted."
    divisors = [k for k in range(1, number + 1) if number % k == 0]
    return divisors


def run():
    number = input("Please, enter a number: ")
    assert number.isnumeric(), "Only integers are accepted."
    print(f"Its divisors are: {divisors(int(number))}")


if __name__ == "__main__":
    run()