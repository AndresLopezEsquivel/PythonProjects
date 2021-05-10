# Andrés López Esquivel
# 05/02/2021
# Project: Hangman

import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)

print(logo)

current_list = []

for _ in range(len(chosen_word)): current_list.append('_')

end_of_game = False

lives = -1 

message = ""

picture = ""

while not end_of_game:

  guess = input('Enter a letter.\n').lower()

  if guess in chosen_word:
    for position in range(len(chosen_word)):
      if guess == chosen_word[position]:
        current_list[position] = guess
  else:
    lives -= 1

  if '_' not in current_list:
    end_of_game = True
    message = "won"
  
  if lives == -len(stages):
    end_of_game = True
    message = "lost"

  print("".join(current_list))

  print(f"lives: {len(stages) + lives}")

  print(stages[lives])

print(f'You {message}.')