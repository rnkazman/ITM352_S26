# Create a dataframe from individual lists.
# Do some simple statistics on the data.
import pandas as pd

# Lists of individuals' ages, names, and genders
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]
names = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

# Create a dictionary from the lists of ages and genders
raw_data = zip(ages, gender)

# Create a DataFrame from the data, with names as index, specifying column names.
df = pd.DataFrame(raw_data, index=names, columns=["Age", "Gender"])
print(df)

summary = df.describe()
print(summary)

# Calculate average age by gender
average_age_by_gender = df.groupby("Gender")["Age"].mean()
print("\nAverage age by gender: \n", average_age_by_gender)
