import random
from termcolor import colored

def gamble(player):
    print("\nYou're on the street, and you see a group of people gambling.")
    print("Feeling lucky? Roll the dice and test your fortune!")
    while True:
        try:
            bet = int(input("How much do you want to bet? (Enter 0 to exit): "))
            if bet == 0:
                return
            elif bet <= player.wallet:
                player.wallet -= bet
                break
            else:
                print(colored("You don't have enough Shines.", "red"))
        except ValueError:
            print(colored("Please enter a valid number.", "red"))

    print("Rolling the dice...")
    dice_roll = random.randint(1, 6)
    print("You rolled:", dice_roll)
    if dice_roll <= 3:
        print(colored("You won the gamble!", "green"))
        player.wallet += bet * 2
    else:
        print(colored("You lost the gamble!", "red"))
