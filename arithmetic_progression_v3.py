"""
Super Arithmetic Progression v3.0
---------------------------------
Author: Luis Henrique Carmanhan
Description: An AP generator that allows the user to extend the sequence dynamically.
Features: Nested loops, cumulative counters, and interactive flow control.
"""

print('PA GENERATOR')
print('-=' * 10) 

# Initial user inputs for the sequence start and its common difference
first_term = int(input('First term: '))
q = int(input('Difference:'))

# Counters to track the position in the sequence and the total terms shown
count = 1
total_terms = 0
extra_terms = 10

# Main loop: continues as long as the user requests more terms (not 0)
while extra_terms != 0:
    # Updates the total number of terms to be displayed in the current run
    total_terms  += extra_terms
    
    # Internal loop: calculates and displays each term of the AP
    while count <= total_terms:
        print(f'{first_term} -> ', end='')
        first_term += q
        count += 1
    print('PAUSED')
    
    # Interaction: asks if the user wants to keep the program running
    cont = str(input('Do you want to continue? [Y/N]')).strip().upper()
    
    if cont == 'Y':   
    # If yes, asks for the number of additional terms for the next batch
     extra_terms = int(input('How many more terms do you want to show?'))
    else:
        # If no (or any other key), forces the main loop to stop immediately 
        break

    
    # Final report displayed when the user exits the loop by typing 0   
print(f'Progress finished with {total_terms} terms displayed.')    