# Ask the user for a number between 1 and 100.  Square the number and print the number and its square.
# Name: Rick Kazman
# Date: Jan. 20, 2026

print("Welcome to the program")
valueUserEntered = input("Please enter a number between 1 and 100: ")
print("You entered:", valueUserEntered)

value_as_integer = int(valueUserEntered)
squared_value = value_as_integer ** 2
#print("The square of", value_as_integer, "is", squared_value)
print(f"The square of {value_as_integer} is {squared_value}")
