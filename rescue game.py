# Класс `Hero`:
# - Атрибуты:
# - Имя (`name`)
# - Здоровье (`health`), начальное значение 100
# - Сила удара (`attack_power`), начальное значение 20
# - Методы:
# - `attack(other)`: атакует другого героя (`other`), отнимая здоровье в размере своей силы удара
# - `is_alive()`: возвращает `True`, если здоровье героя больше 0, иначе `False`
# Класс `Game`:
# - Атрибуты:
# - Игрок (`player`), экземпляр класса `Hero`
# - Компьютер (`computer`), экземпляр класса `Hero`
# - Методы:
# - `start()`: начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет.
# Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника)
# и объявляет победителя.

import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.special_ability_used = False

    def attack(self, other):
        damage = random.randint(5, self.attack_power)  # Random damage from 5 to attack_power (20)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    # Немного отсебятины, которой нет в задании. Добавила восстановление здоровья героев. Так интереснее. Эту часть помогал делать Котик
    def use_special_ability(self):
        if not self.special_ability_used:
            heal_amount = random.randint(5, 15)
            self.health += heal_amount
            self.special_ability_used = True
            print(f"{self.name} использует лечение и восстанавливает {heal_amount} здоровья!")
        else:
            print(f"{self.name} уже использовал лечение!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name}: {self.health} ед.здоровья"

class Game:
    def __init__(self):
        self.player = None
        self.computer = None

    def start(self):
        player_name = input("Введите имя вашего героя: ")
        print('Ваш герой может использовать лечение и восстановить часть своего здоровья. \nНо воспользоваться этой возможностью можно только один раз!')
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

        while self.player.is_alive() and self.computer.is_alive():
            print("\nСтатусы:")
            print(self.player)
            print(self.computer)

            self.player_turn()
            if self.computer.is_alive():
                self.computer_turn()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def player_turn(self):
        action = input("Выберите действие: 1 - Атаковать, 2 - Использовать лечение: ")
        if action == "1":
            self.player.attack(self.computer)
        elif action == "2":
            self.player.use_special_ability()
        else:
            print("Неверный ввод. Попробуйте еще раз.")

    def computer_turn(self):
        if random.choice([True, False]) and not self.computer.special_ability_used:
            self.computer.use_special_ability()
        else:
            self.computer.attack(self.player)

game = Game()
game.start()