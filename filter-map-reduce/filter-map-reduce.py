# Andrés López Esquivel
# 06/22/2021
# Filter, map, reduce. Higher order functions

from functools import reduce

# FILTER

names = ["Andrew", "Alejandro", "Mike", "Omar", "Joseph", "Amanda"]

names_starting_with_a = list(filter(lambda name: name.lower()[0] == "a", names))

print("names_starting_with_a:", names_starting_with_a)

# MAP

names_lowercased = list(map(lambda name: name.lower(), names))

print("names_lowercased:", names_lowercased)

# REDUCE

names_with_commas = list(reduce(lambda string1, string2: f"{string1},{string2}", names))

print("names_with_commas: ", names_with_commas)
