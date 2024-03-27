class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enemies = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def get_enemies(self):
        return self.enemies

class Village:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.locations = []

    def add_location(self, location):
        self.locations.append(location)

    def get_location(self, location_name):
        for location in self.locations:
            if location.name.lower() == location_name.lower():
                return location
        return None

