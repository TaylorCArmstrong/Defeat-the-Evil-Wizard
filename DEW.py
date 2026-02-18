# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special(self, opponent, special_choice=None):
        print(f"{self.name} doesn't have a special ability.")

    def special_options(self):
        return []

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def special_options(self):
        return ["Power Strike", "Battle Cry"]

    def special(self, opponent, special_choice):
        if special_choice == '1':
            damage = 45
            opponent.health -= damage
            print(f"{self.name} uses Power Strike for {damage} damage!")
        elif special_choice == '2':
            damage = 30
            self.health = min(self.max_health, self.health + 20)
            opponent.health -= damage
            print(f"{self.name} uses Battle Cry for {damage} damage and restores 20 health!")
        else:
            print("Invalid special ability choice.")
            return

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def special_options(self):
        return ["Fireball", "Arcane Shield"]

    def special(self, opponent, special_choice):
        if special_choice == '1':
            damage = 60
            opponent.health -= damage
            print(f"{self.name} casts Fireball for {damage} damage!")
        elif special_choice == '2':
            damage = 25
            self.health = min(self.max_health, self.health + 25)
            opponent.health -= damage
            print(f"{self.name} casts Arcane Shield for {damage} damage and restores 25 health!")
        else:
            print("Invalid special ability choice.")
            return

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=30)

    def special_options(self):
        return ["Piercing Arrow", "Volley"]

    def special(self, opponent, special_choice):
        if special_choice == '1':
            damage = 40
            opponent.health -= damage
            print(f"{self.name} uses Piercing Arrow for {damage} damage!")
        elif special_choice == '2':
            damage = 50
            opponent.health -= damage
            print(f"{self.name} uses Volley for {damage} damage!")
        else:
            print("Invalid special ability choice.")
            return

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

# Create Paladin class 
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=15)

    def special_options(self):
        return ["Holy Smite", "Divine Blessing"]

    def special(self, opponent, special_choice):
        if special_choice == '1':
            damage = 35
            heal_amount = 15
            opponent.health -= damage
            self.health = min(self.max_health, self.health + heal_amount)
            print(f"{self.name} uses Holy Smite for {damage} damage and heals {heal_amount} health!")
        elif special_choice == '2':
            damage = 20
            heal_amount = 35
            opponent.health -= damage
            self.health = min(self.max_health, self.health + heal_amount)
            print(f"{self.name} uses Divine Blessing for {damage} damage and heals {heal_amount} health!")
        else:
            print("Invalid special ability choice.")
            return

        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")



def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") 
    print("4. Paladin")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return  Archer(name)
    elif class_choice == '4':
        return  Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            specials = player.special_options()
            if specials:
                print("Choose a special ability:")
                for idx, special_name in enumerate(specials, start=1):
                    print(f"{idx}. {special_name}")
                special_choice = input("Enter special ability number: ")
                player.special(wizard, special_choice)
            else:
                player.special(wizard)
        elif choice == '3':
            pass  # Implement heal method
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()