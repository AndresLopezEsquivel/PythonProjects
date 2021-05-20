# Exercise 1:
# Use the given sentence and create a dictionary where each key represents
# each word of the sentence and each of their corresponding values to
# the numbers of letters in them

given_sentence = "You speak a very good japanese"
sentence = given_sentence.split()
words_dict = {word: len(word)for word in sentence}
print(words_dict)

# Exercise 2
# Use dictionary comprehension to create a new dictionary that takes the
# temperatures in Celsius from another dictionary and converts it to
# Fahrenheit scale.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: temp_c * (9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)