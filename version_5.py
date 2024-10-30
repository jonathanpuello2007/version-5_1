import random

magic_number = random.randint(1,100)
counter = 5
previous_guesses = []

print("Welcome to the Million dollar game.")
print("You will have 5 opportunities.")
print("Think carefully.")


while counter > 0:
  print("You previously guessed:")
  print(previous_guesses)
  user_guess = int(input("Guess a number between 1 and 100: "))
  previous_guesses.append(user_guess)

  if user_guess < magic_number:
    print("Your guess was too low:")
  elif user_guess > magic_number:
    print("Your guess was too high.")

  counter -= 1
 
