# favorites2.py
# Task: Print every language using csv.DictReader

import csv

with open("favorites.csv", "r") as file:
    # Create a csv.DictReader object
    # This automatically uses the first row of the CSV as keys for the dictionary
    reader = csv.DictReader(file)

    # Loop over the rows (notice: no next() call is needed!)
    for row in reader:
        # Access the data by the column header name
        print(row["language"])
