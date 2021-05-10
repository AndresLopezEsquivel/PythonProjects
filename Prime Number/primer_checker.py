def prime_checker(number):

  verification = True

  for i in range(2, number):
    if number % i == 0:
      verification = False
      break
  
  if verification:
    print(f"{number} is a prime number.")
  else:
    print(f"{number} is not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)