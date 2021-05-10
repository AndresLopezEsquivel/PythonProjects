# Andrés López Esquivel
# 05/04/2021
# Project: Caesar Chipher

list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

def caesar_cipher(type,word,shift):

  if type == 1 or type == 2:

    list_2 = list_1.copy()

    result = ""

    final_shift = 0

    if shift > (len(list_1) - 1):

      if (shift % (len(list_1) - 1)) == 0:

        final_shift = len(list_1) - 1

      else:

        final_shift = shift % (len(list_1) - 1)

    else:

      final_shift = shift

    for i in range(len(list_1)):
      list_2[i - final_shift] = list_1[i]

    if type == 1:

      for j in word:
        result += list_2[list_1.index(j)]

      print(f'Plain text: {word}')
      print(f'Encrypted word: {result}')

    else:
      
      for j in word:
        result += list_1[list_2.index(j)]

      print(f'Encrypted word: {word}')
      print(f'Plain text: {result}')

  else:

    print('Invalid option.')


choice = int(input('Enter 1 to encrypt or 2 to decrypt. \n'))

word = input('Word to encrypt: \n').lower()

shift = int(input('Shift: \n'))

caesar_cipher(choice, word, shift)