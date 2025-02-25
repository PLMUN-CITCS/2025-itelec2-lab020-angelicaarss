print("Enter an integer:")
user_input = input()

# Let's try to turn it into a number
try:
  number = int(user_input)

  # Now, check if it's even or odd
  if number % 2 == 0:
    print(number, "is an Even number.")
  else:
    print(number, "is an Odd number.")

# If they didn't type a number...
except:
  print("That's not a number! Try again.")
