# favorites8.py
# Task: Print language counts sorted by POPULARITY (most popular first)

import csv

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

# We pass the 'get' method of our dictionary to the sorted function.
# reverse=True ensures the largest numbers come first.
for favorite in sorted(counts, key=counts.get, reverse=True):
    print(f"{favorite}: {counts[favorite]}")
