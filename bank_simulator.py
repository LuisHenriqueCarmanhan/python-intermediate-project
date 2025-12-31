
cheapest_name = ""
lowest_price = 0
balance = 1000

while True:
    print('\n' + '=' * 30)
    print('=' * 30)
    print('1 - Register Shopping (Debit Card)')
    print('2 - ATM Withdrawal ')
    print('3 - Deposit Money')
    print('4 - View Balance')
    print('5 - Exit')
    print('-' * 30)

    option = int(input('Choose an option: '))
     
    # --- OPTION 1: SHOPPING ANALYZER (Former Ex 70) ---   
    if option == 1:
        print(f"\n{' SHOPPING MODE ':-^30}")
        current_session_spent = 0
        
        while True:
            product = str(input('Product Name: ')).strip().capitalize()
            price = float(input('Price: $ '))
            
            if price <= balance:
                balance -= price
                current_session_spent += price
                print(f"Purchased! Item added to session.")
                
                if cheapest_name == "" or price < lowest_price:
                    lowest_price = price
                    cheapest_name = product
            else:
                print(">>> TRANSACTION DENIED: Insufficient balance!")
            
            choice = ' '
            while choice not in 'YN':
                choice = str(input('Add another item? [Y/N]: ')).upper().strip()[0]
            if choice == 'N':
                break
        print(f"Total spent in this session: ${current_session_spent:.2f}")

# --- OPTION 2: ATM WITHDRAWAL ---
    elif option == 2:
        print(f"\n{' ATM WITHDRAWAL ':-^30}")
        print(f"Available Balance: ${balance:.2f}")
        
        withdrawal_value = float(input('Withdrawal amount: R$ '))
        
        if withdrawal_value <= balance: 
            balance -= withdrawal_value 
            
            amount_to_process = withdrawal_value
            bill = 100       
            total_bills = 0  
            
            while True:
                if amount_to_process >= bill:
                    amount_to_process -= bill
                    total_bills += 1
                else:
                    if total_bills > 0:
                        print(f'Total of {total_bills} bills/coins of R$ {bill:.2f}')
                        
                    if bill == 100: bill = 50
                    elif bill == 50: bill = 20
                    elif bill == 20: bill = 10
                    elif bill == 10: bill = 1
                    elif bill == 1: bill = 0.5
                    elif bill == 0.5: bill = 0.1
                    elif bill == 0.1: bill = 0.05
                    elif bill == 0.05: bill = 0.01
                    
                    total_bills = 0 
                    amount_to_process = round(amount_to_process, 2) 
                    
                    if amount_to_process == 0: 
                        break
            print(f">>> Withdrawal successful! New balance: ${balance:.2f}")
        else:
            print(">>> ERROR: Insufficient balance!")
            
    # --- OPTION 3: DEPOSIT ---
    elif option == 3:
        deposit = float(input('Enter deposit amount: $ '))
        if  deposit > 0:
            balance += deposit
            print(f'>>> Success! New balance: ${balance:.2f}')
            
    # --- OPTION 4: BALANCE & STATEMENT ---
    elif option == 4:
        print(f"\n{' ACCOUNT DETAILS ':-^30}")
        print(f"Current Balance: ${balance:.2f}")
        if cheapest_name != "":
            print(f"Last cheapest purchase: {cheapest_name} (${lowest_price:.2f})")
    
    elif option == 5:
        print("\nExiting system... Have a nice day!")
        break
             
print('=' * 30)
print('Transaction completed. Have a nice day!')