"""
Multiplication Table v3.0
-------------------------
Author: Luis Henrique Carmanhan
Description: Generates automated tables for any number. 
             Stops when a negative value is entered.
Features: Infinite loop, input-based termination, and formatted output.
"""

while True:
    print('-'* 40)
    num = int(input('Which number do you want to see the table for?'))
    
    # Automation: Using 'for' to generate values from 1 to 10
    for c in range(1,11):
        print(f'{num} x {c:2} = {num * c}')  
    
    choice = str(input('Do you want to [continue] or [exit]? ')).upper().strip()
    
    if choice == 'EXIT':
        break
    
    
print('PROGRAM TERMINATED. Come back soon!')