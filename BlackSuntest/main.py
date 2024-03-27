from gamble import gamble
from train import train
from villages import Village, Location
from player import Player
from utilities import typewriter_effect
from termcolor import colored
from shop import shop_market, shop_blacksmith, shop_tavern, shop_alchemist
from text import intro_text, race_descriptions, class_descriptions, location_descriptions, townsquare_options
from fight import CombatSystem, Enemy

class Game:
    def __init__(self):
        self.player = None
        self.village = None
        self.combat_system = CombatSystem()

    def start(self):
        print(intro_text)

        self.player = self.create_character()
        self.village = self.setup_village()

        self.game_loop()

    def create_character(self):
        print("What's your name, adventurer?")
        name = input().capitalize()
        print(
            f"Welcome, {name}! Choose your gender (type 'male' or 'female'): ")
        gender = input().lower()
        print("\nNow, let's learn about the races of Eboncrest:\n")
        races = {
            "1": ("Umbrals", race_descriptions["Umbrals"]),
            "2": ("Lumineers ", race_descriptions["Lumineers"]),
            "3": ("Nightborn", race_descriptions["Nightborn"]),
            "4": ("Lunar Sages", race_descriptions["Lunar Sages"])
        }
        while True:
            print(
                "Choose a race to learn more about (or enter 'done' to proceed):")
            for key, value in races.items():
                print(colored(f"{key}. {value[0]}", "cyan"))
            race_choice = input(
                "Enter the number corresponding to your choice: ")
            if race_choice == "done":
                break
            elif race_choice in races.keys():
                race_name, race_description = races[race_choice]
                print(colored(
                    f"{race_name}: {race_description}", "yellow"))
                confirm_race = input(
                    "Would you like to select this race? (yes/no): ").lower()
                if confirm_race == "yes":
                    break
                else:
                    print(
                        "Invalid choice. Please enter a number between 1 and 4.")

        player_classes = {
            "1": (colored("Trickster", "magenta"), class_descriptions["Trickster"]),
            "2": (colored("Philosopher", "blue"), class_descriptions["Philosopher"]),
            "3": (colored("Duelist", "red"), class_descriptions["Duelist"]),
            "4": (colored("Pathfinder", "cyan"), class_descriptions["Pathfinder"]),
            "5": (colored("Doctor", "green"), class_descriptions["Doctor"])
        }

        while True:
            print("\nChoose a class to learn more about (or enter 'done' to proceed):")
            for key, value in player_classes.items():
                print(f"{key}. {value[0]}")
            class_choice = input("Enter the number corresponding to your choice: ")
            if class_choice == "done":
                break
            elif class_choice in player_classes.keys():
                class_name, class_description = player_classes[class_choice]
                print(colored(
                    f"{class_name}: {class_description}", "yellow"))
                confirm_class = input(
            "Would you like to select this class? (yes/no): ").lower()
                if confirm_class == "yes":
                    break
                else:
                    print(
                        "Invalid choice. Please enter a number between 1 and 5.")

        print("\nCharacter Summary:")
        print(colored(
            f"You look at the mirror - a young {race_name} {class_name}, you wonder what it was like to witness daylight.. All your life you lived surrounded by candles.. in other words, to see you rely on fire.", "green"))

        return Player(name, gender, race_name, class_name)

    def setup_village(self):
        village = Village(
            "Eboncrest Village", "A small village situated at the edge of the Kingdom of Eboncrest.")
        village.add_location(
            Location("Market", location_descriptions["Market"]))
        village.add_location(
            Location("Blacksmith", location_descriptions["Blacksmith"]))
        village.add_location(
            Location("Tavern", location_descriptions["Tavern"]))
        village.add_location(
            Location("Alchemist's Shop", location_descriptions["Alchemist's Shop"]))
        # Add Black Forest location with enemies
        black_forest = Location("Black Forest", "A dense forest shrouded in darkness.")
        black_forest.add_enemy("Goblin")
        black_forest.add_enemy("Skeleton")
        black_forest.add_enemy("Orc")
        village.add_location(black_forest)
        return village

    def game_loop(self):
        while True:
            print(townsquare_options)
            choice = input("Enter your choice: ")

            if choice == '1':
                shop_market(self.player)
            elif choice == '2':
                shop_blacksmith(self.player)
            elif choice == '3':
                shop_tavern(self.player)
            elif choice == '4':
                shop_alchemist(self.player)
            elif choice == '5':
                print("You are in the Black Forest.")
                self.explore_black_forest()
            elif choice == '6':
                gamble(self.player)
            elif choice == '7':
                train(self.player)
            elif choice == '8':
                self.player.display_base_stats()
                self.player.display_inventory()
            elif choice == '9':
                print("Goodbye, adventurer! See you next time.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

    def explore_black_forest(self):
        current_location = self.village.get_location("Black Forest")
        if current_location:
            enemies = current_location.get_enemies()
            if enemies:
                print("You encounter enemies in the Black Forest!")
                print("You have the following enemies to face:")
                for enemy in enemies:
                    print(f"- {enemy}")
                fight_or_flee = input("Do you want to fight or flee? (fight/flee): ").lower()
                if fight_or_flee == "fight":
                    # Start combat
                    for enemy_name in enemies:
                        enemy = Enemy(enemy_name, 20, 5)  # Initialize enemy with default stats
                        if not self.combat_system.initiate_combat(self.player, enemy):
                            # Player lost the battle
                            print("You were defeated in battle...")
                            return
                        # Player won the battle against current enemy
                        print(f"You defeated the {enemy_name}.")
                    print("You defeated all enemies in the Black Forest!")
                elif fight_or_flee == "flee":
                    print("You flee from the enemies.")
                else:
                    print("Invalid choice. Please enter 'fight' or 'flee'.")
            else:
                print("The Black Forest seems eerily quiet...")
        else:
            print("Error: Black Forest location not found.")

if __name__ == "__main__":
    game = Game()
    game.start()
