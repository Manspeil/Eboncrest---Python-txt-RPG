from termcolor import colored

def shop_market(player):
    print("\nWelcome to the market! Here's what's available:")
    items = {"Food": {"Apple": 5, "Bread": 10, "Weed": 8}, "Potions": {"Health Potion": 15, "Mana Potion": 20}, "Treasure Maps": {"Map of Forgotten Ruins": 50, "Map to Hidden Treasures": 75}}
    print(f"Shines: {player.wallet}")
    for category, item_list in items.items():
        print(colored(f"{category}:", "cyan"))
        for index, (item, price) in enumerate(item_list.items(), start=1):
            print(colored(f"{index}. {item}: {price} Shines", "yellow"))

    while True:
        choice = input("\nChoose an item to buy or enter '0' to leave: ")
        if choice == '0':
            return
        elif choice.isdigit():
            choice = int(choice)
            for category, item_list in items.items():
                if 1 <= choice <= len(item_list):
                    item = list(item_list.keys())[choice - 1]
                    price = item_list[item]
                    if player.wallet >= price:
                        player.wallet -= price
                        player.inventory["Items"].append(item)
                        print(colored(f"{item} purchased successfully!", "green"))
                    else:
                        print(colored("You don't have enough Shines to buy that item.", "red"))
                    return
                else:
                    print("Invalid choice. Please enter a valid item number.")
        else:
            print("Invalid input. Please enter a number.")

def shop_blacksmith(player):
    print("\nWelcome to the blacksmith's shop! Here's what's available:")
    items = {
        "Weapons": {"Sword": 50, "Axe": 40, "Mace": 45},
        "Armours": {"Shield": 30, "Iron Armour": 60, "Leather Armour": 40}
    }
    print(f"Shines: {player.wallet}")
    for category, item_list in items.items():
        print(colored(f"{category}:", "cyan"))
        for index, (item, price) in enumerate(item_list.items(), start=1):
            print(colored(f"{index}. {item}: {price} Shines", "yellow"))

    while True:
        choice = input("\nChoose an item to buy or enter '0' to leave: ")
        if choice == '0':
            return
        elif choice.isdigit():
            choice = int(choice)
            for category, item_list in items.items():
                if 1 <= choice <= len(item_list):
                    item = list(item_list.keys())[choice - 1]
                    price = item_list[item]
                    if player.wallet >= price:
                        player.wallet -= price
                        confirm_choice = input(colored(f"Do you want to equip {item}? (yes/no): ", "cyan")).lower()
                        if confirm_choice == "yes":
                            player.equip_item(item)
                        else:
                            player.inventory["Items"].append(item)  # Add to items if not equipped
                            print(colored(f"{item} purchased successfully!", "green"))
                    else:
                        print(colored("You don't have enough Shines to buy that item.", "red"))
                    return
                else:
                    print("Invalid choice. Please enter a valid item number.")
        else:
            print("Invalid input. Please enter a number.")

def shop_tavern(player):
    print("\nWelcome to the tavern! Here's what's available:")
    drinks = {"Ale": 5, "Wine": 10, "Mead": 8}
    print(f"Shines: {player.wallet}")
    for index, (drink, price) in enumerate(drinks.items(), start=1):
        print(colored(f"{index}. {drink}: {price} Shines", "yellow"))

    while True:
        choice = input("\nChoose a drink to buy or enter '0' to leave: ")
        if choice == '0':
            return
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(drinks):
                drink = list(drinks.keys())[choice - 1]
                price = drinks[drink]
                if player.wallet >= price:
                    player.wallet -= price
                    print(colored(f"You enjoy a refreshing {drink}!", "green"))
                else:
                    print(colored("You don't have enough Shines to buy that drink.", "red"))
                return
            else:
                print("Invalid choice. Please enter a valid drink number.")
        else:
            print("Invalid input. Please enter a number.")
def shop_alchemist(player):
    print("\nWelcome to the alchemist's workshop! Here's what's available:")
    potions = {"Healing Potion": 20, "Strength Potion": 30, "Invisibility Potion": 40}
    print(f"Shines: {player.wallet}")
    for index, (potion, price) in enumerate(potions.items(), start=1):
        print(colored(f"{index}. {potion}: {price} Shines", "yellow"))

    while True:
        choice = input("\nChoose a potion to buy or enter '0' to leave: ")
        if choice == '0':
            return
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(potions):
                potion = list(potions.keys())[choice - 1]
                price = potions[potion]
                if player.wallet >= price:
                    player.wallet -= price
                    player.inventory["Potions"].append(potion)
                    print(colored(f"You obtained a {potion}!", "green"))
                else:
                    print(colored("You don't have enough Shines to buy that potion.", "red"))
                return
            else:
                print("Invalid choice. Please enter a valid potion number.")
        else:
            print("Invalid input. Please enter a number.")
