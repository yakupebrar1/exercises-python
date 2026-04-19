# favorites0.py
# Task: Print every student's favourite language using csv.reader

import csv

# Open favorites.csv for reading
# We use 'with' to ensure the file closes automatically
with open("../week1/favorites.csv", "r") as file:

    # Create a csv.reader object
    reader = csv.reader(file)

    # Skip the header row (Timestamp, language, problem)
    # next() moves the reader's internal pointer forward by one row
    next(reader)

    # Loop over the remaining rows
    for row in reader:
        # Since csv.reader returns a LIST, we access by index.
        # Index 0 is Timestamp, Index 1 is language.
        print(row[1])
