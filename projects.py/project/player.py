import random

player_gold = 150
chest_cost = 30
chests_opened = 0

def get_player_gold():
    return player_gold

def get_chest_cost():
    return chest_cost

def get_chests_opened():
    return chests_opened

def calculate_loot_chance():
    return random.randint(1, 100)

def determine_loot(loot_chance):
    if loot_chance < 3:
        return 200
    elif loot_chance < 7:
        return 150
    elif loot_chance < 13:
        return 100
    elif loot_chance < 21:
        return 75
    elif loot_chance < 31:
        return 50
    elif loot_chance < 56:
        return 40
    elif loot_chance < 76:
        return 30
    else:
        return 10

def loot_chance_percent(loot_amount):
    if loot_amount == 200:
        return 2
    elif loot_amount == 150:
        return 4
    elif loot_amount == 100:
        return 6
    elif loot_amount == 75:
        return 8
    elif loot_amount == 50:
        return 10
    elif loot_amount == 40:
        return 15
    elif loot_amount == 30:
        return 20
    elif loot_amount == 10:
        return 24
    else:
        return 0

def buy_chest():
    global player_gold, chests_opened
    loot_chance = calculate_loot_chance()
    loot = determine_loot(loot_chance)
    chance_percent = loot_chance_percent(loot)
    print(f"You received: {loot} Gold (Chance: {chance_percent}%)")
    player_gold = player_gold + loot - chest_cost
    chests_opened += 1
    return loot
