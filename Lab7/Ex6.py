weird_tuple = ("hello", 10, "goodbye", 3, "goodnight", 5)
try:
	weird_tuple.append(input("Enter a value to append: "))
except AttributeError as error:
	print(f"An attempt was made to append a value to the tuple, but it failed: {error}")
