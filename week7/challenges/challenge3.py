# challenge3.py — CSV Writer
# Read favorites.csv, calculate percentages, and write to language_summary.csv

import csv

counts = {}
total_votes = 0

# 1. Read and count
with open("../week1/favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        lang = row["language"]
        counts[lang] = counts.get(lang, 0) + 1
        total_votes += 1

# 2. Prepare the new file for writing
# We use 'w' mode to create/overwrite the file
with open("language_summary.csv", "w", newline="") as file:
    # Define the headers
    fieldnames = ["language", "votes", "percentage"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # 3. Sort by votes descending and write the data
    for lang in sorted(counts, key=counts.get, reverse=True):
        votes = counts[lang]

        # Calculate percentage: (part / total) * 100
        # Rounded to 2 decimal places
        percentage = round((votes / total_votes) * 100, 2)

        # Write the row as a dictionary
        writer.writerow({
            "language": lang,
            "votes": votes,
            "percentage": percentage
        })

print("Saved to language_summary.csv")
