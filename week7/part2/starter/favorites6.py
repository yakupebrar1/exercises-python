# favorites6.py
# Task: Count languages using EAFP (try/except) logic.

import csv

with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]

        try:
            # Try to increment the count assuming the key already exists
            counts[favorite] += 1
        except KeyError:
            # If the key doesn't exist, Python raises a KeyError.
            # We "catch" it and initialize the count to 1.
            counts[favorite] = 1

for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")
