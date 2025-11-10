"""
COMP 163 - Project 2: Character Abilities Showcase
Name: [Dion Brown]
Date: [11/10/2025]

AI Usage: ChatGPT (GPT-5) helped show the concepts of the class methods while also explaining inheritance and overriding.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        # Store both characters for the battle
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show both characters’ starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Round 1 starts
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        # Second character only attacks if still alive
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        # Show results after both attacks
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        # Decide winner or tie
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

import random  # For critical hits

class Character:
    """
    Base class for all characters.
    """
    
    def __init__(self, name, health, strength, magic):
        """Set up the character’s basic info."""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        
    def attack(self, target):
        """
        Basic physical attack.
        Uses strength to deal damage.
        """
        damage = self.strength
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def take_damage(self, damage):
        """
        Lose health equal to the damage taken.
        Health cannot go below 0.
        """
        self.health = max(0, self.health - damage)
        print(f"{self.name} takes {damage} damage. Remaining health: {self.health}")
        
    def display_stats(self):
        """Print the character’s current stats in a simple format."""
        print(f"Name: {self.name} | Health: {self.health} | Strength: {self.strength} | Magic: {self.magic}")

class Player(Character):
    """
    Base class for all player-controlled characters.
    Inherits everything from Character and adds player info.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """Set up player stats and class info."""
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        self.experience = 0
        
    def display_stats(self):
        """
        Show stats from Character and add player info.
        """
        super().display_stats()
        print(f"Class: {self.character_class} | Level: {self.level} | Experience: {self.experience}")

class Warrior(Player):
    """
    Warrior class - strong and tough fighter.
    High health and strength, low magic.
    """
    
    def __init__(self, name):
        """Make a warrior with preset stats."""
        super().__init__(name, "Warrior", health=120, strength=15, magic=5)
        
    def attack(self, target):
        """Warrior’s basic attack does extra strength damage."""
        damage = self.strength + 5
        print(f"{self.name} swings a mighty sword at {target.name} for {damage} damage!")
        target.take_damage(damage)
        
    def power_strike(self, target):
        """Special move: a huge attack that deals double damage."""
        damage = self.strength * 2
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        target.take_damage(damage)

class Mage(Player):
    """
    Mage class - master of magic.
    High magic power, low health and strength.
    """
    
    def __init__(self, name):
        """Make a mage with preset stats."""
        super().__init__(name, "Mage", health=80, strength=8, magic=20)
        
    def attack(self, target):
        """Mage attacks using magic instead of strength."""
        damage = self.magic
        print(f"{self.name} casts a spell on {target.name} for {damage} magic damage!")
        target.take_damage(damage)
        
    def fireball(self, target):
        """Special spell: a fireball that does extra magic damage."""
        damage = self.magic + 10
        print(f"{self.name} launches a Fireball at {target.name} for {damage} damage!")
        target.take_damage(damage)

class Rogue(Player):
    """
    Rogue class - fast and sneaky.
    Medium stats with a chance for critical hits.
    """
    
    def __init__(self, name):
        """Make a rogue with preset stats."""
        super().__init__(name, "Rogue", health=90, strength=12, magic=10)
        
    def attack(self, target):
        """Rogue has a random chance to land a critical hit (double damage)."""
        crit_chance = random.randint(1, 10)  # 30% chance (1-3)
        if crit_chance <= 3:
            damage = self.strength * 2
            print(f"Critical hit! {self.name} strikes {target.name} for {damage} damage!")
        else:
            damage = self.strength
            print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)
        
    def sneak_attack(self, target):
        """Special move: guaranteed critical hit (double damage)."""
        damage = self.strength * 2
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} critical damage!")
        target.take_damage(damage)

class Weapon:
    """
    Weapon class to show composition (a character has a weapon).
    """
    
    def __init__(self, name, damage_bonus):
        """Make a weapon with a name and bonus damage."""
        self.name = name
        self.damage_bonus = damage_bonus
        
    def display_info(self):
        """Print the weapon’s info."""
        print(f"Weapon: {self.name} | Damage Bonus: +{self.damage_bonus}")

# ============================================================================
# MAIN PROGRAM FOR TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # Create one of each type of character
    warrior = Warrior("Sir Galahad")
    mage = Mage("Merlin")
    rogue = Rogue("Robin Hood")
    
    # Show all stats
    print("\n📊 Character Stats:")
    warrior.display_stats()
    mage.display_stats()
    rogue.display_stats()
    
    # Test same method name (attack) but different results
    print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    dummy_target = Character("Target Dummy", 100, 0, 0)
    
    # Each character attacks the dummy
    for character in [warrior, mage, rogue]:
        print(f"\n{character.name} attacks the dummy:")
        character.attack(dummy_target)
        dummy_target.health = 100  # Reset dummy after each test
    
    # Try each special move
    print("\n✨ Testing Special Abilities:")
    target1 = Character("Enemy1", 50, 0, 0)
    target2 = Character("Enemy2", 50, 0, 0)
    target3 = Character("Enemy3", 50, 0, 0)
    
    warrior.power_strike(target1)
    mage.fireball(target2)
    rogue.sneak_attack(target3)
    
    # Show weapons
    print("\n🗡️ Testing Weapon Composition:")
    sword = Weapon("Iron Sword", 10)
    staff = Weapon("Magic Staff", 15)
    dagger = Weapon("Steel Dagger", 8)
    
    sword.display_info()
    staff.display_info()
    dagger.display_info()
    
    # Run the built-in battle system
    print("\n⚔️ Testing Battle System:")
    battle = SimpleBattle(warrior, mage)
    battle.fight()
    
    print("\n✅ Testing complete!")

