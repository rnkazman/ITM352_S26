country_capitals = {
    "Germany": {"capital": "Berlin", "population": 3769495},
    "Canada": {"capital": "Ottawa", "population": 1017449},
    "England": {"capital": "London", "population": 8945310}}

print(country_capitals)

print(country_capitals["Canada"])
print(country_capitals["England"])

country_capitals["Italy"] = {"capital": "Rome", "population": 2761632}
print(country_capitals)

country_capitals["Italy"] = {"capital": "Milan", "population": 1378689}
print(country_capitals)

print("Germany" in country_capitals)
print("Spain" not in country_capitals)
print("Korea" in country_capitals)