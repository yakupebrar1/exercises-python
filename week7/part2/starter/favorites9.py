# favorites9.py
# Task: Count languages using SQL instead of a Python dictionary.

from cs50 import SQL

# Open the database (ensure favorites.db exists in your directory)
db = SQL("sqlite:///favorites.db")

# Execute the SQL query
# 1. COUNT(*) AS n: Counts occurrences and renames the result column to 'n'
# 2. GROUP BY language: Collapses all identical languages into single rows
# 3. ORDER BY n DESC: Sorts the resulting counts from highest to lowest
rows = db.execute("SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC")

# Loop over rows and print the results
# db.execute returns a list of dictionaries, where keys are column names
for row in rows:
    print(f"{row['language']} {row['n']}")
