# challenge4.py — SQL Explorer
# Interacting with favorites.db using SQL queries and parameterized inputs.

import sqlite3

def main():
    # Connect to the database
    db = sqlite3.connect("favorites.db")
    cursor = db.cursor()

    while True:
        print("\n=== SQL Explorer ===")
        print("1. Count by language")
        print("2. Count by problem")
        print("3. Search by problem name")
        print("4. Top 5 problems overall")
        print("5. Quit")

        choice = input("Choice: ")

        if choice == "1":
            # Count occurrences of each language
            rows = cursor.execute("SELECT language, COUNT(*) AS n FROM favorites GROUP BY language ORDER BY n DESC")
            for row in rows:
                print(f"{row[0]}: {row[1]}")

        elif choice == "2":
            # Count occurrences of each problem
            rows = cursor.execute("SELECT problem, COUNT(*) AS n FROM favorites GROUP BY problem ORDER BY n DESC")
            for row in rows:
                print(f"{row[0]}: {row[1]}")

        elif choice == "3":
            # Parameterized search to prevent SQL injection
            search = input("Enter problem name: ")
            # We use (search,) because the execute function expects a tuple for parameters
            rows = cursor.execute("SELECT language, COUNT(*) AS n FROM favorites WHERE problem = ? GROUP BY language", (search,))

            print(f"\nResults for '{search}':")
            for row in rows:
                print(f"{row[0]}: {row[1]}")

        elif choice == "4":
            # Use LIMIT to get the top 5
            rows = cursor.execute("SELECT problem, COUNT(*) AS n FROM favorites GROUP BY problem ORDER BY n DESC LIMIT 5")
            for row in rows:
                print(f"{row[0]}: {row[1]}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close the connection
    db.close()

if __name__ == "__main__":
    main()
