import random


class Person:
    def __init__(self, race, _damage, _health, _armor):
        self.race = race
        self._damage = _damage
        self._health = _health
        self._armor = _armor

    def get_atr(self):
        print(
            f'У нас тут {self.race}, {self._health} ХП, тычка на {self._damage} с руки, армор поглощает {self._armor * 100}% урона')
    
    def get_health(self):
        return self._health

    def _i_deal_damage(self):
        return self._damage

    def _i_get_damage(self, enemy):
        self._health -= enemy._i_deal_damage() * (1 - self._armor)

    def i_attack(self, enemy):
        self._i_deal_damage()
        enemy._i_get_damage(self)

    def initiative(self):
        return random.random()


class Player(Person):
    def __init__(self, _damage=100, _health=300, _armor=0.4):
        self.race = 'Человек'
        super().__init__(self.race, _damage, _health, _armor)


class Enemy(Person):
    def __init__(self, _damage=70, _health=400, _armor=0.2):
        self.race = 'Андед'
        super().__init__(self.race, _damage, _health, _armor)


class Game:
    def __init__(self, player, enemy):
        if enemy.initiative() > player.initiative():
            self.attacker = enemy
            self.defer = player
        else:
            self.attacker = player
            self.defer = enemy

    def gaming(self):
        while True:
            self.attacker.i_attack(self.defer)
            if self.defer.get_health() <=0:
                print(f'{self.attacker.race} выжил! У него осталось {self.attacker.get_health()} ХП')
                break
            else:
                self.defer, self.attacker = self.attacker, self.defer

human = Player()
undead = Enemy()
human.

human.get_atr()
undead.get_atr()

game = Game(human, undead)
game.gaming()
