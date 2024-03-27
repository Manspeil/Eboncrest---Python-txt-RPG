from termcolor import colored

class Player:
    def __init__(self, name, gender, race, player_class):
        self.name = name
        self.gender = gender
        self.race = race
        self.player_class = player_class
        self.base_stats = {"Health": 10, "Mana": 20, "Strength": 10, "Agility": 10, "Intellect": 20, "Stealth": 30}
        self.wallet = 100
        self.inventory = {"Items": [], "Worn": []}
        self.skill_levels = {"Strength": 1, "Agility": 1, "Intellect": 1, "Stealth": 1}
    def take_damage(self, damage):
        self.base_stats["Health"] -= damage
        if self.base_stats["Health"] < 0:
            self.base_stats["Health"] = 0

    def is_alive(self):
        return self.base_stats["Health"] > 0    

    def display_base_stats(self):
        print("\nBase Stats:")
        for stat, value in self.base_stats.items():
            print(colored(f"{stat}: {value}", "blue"))

    def display_inventory(self):
        print("\nInventory:")
        print(f"Shines: {self.wallet}")
        for category, items in self.inventory.items():
            print(colored(f"{category}: {', '.join(items)}", "blue"))

        print("\nOptions:")
        print("1. Equip an item")
        print("2. Use an item")
        print("3. Unequip an item")
        print("4. Back")

        while True:
            choice = input("Enter your choice: ")
            if choice == '1':
                item_to_equip = input("Enter the name of the item you want to equip: ")
                self.equip_item(item_to_equip)
            elif choice == '2':
                item_to_use = input("Enter the name of the item you want to use: ")
                self.use_item(item_to_use)
            elif choice == '3':
                item_to_unequip = input("Enter the name of the item you want to unequip: ")
                self.unequip_item(item_to_unequip)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    def equip_item(self, item_name):
        items_stat_bonus = {
            "Sword": {"Strength": 5}, "Axe": {"Strength": 7}, "Mace": {"Strength": 6},
            "Shield": {"Strength": 3, "Health": 5}, "Iron Armour": {"Health": 10, "Agility": -5},
            "Leather Armour": {"Agility": 5, "Stealth": 10}
        }
        item_stat_bonus = items_stat_bonus.get(item_name)
        if item_stat_bonus:
            for stat, bonus in item_stat_bonus.items():
                self.base_stats[stat] += bonus
            if item_name not in self.inventory["Worn"]:  # Ensure item is not already equipped
                self.inventory["Worn"].append(item_name)
                print(colored(f"{item_name} equipped successfully.", "green"))
            else:
                print(colored(f"{item_name} is already equipped.", "yellow"))
        else:
            print(colored("Item not found.", "red"))

    def unequip_item(self, item_name):
        if item_name in self.inventory["Worn"]:
            self.inventory["Worn"].remove(item_name)
            self.inventory["Items"].append(item_name)  # Move item back to inventory items list
            print(colored(f"{item_name} unequipped successfully.", "green"))
        else:
            print(colored(f"{item_name} is not currently equipped.", "yellow"))

    def use_item(self, item_name):
        if item_name in self.inventory["Items"]:
            if item_name == "Health Potion":
                self.base_stats["Health"] += 10
                print(colored("Health Potion used. Health increased by 10.", "green"))
            elif item_name == "Mana Potion":
                self.base_stats["Mana"] += 15
                print(colored("Mana Potion used. Mana increased by 15.", "green"))
            elif item_name == "Apple":
                self.base_stats["Health"] += 5
                print(colored("Apple eaten. Health increased by 5.", "green"))
            elif item_name == "Bread":
                self.base_stats["Health"] += 10
                print(colored("Bread eaten. Health increased by 10.", "green"))
            elif item_name == "Cheese":
                self.base_stats["Health"] += 8
                print(colored("Cheese eaten. Health increased by 8.", "green"))
            self.inventory["Items"].remove(item_name)
        else:
            print(colored("Item not found in inventory.", "red"))

    def train_skill(self, skill_name):
        if skill_name in self.skill_levels:
            if self.wallet >= 20:  # Cost to level up a skill
                self.wallet -= 20
                self.skill_levels[skill_name] += 1
                print(colored(f"{skill_name} leveled up! {skill_name} level: {self.skill_levels[skill_name]}", "green"))
        
        else:
            print(colored("Skill not found.", "red"))  # Notify if the skill is not found

