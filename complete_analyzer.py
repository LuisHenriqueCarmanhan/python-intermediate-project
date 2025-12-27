"""
Complete Data Analyzer (Scalable Version)
----------------------------------------
Author: Luis Henrique Carmanhan
Description: Analyzes age and gender patterns within a group.
Features: Includes a dynamic participant count and logical filters.
"""

# --- SETUP & CONFIGURATION ---
# Prompt the user for the group size to ensure scalability
total_people = int(input('How many people do you want to list? '))

# Initialization of counters and accumulators
sum_age = 0
women_under_20 = 0
oldest_man_age = 0
oldest_man_name = ''

# --- DATA COLLECTION LOOP ---
# Iterate through the range defined by the user
for l in range(1, total_people + 1):
    print(f'----- {l}ª PERSON -----')
    name = str(input('Name: '))
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]:')).strip().upper()
    
    # Cumulative sum for the average age calculation
    sum_age += age

    # Logic: Identify the oldest male participant
    if gender == 'M':
        # Updates if it's the first loop iteration or if current age is a new record
        if l == 1 or age > oldest_man_age:
            oldest_man_age = age
            oldest_man_name = name
            
    # Logic: Filter females based on age criteria
    elif gender == 'F' and age <= 20:
        women_under_20 +=  1

# --- DATA PROCESSING ---
# Prevent division by zero if total_people is 0
if total_people > 0:
    average_age = sum_age / total_people

# --- FINAL REPORT ---
print('\n' + '='*30)
print(f'Average age of the group: {average_age:.1f} years.')
print(f'The oldest man is {oldest_man_name} with {oldest_man_age} years.')

# Conditional status based on analyzed data
if women_under_20 > 0:
    print(f'Total women under 20: {women_under_20}.')
    print(f'>>> Status: Leonardo DiCaprio would definitely call this group!')
else:
    print('No women under 20 found in this group.')
