# First, let's ask the person for a number
print("Enter an integer:")
number_text = input()

# Now, let's turn that text into a real number
number = int(number_text)

# Let's see if the number is even or odd
if number % 2 == 0:
  # It's even!
  print(number, "is an Even number.")
else:
  # It's odd!
  print(number, "is an Odd number.")
