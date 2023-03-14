"""
my Game
"""
import random
class Player:
    """
    class Player
    """
    def __init__(self, name):
        """
        initialize the Player
        """
        self.name = name
        self.health = 100
        self.inventory = ['Demonic Sword', 'Poisoned Dagger',"hand"]
        self.current_location = "Stryyska St."

    def move(self, direction):
        """
        moving direction
        """
        if direction == "north":
            self.current_location = "I. Franka St."
        elif direction == "south":
            self.current_location = "Stryyska St."
        elif direction == "east":
            self.current_location = "T. Shevchenko Ave."
        elif direction == "west":
            self.current_location = "Kozelnytska St."
        elif direction == "northeast":
            self.current_location = "Krakivska St."
        else:
            print("Invalid direction!")

    def use_item(self, item):
        """
        using item
        """
        if item in self.inventory:
            if item in self.inventory:
                damage = random.randint(0,5)
                print(f"You attack the enemy and deal {damage} damage!")
            elif isinstance(item, Support):
                self.health += item.healing_power
                print(f"You use the {item.name} and restore {item.healing_power} health.")
            elif isinstance(item, Heal):
                if self.current_location == "I. Franka St.":
                    self.health += item.healing_power
                    print(f"You use the {item.name} and restore {item.healing_power} health.")
                else:
                    print("You can't use that item here!")
        else:
            print("You don't have that item in your inventory!")

    def attack(self, enemy, weapon):
        """
        attack the enemy
        """
        if weapon.name in self.inventory and isinstance(weapon, Weapon):
            damage = random.randint(weapon.min_damage, weapon.max_damage)
            enemy.health -= damage
            print(f"You attack {enemy.name} with {weapon.name} and deal {damage} damage!")
            if enemy.health <= 0:
                loot = enemy.die()
                self.inventory.extend(loot)
        else:
            print("You don't have that weapon in your inventory!")
            
class Character:
    """
    class Character
    """
    def __init__(self, name, health, attack_power):
        """
        initialize the Character
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        """
        attack
        """
        damage = random.randint(1, self.attack_power)
        target.health -= damage
        print(f"{self.name} attacks {target.name} and deals {damage} damage!")

class Enemy(Character):
    """
    class Enemy
    """
    def __init__(self, name, health, attack_power, loot):
        """
        initialize the Enemy
        """
        super().__init__(name, health, attack_power)
        self.loot = loot

    def die(self):
        """
        die
        """
        print(f"{self.name} has been defeated!")
        return self.loot

class Item:
    """
    class Item
    """
    def __init__(self, name, type, min_damage=0, max_damage=0, healing_power=0):
        """
        initialize the Item
        """
        self.name = name
        self.type = type
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.healing_power = healing_power

class Weapon(Item):
    """
    class Weapon
    """
    def __init__(self, name, min_damage, max_damage):
        """
        initialize the Weapon
        """
        super().__init__(name, "weapon", min_damage, max_damage)
        
class Support(Item):
    """
    class Support
    """
    def __init__(self, name, healing_power):
        """
        initialize the Support
        """
        super().__init__(name, "support", healing_power=healing_power)
        
class Heal(Item):
    """
    class Heal
    """
    def __init__(self, name, healing_power):
        """
        initialize the Heal
        """
        super().__init__(name, "heal", healing_power=healing_power)

class Boss(Enemy):
    """
    class Boss
    """
    def __init__(self, name, health, attack_power, loot, minions=None):
        """
        initialize the Boss
        """
        super().__init__(name, health, attack_power, loot)
        self.minions = minions or []
        self.current_location = random.choice(
            ["I. Franka St.", "T. Shevchenko Ave.", "Kozelnytska St.", "Krakivska St."])

    def attack(self, target):
        """
        attack
        """
        enemy = random.choice(self.minions + [self])
        if enemy == self:
            super().attack(target)
        else:
            damage = random.randint(1, enemy.attack_power)
            target.health -= damage
            print(f"{enemy.name} attacks {target.name} and deals {damage} damage!")

player_name = input("What is your name? ")
player = Player(player_name)

# creating boss and minions
boss = Boss("The Evil One", 200, 20, [Weapon("Demonic Sword", 10, 20)],
            [Enemy("Minion 1", 50, 10, [Support("Healing Potion", 20)]),
             Enemy("Minion 2", 50, 10, [Heal("Revitalizing Elixir", 30)]),
             Enemy("Minion 3", 50, 10, [Weapon("Poisoned Dagger", 5, 10)])])

# game loop
while True:
    print(f"\nYou are now at {player.current_location}.")
    print(f"Your health: {player.health}")

    if player.health <= 0:
        print("You have been defeated!")
        break
    elif len(boss.minions) == 0 and boss.health <= 0:
        print("Congratulations! You have defeated the boss and saved the world!")
        break

    if player.current_location == boss.current_location:
        enemy = boss
    else:
        enemy = Enemy("Goblin", 10, 10, [Weapon("Demonic Sword", 10, 20)])

    print(f"A wild {enemy.name} appears!")
    print(f"{enemy.name}'s health: {enemy.health}")

    # player action loop
    while True:
        action = input("What do you want to do? (attack/use item/move/quit) ").lower()

        if action == "attack":
            player.attack(enemy, random.choice([Weapon("Demonic Sword", 10, 20),
                                                Weapon("Poisoned Dagger", 5, 10),
                                                Weapon("hand", 4, 8)]))

            if enemy.health <= 0:
                loot = enemy.die()
                for item in loot:
                    player.inventory.append(item)
                if enemy in boss.minions:
                    boss.minions.remove(enemy)
                break
            enemy.attack(player)

        elif action == "use item":

            if len(player.inventory) == 0:

                print("Your inventory is empty!")

            else:

                for item in player.inventory:
                    print(item)

                item_name = input("Which item do you want to use? ")

                for item in player.inventory:

                    if item == item_name:
                        player.use_item(item)
                        enemy.attack(player)
                        break
                else:

                    print("You don't have that item in your inventory!")

        elif action == "move":
            direction = input("Which direction do you want to go? (north/south/east/west/northeast) ").lower()
            if direction in ["north", "south", "east", "west", "northeast"]:
                player.move(direction)
                break
            else:
                print("Invalid direction!")

        elif action == "heal":
            if player.current_location == "Stryyska St.":
                player.use_item(Heal("Bandage", 10))
                enemy.attack(player)
            else:
                print("You can't heal here!")

        elif action == "quit":
            print("The game is over!")
            quit()

        else:
            print("Invalid action!")
