"""
Dynamic Data Statistics v1.0
----------------------------
Author: Luis Henrique Carmanhan
Description: Analyzes a series of numbers to calculate average, maximum, and minimum values.
Features: Dynamic comparison logic, infinite loops, and command-based interaction.
"""

# Initializing variables
# 'total_sum' and 'count' for the average calculation
# 'highest' and 'lowest' to store the extreme values
total_sum = count = highest = lowest = 0


while True:
    num = int(input('Enter a number: '))
    
    # Statistical updates
    total_sum += num 
    count += 1 
    
    # Logic for finding Maximum and Minimum values
    # In the first iteration (count == 1), the first number is both the highest and lowest
    if count == 1:
        highest = lowest = num
        
    else:
        # For subsequent numbers, we compare them with the current records
        if  highest < num:
            highest = num 
            
        if  lowest > num:
            lowest = num 

    # Interaction: Using professional command-based exit
    choice = str(input('Do you want to [continue] or [exit]? ')). strip().upper()
    
    if choice == 'EXIT':
        break

# Calculating the average  
average = total_sum / count

# Final statistical report
print('-=' * 20)
print(f'Processed {count} numbers.')
print(f'Average value: {average:.2f}')
print(f'Highest value recorded: {highest}')
print(f'Lowest value recorded: {lowest}')
print('-=' * 20)
print('--- Analysis Complete ---')


