# favorites5.py
# Task: Count languages dynamically using a dictionary.

import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)

    counts = {}  # Dictionary to store language -> count

    for row in reader:
        favorite = row["language"]

        # If favorite is already in counts, increment by 1
        if favorite in counts:
            counts[favorite] += 1
        # Otherwise, initialize the count at 1
        else:
            counts[favorite] = 1

    # Print each key-value pair in counts
    for language in counts:
        print(f"{language}: {counts[language]}")
