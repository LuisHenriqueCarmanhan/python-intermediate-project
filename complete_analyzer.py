

total_people = int(input('How many people do you want to list? '))


sum_age = 0
women_under_20 = 0
oldest_man_age = 0
oldest_man_name = ''


for l in range(1, total_people + 1):
    print(f'----- {l}ª PERSON -----')
    name = str(input('Name: '))
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]:')).strip().upper()
    
    sum_age += age

    if gender == 'M':
        if l == 1 or age > oldest_man_age:
            oldest_man_age = age
            oldest_man_name = name
    
    elif gender == 'F' and age <= 20:
        women_under_20 +=  1
        
if total_people > 0:
    average_age = sum_age / total_people


print('\n' + '='*30)
print(f'Average age of the group: {average_age:.1f} years.')
print(f'The oldest man is {oldest_man_name} with {oldest_man_age} years.')

if women_under_20 > 0:
    print(f'Total women under 20: {women_under_20}.')
    print(f'>>> Status: Leonardo DiCaprio would definitely call this group!')
else:
    print('No women under 20 found in this group.')