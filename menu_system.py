"""
Interactive Menu System
-----------------------
Author: Luis Henrique Carmanhan
Description: Performs mathematical operations via a dynamic interactive menu.
Features: Input validation, sleep delays, and clean exit logic.
"""


from time import sleep

# --- DATA INPUT ---
n1 = int(input('First value: '))
n2 = int(input('Second value: '))
option = 0

# --- INTERACTIVE MENU LOOP ---
while option != 5:
    print('''[ 1 ] Sum
    [ 2 ] Multiply
    [ 3 ] Higher
    [ 4 ] New numbers
    [ 5 ] Exit program''')
    
    option = int(input('>>>> What is your option?'))
    
    # Validation for options outside the scope [1-5]
    if option > 5 or option < 0: 
        print('Invalid operation')
        
    else:
        # --- OPERATION LOGIC ---
        if option == 1:
            result = n1 + n2 
            print(f'The sum between {n1} + {n2} is {result}')
        
        elif option == 2:
            result = n1 * n2 
            print(f'The result of {n1} x {n2} is {n1 * n2}')
            
        elif option == 3:
            # Check for the higher value between the two inputs
            if n1 > n2:
                higher = n1
            else:
                higher = n2 
            print(f'Between {n1} and {n2} the higher value is {higher}')
        elif option == 4:
            # Allows resetting the data without restarting the loop
            print('Inform the numbers again:')
            n1 = int(input('First value: '))
            n2 = int(input('Second value: '))
        elif option == 5:
            print('Finalizing...')
            sleep(1)
            
    print('=-=' * 10)   
            
 # --- TERMINATION ---           
print('End of the program. Thank you for choosing us!')
