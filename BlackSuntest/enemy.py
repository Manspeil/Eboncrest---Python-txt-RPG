import random

class Enemy:
    def __init__(self, name, max_hp, damage):
        self.name = name
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.damage = damage

    def attack(self):
        return random.randint(1, self.damage)

class Goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", max_hp=20, damage=8)

class Wolf(Enemy):
    def __init__(self):
        super().__init__(name="Wolf", max_hp=25, damage=10)

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", max_hp=30, damage=12)
