"""
Fibonacci Sequence v1.0
-----------------------
Author: Luis Henrique Carmanhan
Description: Generates the Fibonacci sequence based on the number of terms requested.
Features: Sequential logic, variable swapping, and clean output formatting.
"""

print('-' * 30)
print('Fibonacci Sequence')
print('-' * 30)

# Defines how many elements the user wants to see
n = int(input('How many terms do you want to show? '))

# Fibonacci starts with 0 and 1
t1 = 0
t2 = 1

# Counter starts at 3 because we already printed the first two terms
count = 3

print(f'{t1} -> {t2}', end='')

# Loop: calculates the next term as the sum of the previous two
while count <= n:
     t3 = t1 + t2 
     print(f' -> {t3}', end='')
     
     # Logic: moves the values forward to calculate the next step
     t1 = t2 
     t2 = t3 
     count += 1 


print(' -> END')
print('~' * 30)



