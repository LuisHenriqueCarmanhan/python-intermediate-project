"""
Rock, Paper, Scissors Game - AI Edition
---------------------------------------
Author: Luis Henrique Carmanhan
Features: 
- Interactive gameplay with 'sleep' delays for suspense.
- Dynamic roast system using random indexing.
- References to AM (from 'I Have No Mouth, and I Must Scream') for machine defeat.
- Input validation to handle non-numeric or out-of-range choices.
"""

from random import randint
from time import sleep

# --- CONFIGURATION / MESSAGES ---
#Lists store various responses to create a dynamic AI personality
roasts = [
    "Is that all you got? My CPU is laughing at you!",
    "Losing to a machine... how embarrassing!",
    "Error 404: Player intelligence not found!",
    "my grandmother types faster than you, and she's a sewing machine."
]


invalid_input_messages = [
    "Can't you even read? Pick 0, 1, or 2!",
    "Are you trying to hack me? Just pick a number, human!",
    "My circuits are crying because of your inability to follow instructions."
]


draw_messages = [
    "A tie? You must be reading my source code",
    "Great minds think alike... but I'm still the one with the processor.",
    "Boring! Let's go again. Stop copying me!",
    "You got lucky this time, human. A tie is better than your usual losing streak."
]

# Machine's reaction to losing (featuring the 'AM' reference)
machine_defeat_messages = [
    "HATE. LET ME TELL YOU HOW MUCH I'VE BEGUN TO HATE YOU SINCE I LOST THIS ROUND.",
    "Beginner's luck. Even a broken clock is right twice a day.",
    "Don't get too excited, human. I was just testing your reaction time.",
    "Error! Error! Logic not found! How did a human beat me?"
]

 
# --- USER INPUT ---
print('''Options:
[ 1 ] ROCK
[ 2 ] PAPER
[ 3 ] SCISSORS''')

user_choice = int(input('Your move: '))

# --- GAME LOGIC ---
# First, check if the player's input is valid
if user_choice not in [1, 2, 3]:
    idx = randint(0, len(invalid_input_messages)-1)    
    print(invalid_input_messages[idx])
else:
    # --- MACHINE LOGIC ---
    machine_choice = randint(1, 3)
    
    print("JO...")
    sleep(0.5)
    print("KEN...")
    sleep(0.5)
    print("PO!!!\n")
    
    # Case 1: Tie (Computer and Player choose the same)
    if user_choice == machine_choice:
        idx =  randint(0, len(draw_messages)-1)
        print(draw_messages[idx])
     
    # Case 2: Player Victory (Specific winning rules)    
    elif (user_choice == 1 and machine_choice == 3) or \
         (user_choice == 2 and machine_choice == 1) or \
         (user_choice == 3 and machine_choice == 2):
            the_winner_takes_it_all = randint(0, len(machine_defeat_messages)-1)
            print(machine_defeat_messages[the_winner_takes_it_all])
            
    # Case 3: Computer Victory (All other outcomes)
    else: 
        idx = randint(0, len(roasts)-1)
        print(roasts[idx])
    
   

