import csv

# Configuration for validation
VALID_LANGUAGES = {"Python", "C", "Scratch", "SQL"}
SCORE_RANGE = range(1, 6) # 1 to 5

def clean_data():
    input_file = "messy_data.csv"
    output_file = "cleaned_data.csv"

    # Tracking for the final report
    report = {
        "total_rows": 0,
        "duplicates_removed": 0,
        "blanks_removed": 0,
        "invalid_scores_fixed": 0,
        "unknown_langs_flagged": 0,
        "cleaned_count": 0
    }

    seen_ids = set()
    cleaned_rows = []

    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                report["total_rows"] += 1

                # 1. Detect Blank Rows (Checking if ID or Name is missing)
                if not row["id"] or not row["name"]:
                    report["blanks_removed"] += 1
                    continue

                # 2. Detect Duplicate IDs
                student_id = row["id"]
                if student_id in seen_ids:
                    report["duplicates_removed"] += 1
                    continue
                seen_ids.add(student_id)

                # 3. Handle Out-of-Range Scores
                # We try to convert to int; if it fails or is out of range, we cap it
                try:
                    score = int(row["score"])
                    if score not in SCORE_RANGE:
                        # Logic: Cap the score to the nearest boundary
                        row["score"] = 5 if score > 5 else 1
                        report["invalid_scores_fixed"] += 1
                except ValueError:
                    row["score"] = 1 # Default for non-numeric junk
                    report["invalid_scores_fixed"] += 1

                # 4. Unknown Languages
                # We normalize case to catch 'python' vs 'Python'
                lang = row["language"].strip().capitalize()
                if lang not in VALID_LANGUAGES:
                    report["unknown_langs_flagged"] += 1
                    # We keep the data but could mark it as 'Other'
                    row["language"] = "Other"
                else:
                    row["language"] = lang

                cleaned_rows.append(row)
                report["cleaned_count"] += 1

        # Write the cleaned data
        with open(output_file, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "language", "score"])
            writer.writeheader()
            writer.writerows(cleaned_rows)

        # 5. Print Cleaning Report
        print_report(report)

    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please create it first!")

def print_report(r):
    print("\n=== Data Cleaning Report ===")
    print(f"Rows processed:      {r['total_rows']}")
    print(f"Blanks removed:      {r['blanks_removed']}")
    print(f"Duplicates removed:  {r['duplicates_removed']}")
    print(f"Scores corrected:    {r['invalid_scores_fixed']}")
    print(f"Languages set to 'Other': {r['unknown_langs_flagged']}")
    print("-" * 28)
    print(f"Cleaned rows saved:  {r['cleaned_count']}")
    print("Saved to cleaned_data.csv")

if __name__ == "__main__":
    clean_data()
