# Ask the user to enter their birth year.  Calculate their
# age based on the current year (2026) and print it out.
# Name: Rick Kazman
# Date: Jan. 20, 2026

birth_year = input("Please enter your birth year: ")
birth_year_int = int(birth_year)
current_year = 2026
age = current_year - birth_year_int
print("You entered:", birth_year)
print(f"You are {age} years old.")