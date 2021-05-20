# Looking for numbers in common in both files (file1.txt and file2.txt)

with open("file1.txt") as file1:
  numbers_list = file1.readlines()
  list1 = [int(number.strip()) for number in numbers_list]

with open("file2.txt") as file2:
  numbers_list = file2.readlines()
  list2 = [int(number.strip()) for number in numbers_list]

new_list = [number for number in list1 if number in list2]

print(new_list)
