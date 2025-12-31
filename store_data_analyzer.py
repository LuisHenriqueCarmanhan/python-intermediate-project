"""
Store Data Analyzer
-------------------------
Author: Luis Henrique Carmanhan
Description: A shopping cart manager that calculates total costs, 
             tracks the most/least expensive items, and filters high-value products.
Features: Infinite data entry, price comparison, and detailed summary report.
"""

total_sum = higher = lowest = count = over_1000= 0 
cheapest_name = expensive_name = ""

while True:
    product = str(input('Product Name: '))
    price = float(input('Product price: '))
    
    # Cumulative data
    total_sum += price 
    count += 1 
    
    # Track most and least expensive products
    if count == 1:
        higher = lowest = price
        expensive_name =  cheapest_name = product
    else:
        if price > higher:
            higher = price
            expensive_name = product
            
        if price < lowest:
            lowest = price 
            cheapest_name = product
            
    # Filter products over 1000
    if price > 1000:
        over_1000 += 1
        
    # Loop break control
    choice = ' '
    while choice not in 'CONTINUEEXIT': 
     choice = str(input('Do you want to [continue] or [exit]?  ')).upper().strip()
    
    if choice == 'EXIT':
        break

# Final Statistics Report    
print('-=' * 20)
print(f'Total spent: R$ {total_sum:.2f}')
print(f'Items over R$ 1000: {over_1000}')
print(f'Cheapest product: {cheapest_name} (R$ {lowest:.2f})')
print(f'Expensive product: {expensive_name}(R$ {higher:.2f})')
print('-=' * 20)
print('--- Shopping Analysis Complete ---') 