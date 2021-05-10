import random

# Functions

def deal_card():
	""" Returns a random card from the deck """
	# A = 11
	# J = Q = K = 10
	# We are going to assume that the deck is infinite

	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

	return random.choice(cards)

def calculate_score(list_cards):
	""" Calculates current score for a given list of cards """

	if sum(list_cards) == 21:

		return 0


	if sum(list_cards) > 21 and 11 in list_cards:

		list_cards.remove(11)

		list.cards.append(1)

	return sum(list_cards)

def define_winner():
	"""Inidicates who wins the game"""

	print(f'Your cards: {participant_cards}. Total score: {sum(participant_cards)}')

	print(f'Dealer\'s cards: {dealer_cards}. Total score: {sum(dealer_cards)}')

	

	
	elif sum(participant_cards) > 21:

		print('You went over 21. You lose. :(')

	elif sum(participant_cards) > sum(dealer_cards):

		print('You win. :)')

	else:

		print('Dealer wins. :(')


# Initially, the dealer and the participant are randomly given two cards. 

participant_cards = []

dealer_cards = []

give_another_card = True

for _ in range(2):

	participant_cards.append(deal_card())

	dealer_cards.append(deal_card())

print(f'Your cards: {participant_cards}. Total score: {sum(participant_cards)}')

print(f'Dealer\'s first card: {dealer_cards[0]}.')

while give_another_card:

	choice = input("Type either 'y' if you want another card or 'n' if you don't.")

	if choice == 'y':

		print('Typed yes')

	else:

		give_another_card = False

		define_winner()

