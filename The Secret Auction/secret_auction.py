# Andrés López Esquivel
# 05/04/2021
# Project: The Secret Auction

participants = {}

def add_participant(name, bid):
	"""
	Add more participants to The Secret Auction
	"""
	participants[name] = bid


def define_winner():
	"""
	Determine the winner of The Secret Auction
	"""

	names = []

	bids = []

	winner = ""

	max_bid = 0

	for participant in participants:

		names.append(participant)

		bids.append(participants[participant])


	max_bid = max(bids)

	winner = names[bids.index(max_bid)]

	print(f"{winner} wins with a bid of ${max_bid}")

# The Secret Auction

end_of_game = False

print('Welcome to the Secret Auction. \n Start by defining the participants.')

while not end_of_game:

	name = input('Participant name: \n')

	bid = int(input('Bid: \n'))

	add_participant(name, bid)

	print('Would you like to add another participant? \n')

	choice = input('Yes or No \n').lower()

	if  choice != "yes":

		end_of_game = True

		define_winner()

