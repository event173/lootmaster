import random

# Start the main loop

loot_tables = {
    'easy': {
        'common': ['potion of healing', '50 gold coins', 'scroll of protection', 'cloak of elvenkind'],
        'uncommon': ['magic amulet', 'scroll of fireball', 'boots of stealth'],
    },
    'medium': {
        'common': ['100 gold coins', 'greater potion of healing', 'dagger of venom'],
        'uncommon': ['+1 weapon', 'scroll of invisibility', 'wand of magic missiles'],
        'rare': ['ring of protection', 'cloak of displacement'],
    },
    'hard': {
        'common': ['200 gold coins', 'potion of superior healing'],
        'uncommon': ['+2 weapon', 'scroll of resurrection', 'boots of levitation'],
        'rare': ['amulet of health', 'staff of power'],
        'legendary': ['vorpal sword', 'ring of three wishes'],
    }
}

def generate_loot(difficulty, roll, rarity=None):
    
    # Simplified selection logic based on difficulty
    loot_options = loot_tables[difficulty]
    loot_generated = []
    
    # If rarity is directly provided, use it
    if rarity:
        final_rarity = rarity
    else:
        # Randomly select a rarity based on encounter difficulty
        initial_rarity = random.choice(list(loot_options.keys()))
        print(f"Initial rarity: {initial_rarity}")
        
        final_rarity = initial_rarity
        if roll > 15:  # If roll is greater than 15, increase the rarity
            rarity_order = ['common', 'uncommon', 'rare', 'legendary']
            # Rest of your code...

# Rest of your code...
            current_index = rarity_order.index(initial_rarity)
            if current_index < len(rarity_order) - 1:  # If not already at the highest rarity
                final_rarity = rarity_order[current_index + 1]
    
    print(f"Final rarity after considering the roll: {final_rarity}")
    
    item = random.choice(loot_options[final_rarity])
    
    loot_generated.append(item)
    return loot_generated

difficulty_mapping = {
    1: 'easy',
    2: 'medium',
    3: 'hard'
}
yesno_mapping = {
    1: "yes",
    2: "no"
}
rarity_mapping = {
    1: "common",
    2: "uncommon",
    3: "rare",
    4: "legendary"
}

while True:

    # Ask the user for the difficulty and party level
    use_difficulty = int(input("Do you want to use difficulty?\n (1) yes (2) no): "))
    use_difficulty = yesno_mapping[use_difficulty]
    rarity = None
    if use_difficulty.lower() == 'yes':
        difficulty = int(input("Enter difficulty \n (1)easy (2)medium (3)hard: "))
        difficulty = difficulty_mapping[difficulty]
    else:
        rarity = int(input("Enter rarity \n (1)common (2)uncommon (3)rare (4)legendary): "))
        rarity = rarity_mapping[rarity]
        difficulty = 'medium' # Default to medium difficulty
    

    roll = None
    use_roll = int(input("Do you want to roll?\n (1)yes (2)no): "))
    use_roll = yesno_mapping[use_roll]
    if use_roll.lower() == 'yes':
        roll = int(input("Enter roll: "))

    # Example of generating loot for a medium difficulty encounter
    loot = generate_loot(difficulty, roll, rarity=rarity if use_difficulty.lower() == 'no' else None)
    print("Loot generated:", loot)

    # Ask the user if they want to quit
    quit = input("Enter 'q' or 'exit' to quit, or any other key to continue: ")
    if quit.lower() in ['q', 'exit']:
        break