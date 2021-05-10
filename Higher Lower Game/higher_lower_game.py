# Andrés López Esquivel
# 05/06/2021
# Project: Higher Lower Game

import random
from art import logo, vs
from game_data import data

def who_is_higher(A_data, B_data):

	if A_data['follower_count'] > B_data['follower_count']:

		return 'A'

	else:

		return 'B'

def information(dict):

	return f"{dict['name']}, a {dict['description']}, from {dict['country']}, {dict['follower_count']} followers"


def end_or_not_the_game(user_choice, A_data, B_data):

	correct_answer = who_is_higher(A_data, B_data)

	if user_choice == correct_answer:

		return False

	else: 

		return True

copy_data = data.copy()

score = 0

end_of_game = False

A = random.choice(copy_data)

copy_data.remove(A)

B = random.choice(copy_data)

copy_data.remove(B)

while not end_of_game:

	print(f'Current score: {score}')

	print(f'Compare A: {information(A)}.\n')

	print(vs)

	print(f'Against B: {information(B)}.\n')

	choice = input("Who has more followers? Type 'A' or 'B'. ").upper()

	end_of_game = end_or_not_the_game(choice, A, B)

	if not end_of_game:


		if len(copy_data) > 0:

			print('You got it.')

			score += 1

			A = B 

			B = random.choice(copy_data)

			copy_data.remove(B)

		else:

			print("You've finished the game. Congratulations")

			print(f"Final score {score}")

			end_of_game = True

	else:

		print(f'Wrong answer. Final score {score}')

		end_of_game = True