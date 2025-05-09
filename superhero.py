# Base class: Superhero
class Superhero:
    def __init__(self, name, power, origin, health=100):
        self.name = name
        self.power = power
        self.origin = origin
        self.__health = health

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health = max(0, self.__health - damage)
        return f"{self.name} takes {damage} damage, health now {self.__health}"

    def is_alive(self):
        return self.__health > 0

    def __str__(self):
        return f"{self.name} from {self.origin} with power: {self.power}"

# Subclass: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} km/h and unleashes {self.power}!"

# Subclass: TechHero
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadgets):
        super().__init__(name, power, origin)
        self.gadgets = gadgets

    def use_power(self):
        return f"{self.name} uses gadgets like {', '.join(self.gadgets)} and blasts {self.power}!"

# Villain class
class Villain:
    def __init__(self, name, evil_plan, health=120):
        self.name = name
        self.evil_plan = evil_plan
        self.__health = health

    def attack(self):
        return f"{self.name} executes {self.evil_plan}!"

    def take_damage(self, damage):
        self.__health = max(0, self.__health - damage)
        return f"{self.name} takes {damage} damage, health now {self.__health}"

    def is_alive(self):
        return self.__health > 0

    def get_health(self):
        return self.__health

    def __str__(self):
        return f"Villain {self.name} with plan: {self.evil_plan}"

# Hero Team class
class HeroTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_hero(self, hero):
        self.members.append(hero)
        print(f"{hero.name} has joined team {self.team_name}!")

    def team_attack(self, villain):
        print(f"\nTeam {self.team_name} attacks {villain.name}!")
        for hero in self.members:
            if hero.is_alive():
                print(hero.use_power())
                damage = 20  # fixed damage for simplicity
                print(villain.take_damage(damage))
            else:
                print(f"{hero.name} is down and can't fight.")

# Demo Simulation
if __name__ == "__main__":
    # Create heroes
    hero1 = FlyingHero("SkyFalcon", "Wind Slash", "Cloud Kingdom", 500)
    hero2 = TechHero("ByteKnight", "Laser Beam", "Silicon Valley", ["Drone", "Smart Shield"])

    # Create villain
    villain = Villain("DarkByte", "City Blackout")

    # Create and fill team
    avengers = HeroTeam("NeoGuardians")
    avengers.add_hero(hero1)
    avengers.add_hero(hero2)

    # Simulate battle
    avengers.team_attack(villain)
    print("\nVillain counterattacks!\n")
    print(villain.attack())
    print(hero1.take_damage(40))
    print(hero2.take_damage(60))

    # Round 2
    avengers.team_attack(villain)

    # Outcome
    if not villain.is_alive():
        print(f"\n{villain.name} has been defeated! 🌟")
    else:
        print(f"\n{villain.name} is still standing with {villain.get_health()} HP!")
