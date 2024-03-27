# fight.py

import random
from termcolor import colored

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_player(self, player):
        damage = random.randint(1, self.attack)
        player.take_damage(damage)
        print(f"The {self.name} attacks you for {damage} damage!")

class CombatSystem:
    @staticmethod
    def initiate_combat(player, enemy):
        print(colored(f"You encounter a {enemy.name} in the Black Forest!", "red"))
        while player.is_alive() and enemy.is_alive():
            CombatSystem.player_turn(player, enemy)
            if enemy.is_alive():
                CombatSystem.enemy_turn(player, enemy)
        if player.is_alive():
            print(colored(f"You defeated the {enemy.name}!", "green"))
            return True
        else:
            print(colored("You were defeated in battle...", "red"))
            return False

    @staticmethod
    def player_turn(player, enemy):
        print("Your turn:")
        print("1. Attack")
        print("2. Run")

        choice = input("Enter your choice: ")
        if choice == '1':
            damage = random.randint(1, player.base_stats["Strength"])
            enemy.take_damage(damage)
            print(f"You attack the {enemy.name} for {damage} damage!")
        elif choice == '2':
            print("You attempt to flee...")
            if random.random() < 0.5:
                print("You successfully flee from the enemy!")
            else:
                print("You failed to flee and must face the enemy's attack!")
                CombatSystem.enemy_turn(player, enemy)
        else:
            print("Invalid choice. You stand still.")

    @staticmethod
    def enemy_turn(player, enemy):
        enemy.attack_player(player)
        if not player.is_alive():
            return

# Example enemies
enemy1 = Enemy("Goblin", 20, 5)
enemy2 = Enemy("Bandit", 25, 6)
enemy3 = Enemy("Wolf", 30, 7)
