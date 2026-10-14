celebs = ("Taylor Swift", "Cristiano Ronaldo", "The Weeknd", "Trevor Noah", "Dua Lipa")
ages = (36, 41, 36, 42, 31)

celebs_list = []
ages_list = []

for celeb in celebs:
    celebs_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"celebrities": celebs_list, "ages": ages_list}

print(celebs_dict)
