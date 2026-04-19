# challenge2.py — Two-Column Report
# Read favorites.csv, calculate the most common problem per language, and print a formatted table.

import csv

# Nested dictionary to hold counts: {language: {problem: count}}
counts = {}

# 1. Read the CSV file and populate the nested dictionary
with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract the relevant columns
        lang = row["language"]
        problem = row["problem"]

        # If language isn't in our dictionary yet, initialize it with an empty dictionary
        if lang not in counts:
            counts[lang] = {}

        # If the problem isn't in that language's inner dictionary yet, start its count
        if problem not in counts[lang]:
            counts[lang][problem] = 0

        # Increment the count for this specific problem under this specific language
        counts[lang][problem] += 1

# 2. Print the table header
print("Language   | Most Common Problem")
print("-----------+--------------------")

# 3. Find the most common problem for each language and print the rows
# Sorting the keys (languages) alphabetically to keep the output organized
for lang in sorted(counts):

    # max() finds the highest key in the inner dictionary based on its numeric value
    best_problem = max(counts[lang], key=counts[lang].get)

    # Print using an f-string
    # The <10 ensures the language name takes up exactly 10 spaces and is left-aligned
    print(f"{lang:<10} | {best_problem}")
