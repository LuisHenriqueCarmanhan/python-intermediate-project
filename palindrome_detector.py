"""
Palindrome Detector
-------------------
Author: Luis Henrique Carmanhan
Description: Analyzes a phrase to check if it reads the same backwards.
Features: String sanitization (removing spaces) and Pythonic slicing for inversion.
"""

# --- DATA INPUT & SANITIZATION ---
# Read input, remove leading/trailing spaces, and standardize to uppercase
phrase = str(input('Enter a phrase: ')).strip().upper()

# Split the phrase into a list of words to isolate internal spaces
words = phrase.split()

# Join the words back together with NO spaces ('') to create a solid string
joined_phrase = ''.join(words)

# --- STRING PROCESSING ---
# Use Pythonic slicing [start:stop:step] with a step of -1 to reverse the string
inverse_phrase = joined_phrase[::-1]

# Display the comparison process for user feedback
print(f'The inverse of {joined_phrase} is {inverse_phrase}')

# --- LOGICAL VERDICT ---
# Check if the sanitized string is identical to its inverse
if joined_phrase == inverse_phrase:
    print('Verdict: WE HAVE A PALINDROME!')
else:
    print('Verdict: Not a palindrome.')