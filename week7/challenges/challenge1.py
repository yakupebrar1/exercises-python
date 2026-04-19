# challenge1.py — Frequency Filter
# Read favorites.csv, ask for a minimum vote count, print filtered results.

import csv

# Dictionary to keep track of language vote counts
counts = {}

# 1. Read the CSV file and count the languages
with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Assuming the column is named 'language' in the CSV header.
        # Adjust to 'Language' or whatever matches your CSV exact headers if needed.
        lang = row["language"]

        # Tally the votes
        if lang in counts:
            counts[lang] += 1
        else:
            counts[lang] = 1

# 2. Ask the user for the minimum votes threshold
# int() converts the string input into a number so we can do math comparisons
min_votes = int(input("Minimum votes to display: "))

# 3. Sort the languages by count descending and print the filtered results
# key=counts.get tells Python to sort the keys based on their dictionary values
# reverse=True ensures it sorts from highest to lowest
for lang in sorted(counts, key=counts.get, reverse=True):
    if counts[lang] >= min_votes:
        print(f"{lang}: {counts[lang]}")
