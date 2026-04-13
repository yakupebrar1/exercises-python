# Project 4 — Word Counter
# Author: Ebrar
# Date: April 13, 2026

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

# Total word count using len()
total_words = len(words)

# Character count (no spaces)
# sentence.replace(" ", "") removes all spaces, then we count what's left
char_count_no_spaces = len(sentence.replace(" ", ""))

# Word frequency dictionary
frequency = {}
for word in words:
    # If the word is already in the dictionary, increase its count
    if word in frequency:
        frequency[word] += 1
    # If it's a new word, add it to the dictionary with a count of 1
    else:
        frequency[word] = 1

# Print total words, total characters, then word frequency
print("\n--- Text Analysis ---")
print(f"Total Words: {total_words}")
print(f"Total Characters (excluding spaces): {char_count_no_spaces}")
print("\nWord Frequencies:")
for word, count in frequency.items():
    print(f"- {word}: {count}")
