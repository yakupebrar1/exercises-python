# Project 3 — Grade Calculator
# Author: Ebrar
# Date: April 13, 2026

scores = []

print("Please enter 5 test scores (0-100):")

# Use a for loop to collect 5 scores and append each to the list
for i in range(1, 6):
    score = float(input(f"Enter score {i}: "))
    scores.append(score)

# Calculate the average using sum() and len()
average = sum(scores) / len(scores)

# Determine the grade with if/elif/else (A/B/C/D/F)
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the average (1 decimal place) and the grade
print("-" * 25)
print(f"Average Score: {average:.1f}")
print(f"Final Grade: {grade}")
