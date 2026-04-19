# favorites10.py
# Task: Search for a problem count using parameterized SQL.

from cs50 import SQL

# Open the database
db = SQL("sqlite:///favorites.db")

# 1. Ask the user for their favourite problem
favorite = input("Favorite: ")

# 2. Execute a SQL query using a '?' placeholder
# The 'favorite' variable is passed as a separate argument to be safely sanitized
rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?", favorite)

# 3. Get the first (and only) row from the result list
row = rows[0]

# 4. Print the count
print(row["n"])
