def get_integer_input():
  """Gets an integer from the user."""
  while True:
    try:
      user_input = input("Enter an integer: ")
      number = int(user_input)
      return number
    except ValueError:
      print("That's not a whole number. Try again.")

def check_even_odd(number):
  """Checks if a number is even or odd and returns a message."""
  if number % 2 == 0:
    message = str(number) + " is an Even number."
  else:
    message = str(number) + " is an Odd number."
  return message

def main():
  """Main part of the program."""
  the_number = get_integer_input()
  result = check_even_odd(the_number)
  print(result)

if __name__ == "__main__":
  main()