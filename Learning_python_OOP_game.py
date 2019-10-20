import random


def initiative():
    return random.random()


class Person:
    def __init__(self, race, damage, health, armor):
        self.race = race
        self.damage = damage
        self.health = health
        self.armor = armor

    def get_atr(self):
        print(
            f'У нас тут {self.race}, {self.health} ХП, тычка на {self.damage} с руки, армор поглощает {self.armor * 100}% урона')

    def i_deal_damage(self):
        return self.damage()

    def i_get_damage(self, enemy):
        self.health -= enemy.i_deal_damage() * (1 - self.armor)

    def i_attack(self, enemy):
        self.i_deal_damage()
        enemy.i_get_damage(self)


class Player(Person):
    def __init__(self, damage=100, health=300, armor=0.4):
        self.race = 'Человек'
        super().__init__(self.race, damage, health, armor)


class Enemy(Person):
    def __init__(self, damage=70, health=400, armor=0.2):
        self.race = 'Андед'
        super().__init__(self.race, damage, health, armor)


class Game:
    def __init__(self):
        if initiative() > initiative():
            self.attacker = Enemy()
            self.defer = Player()
        else:
            self.attacker = Player()
            self.defer = Enemy()

    def gaming(self):
        self.attacker.i_attack(self.defer)
        print(self.defer.health)


human = Player()
undead = Enemy()

human.get_atr()
undead.get_atr()

game = Game()
game.gaming()
