player_gold = 150
player_debt = 0
def update_debt(update_amount):
    global player_debt
    player_debt = player_debt + update_amount

def buy_item(item_cost):
    global player_gold
    playe_gold = player_gold - item_cost

def can_buy_item(player_gold, item_cost):
    global player_debt
    if player_gold >= item_cost + player_debt:
        return True
    else:
        return False

item_a_cost = 70
item_b_cost = 100

print(f"you have {player_gold} gold")

if can_buy_item(player_gold, item_a_cost):
    buy_item(item_a_cost)

print(f"you have {player_gold} gold")

while True:
    select = input("you can buy 2 things, item a and item b, write which item you want to buy: ")
    if select != "a" or select != "b":
        