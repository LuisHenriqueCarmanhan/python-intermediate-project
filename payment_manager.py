"""
Payment Manager - Checkout System
---------------------------------
Author: Luis Henrique Carmanhan
Description: Calculates the final price of a product based on 
different payment methods and interest rates.
"""

print(f"{'Carmanhan s Store':=^40}")

# Get product price and convert to float for currency calculation
price = float(input('Price of the product: R$ '))

# Display the menu of payment options
print('''PAYMENT METHODS:
[ 1 ] Cash/Check (10% OFF)
[ 2 ] Credit Card - Full (5% OFF)
[ 3 ] Credit Card - 2x
[ 4 ] Credit Card - 3x up to 12x (20% Interest)
[ 5 ] Cancel order
''')

option = int(input('Choose an option: '))
# --- PROCESSING PAYMENT LOGIC ---

# Option 1: Cash/Check with 10% discount
if option == 1:
    print(f'You will pay: R$ {price - price*10/100:.2f}')
    print('Thank you for shopping with us! Come back soon.')
# Option 2: Credit card (single payment) with 5% discount
elif option == 2:
    print(f'You will pay: R$ {price - price*5/100:.2f}')
    print('Thank you for shopping with us! Come back soon.')
    
 # Option 3: Credit card divided in 2x (No interest)   
elif option == 3:
    value_per_installment = (price/2)
    print(f'You will pay R${price:.2f} in total, in  2 installments of R${value_per_installment:.2f}')
    print('Thank you for shopping with us! Come back soon.')

# Option 4: Installments from 3x to 12x with 20% interest (1/5 of price)
elif option == 4:
    total = (price * 1/5) + price
    installments = int(input('In how many installments would you like to pay?'))
    
    # LIMITER: Only proceed if installments are between 3 and 12
    if 3 <= installments <= 12:
        value_per_installment = total / installments
        print(f"You will pay R${total:.2f} in total, in {installments} installments of R${value_per_installment:.2f}")
        print('Thank you for shopping with us! Come back soon.')
    else:
        print(f"ERROR: {installments} installments is invalid. We only accept from 3 to 12. Transaction canceled.")
        
# Option 5: User-triggered cancellation  
elif option == 5:
    print('Transaction canceled')
    
 # Fallback for invalid numeric inputs   
else:
    print('Invalid command, please try again')

