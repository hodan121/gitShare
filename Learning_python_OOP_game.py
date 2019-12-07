from random import random, randint


class Person:
    def __init__(self, race, _damage, _health, _armor):
        self.race = race
        self._damage = _damage
        self._health = _health
        self._armor = _armor

    def get_atr(self):
        print(
            f'У нас тут {self.race}, {self.get_health()} ХП, тычка на {self._damage} с руки, армор поглощает {round(0.1 * self._armor * 100)}% урона')
    
    def get_health(self):
        return self._health

    def _i_deal_damage(self):
        return self._damage

    def _i_get_damage(self, enemy):
        self._health -= enemy._i_deal_damage() * (1 - 0.1 * self._armor)

    def i_attack(self, enemy):
        self._i_deal_damage()
        enemy._i_get_damage(self)

    def _initiative(self):
        return random()


class Player(Person):
    def __init__(self, _damage=randint(110, 120), _health=randint(300, 330), _armor=randint(1, 3)):
        self.race = 'Человек'
        super().__init__(self.race, _damage, _health, _armor)


class Enemy(Person):
    def __init__(self, _damage=randint(120, 130), _health=randint(280, 310), _armor=randint(1, 3)):
        self.race = 'Андед'
        super().__init__(self.race, _damage, _health, _armor)


class Game:
    def __init__(self, player, enemy):
        if enemy._initiative() > player._initiative():
            self.attacker = enemy
            self.defer = player
        else:
            self.attacker = player
            self.defer = enemy

    def gaming(self):
        while True:
            self.attacker.i_attack(self.defer)
            if self.defer.get_health() <=0:
                print(f'{self.attacker.race} выжил! У него осталось {round(self.attacker.get_health())} ХП')
                break
            else:
                self.attacker, self.defer = self.defer, self.attacker

human = Player()
undead = Enemy()

human.get_atr()
undead.get_atr()

game = Game(human, undead)
game.gaming()
