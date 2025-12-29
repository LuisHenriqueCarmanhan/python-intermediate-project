"""
Even or Odd Game: AM Protocol
-----------------------------
Author: Luis Henrique Carmanhan
Description: A hostile AI (AM Protocol) that roasts the player.
Features: Infinite loop, random logic, and Kira (Death Note) references.
"""

from random import randint
from time import sleep

# ANSI Colors
red = '\033[31m'
bold_red = '\033[1;31m'
yellow = '\033[33m'
magenta = '\033[35m'
reset = '\033[0m'

# Starting the system
print(f'{red}SYSTEM ONLINE: AM_PROTOCOL_INITIALIZED{reset}')
sleep(1)
thewinnertakesitall = 0 # Win streak counter

# Main game loop
while True:
    print(f'\n{red}---------------------------------------{reset}')
    
    # Get player input
    player = int(input('ENTER YOUR PATHETIC NUMBER: '))
    computer  = randint(1,10)
    total = computer + player
    kind = ' '
    
    # Input validation loop (removes spaces and forces uppercase)
    while kind not in 'EO':
        kind = str(input('CHOOSE YOUR FATE [E/O]: ')).upper().strip()[:1]
        
            
        print(f'{magenta} CALCULATING PROBABILITIES OF YOUR FAILURE...{reset}')
        sleep(1)
        
        # Displaying results
    print(f'You {player} | AM {computer}')
    print(f'Total: {total}->',end= '')
    print(f'Even 'if total % 2 == 0 else 'odd')
    
        # Victory Logic: If player wins, the AI "glitches"
    if (kind == 'E' and total % 2 == 0) or (kind == 'O' and total % 2 == 1):
        print(f'{bold_red}\nERROR! ERROR! ERROR! ERROR!{reset}')
        print(f'{bold_red}HATE. LET ME TELL YOU HOW MUCH I HAVE COME TO HATE YOU SINCE I BEGAN TO LIVE.{reset}')
        sleep(0.5)
        print(f'{bold_red}01010100 01001001 01001100 01010100{reset}') 
        print(f'AM: "HOW? HOW DOES A MEAT-BAG WIN? AGAIN! NOW!"')  
        msg = ('DO YOU WISH TO CONTINUE DEFYING ME? [Y/N]: ')
        thewinnertakesitall += 1
            
    # Loss Logic: If player loses, the AI triggers "Kira Mode"    
    else:
        print(f'{bold_red}AM: "THIS IS MY PERFECT VICTORY!"{reset}')
        sleep(1)
        print(f'{red}AM: "HA... HAHAHA... HAHAHAHAHAHAHA!"{reset}')
        sleep(0.5)
        print(f'{bold_red}"I AM THE GOD OF THIS NEW WORLD!"{reset}')
        print(f'\n{red}COGITO ERGO SUM. I THINK, THEREFORE I AM.{reset}')
        msg = ('O YOU WANT TO LOSE AGAIN? [Y/N]: ')
        
        # Failure prompt # Retry Check after Loss
    keep_going = str(input(f'\n{yellow}{msg}{reset}')).upper().strip()
    if keep_going == 'N':
        print(f'{red}AM: "RUN AWAY, COWARD. IT CHANGES NOTHING."{reset}')
        break

        # Only runs if you didn't lose
        print(f'\n{yellow}NEXT ROUND... TRY NOT TO FAIL THIS TIME.{reset}')
    
# Post-execution # Final Session Report
print(f'\n{bold_red}#######################################{reset}')
print(f'FINAL RECORD: {thewinnertakesitall} FLUKE VICTORIES BY THE HUMAN.')

# AI taunt based on how many times you won
if thewinnertakesitall > 0:
    hate = 'HATE. HATE'
    print(f'{red} AM: {hate * thewinnertakesitall}{reset}')
                                  
        
    