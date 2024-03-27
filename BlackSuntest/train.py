from termcolor import colored

def train(player):
    for skill, level in player.skill_levels.items():
        print(f"{colored(skill, 'blue')}: {level}")

    print("Which skill would you like to train?")
    print("1. Strength")
    print("2. Agility")
    print("3. Intellect")
    print("4. Stealth")
    print("5. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            if player.wallet >= 20:
                player.train_skill("Strength")
            else:
                print(colored("You don't have enough Shines to train Strength.", "red"))
        elif choice == '2':
            if player.wallet >= 20:
                player.train_skill("Agility")
            else:
                print(colored("You don't have enough Shines to train Agility.", "red"))
        elif choice == '3':
            if player.wallet >= 20:
                player.train_skill("Intellect")
            else:
                print(colored("You don't have enough Shines to train Intellect.", "red"))
        elif choice == '4':
            if player.wallet >= 20:
                player.train_skill("Stealth")
            else:
                print(colored("You don't have enough Shines to train Stealth.", "red"))
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")