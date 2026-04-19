# favorites3.py
# Task: Print directly using DictReader for a more compact script.

import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["language"])
