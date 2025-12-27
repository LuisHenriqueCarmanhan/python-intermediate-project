"""
Prime Number Checker with Visual Feedback
-----------------------------------------
Author: Luis Henrique Carmanhan
Description: Verifies if a number is prime by checking its divisors.
Features: ANSI colors for terminal visualization and divisor counting.
"""

# --- DATA INPUT ---
# Input: Get user number for analysis
num = int(input('Enter a number: '))
total_divisors = 0

# --- CORE LOGIC ---
# Iterate from 1 to 'num' (inclusive) to check all possible divisors
for c in range(1,num + 1):
    
   # Check if 'num' is divisible by 'c' without remainder
    if num % c == 0:
        # Yellow color for divisors
        print('\033[33m', end='') 
        total_divisors += 1    # Shorthand for: total_divisors = total_divisors + 1
        
    else:
        # Red color for non-divisors
        print('\033[31m', end='') 
    
    # Print current iteration number in the assigned color    
    print(f'{c}', end=' ', )
    
# Reset terminal color formatting back to default
print('\033[m')

# --- RESULTS OUTPUT ---
print(f'The number {num} was divisible {total_divisors} times.')

# Definition of a prime number: must be divisible exactly by two numbers (1 and itself)
if total_divisors == 2:
    print('RESULT: This IS a PRIME number!')
    
else:
    print("RESULT: This is NOT a PRIME number!")  