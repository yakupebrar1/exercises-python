# favorites1.py
# Task: Store the language in a variable to make the code self-documenting.

import csv

with open("favorites.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        # Store row[1] in a variable called 'favorite'
        # This makes it clear that index 1 represents the user's choice
        favorite = row[1]

        # Print favorite
        print(favorite)
