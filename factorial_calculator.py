"""
Factorial Calculator
--------------------
Author: Luis Henrique Carmanhan
Description: Calculates the factorial of a number using a while loop.
Features: Mathematical logic, clean formatting, and step-by-step visualization.
"""

from time import sleep

# ANSI color codes for terminal styling
cyan = '\033[36m'
reset = '\033[0m'

print(f'{cyan}--- FACTORIAL CALCULATOR ---{reset}')

# User input: defines the starting number for the factorial calculation
c = (int(input('Enter a number to calculate its factorial: ')))

# Accumulator variable: initialized at 1 as it will be used for multiplication
f = 1

print(f'Calculating {c}! = ', end='')

# Main loop: runs as long as the counter is greater than zero
while c > 0:
    # Displays the current number in the sequence
    print(f'{c}', end='')
    
    # Conditional string formatting: prints 'x' between numbers and '=' at the end
    print(f'x' if c > 1 else '=', end='')
    
    # Logic: multiplies the accumulator by the current counter value
    f *= c 
    
    # Decrement: reduces the counter by 1 for the next iteration
    c -= 1
    
    # UX: small delay to create a sequential calculation effect in the terminal
    sleep(0.1)
    
 # Final result output
print(f'{f}')
print(f'{cyan}--- Calculation Complete ---{reset}')
    