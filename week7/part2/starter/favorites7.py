# favorites7.py
# Task: Print language counts sorted ALPHABETICALLY (A → Z)

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

# sorted(counts) creates a temporary list of keys: ["C", "Python", "Scratch"]
for favorite in sorted(counts):
    print(f"{favorite}: {counts[favorite]}")
