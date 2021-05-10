import random

number_attempts = 0

number_generated = random.randint(1,101)

choice = input("Choose difficulty: Type 'hard' or 'easy'. ").lower()

if choice == 'hard':

	number_attempts = 5

elif choice == 'easy':

	number_attempts = 10

print("I'm thinking of a number between 1 and 100")

while number_attempts > 0:

	print(f"You have {number_attempts} attempts remaining.")

	guess = int(input('Make a guess: '))

	if guess == number_generated:

		print("You've got it. Congratulations")

		number_attempts = 0

	elif guess > number_generated:

		print("Greater than the number that I'm thinking of.")

		number_attempts -= 1

	else:

		print("Lower than the number that I'm thinking of.")

		number_attempts -= 1

if guess != number_attempts:

	print("Try it the next time. ")

print(f"The answer was {number_generated}")

