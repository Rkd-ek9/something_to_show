from random import randint as rd
from glassarium import glassarium as glass


def roll(items, chance):
    rand = rd(0, sum(chance))
    for i in range(len(chance)):
        if rand <= chance[i]:
            return items[i]
        rand -= chance[i]


class Chare:
    def __init__(self, name="Чарминг", cl="knight", lvl=1):
        self.hero = glass["hero"][cl]
        self.act = self.hero["skills"]
        self.base_health = self.hero["base_health"]
        self.health = self.base_health
        self.lvl = lvl
        self.name = name
        self.att = self.act[0]
        self.feature = self.hero['feature']
        self.weapon = self.hero['base_weapon']
        self.armor = self.hero['base_armor']
        self.inventory = {"food": [],
                          "weapon": []}
        self.tocken = 99

    def fight(self):
        enemy = Enemy(self.lvl)
        lvl = self.lvl
        heavy = eval(self.feature["heavy"]) + eval(self.weapon["heavy"])
        light = eval(self.feature["light"]) + eval(self.weapon["light"])
        parry = eval(self.feature["parry"]) + eval(self.weapon["parry"])
        resist = eval(self.feature["resist"]) + eval(self.weapon["resist"]) + eval(self.armor["resist"])
        print(f"Начался бой")
        while enemy.health > 0:
            print(f"""Ваш противник: {enemy.name}
Его здоровье: {enemy.health}
Ваше здоровье: {self.health}""")
            enemy.attack()
            print(enemy.att["disc"])
            self.attack()
            if enemy.att["type"] == "Parry" and self.att["type"] == "Heavy":
                print(f"Противник парировал вашу атаку, вы получили {eval(enemy.att['dmg'])}")
                self.health -= eval(enemy.att["dmg"])
            elif enemy.att["type"] == "Heavy" and self.att["type"] == "Parry":
                print(f"Вы парировали тяжёлую атаку противника, вы нанесли {eval(self.att['dmg'])}")
                enemy.health -= eval(self.att["dmg"])
            elif enemy.att["type"] == "Parry":
                print("Противник попытался парировать атаку, но не смог")
                enemy.health -= eval(self.att["dmg"])
            elif self.att["type"] == "Parry":
                print(f"Вы не смогли парировать атаку, вы получили {eval(enemy.att['dmg'])}")
                self.health -= eval(enemy.att["dmg"])
            else:
                print(f"Вы получили {eval(enemy.att['dmg'])}, нанесли {eval(self.att['dmg'])}")
                self.health -= eval(enemy.att["dmg"])
                enemy.health -= eval(self.att["dmg"])
            if self.health <= 0:
                break
            print()
        else:
            print(f"Вы победили {enemy.name}")
            print("Ваш уровень повышен")
            self.lvl += 1
            self.base_health += 5
            self.health = self.base_health
            print("=" * 40 + "\n", end="")
            return True
        print(f"{self.name} получил критический урон и умер.")
        print("Вы проиграли")
        return False

    def attack(self):

        print("Ваши действия:")
        for i in range(len(self.act)):
            print(f"{i + 1}. {self.act[i]['disc']}")
        self.att = self.act[int(input()) - 1]
        print(f"Вы выбрали '{self.att['disc']}'")

    def intro(self):
        print(self.hero["intro"])
        print('=' * 40)

    def get(self, what="weapon", item={}):
        self.inventory[what].append(item)

    def equip_weapon_from_ground(self, weapon):
        self.get(item=self.weapon)
        self.weapon = weapon

    def change_weapon(self):
        if not self.inventory["weapon"]:
            print("Вам не на что поменять оружие")
            return
        print("Ваше оружие")
        print(self.weapon)
        print()
        print("Оружие в вашем инвентаре:")
        for i in range(len(self.inventory["weapon"])):
            print(f"{i + 1} {self.inventory['weapon'][i]}")
        st = int(input()) - 1
        self.inventory["weapon"].append(self.weapon)
        self.weapon = self.inventory['weapon'][st]
        print("Вы заменили оружие")


class Enemy:
    def __init__(self, lvl):
        enemies = glass["enemies"]
        ch = enemies[rd(0, len(enemies) - 1)]
        self.health = eval(ch["hp"])
        self.act = ch["acts"]
        self.name = ch["name"]
        self.att = self.act[0]
        self.cool = []
        for i in self.act:
            self.cool.append([i["cool"], i["cool"]])

    def attack(self):
        choise = [i for i in range(len(self.cool)) if self.cool[i][0] >= self.cool[i][1]]
        choise = choise[rd(0, len(choise) - 1)]
        self.att = self.act[choise]
        self.cool[choise][0] = 0
        for i in range(len(self.cool)):
            self.cool[i][0] += 1
        return self.att["disc"]


def chest(ch):
    print("Вы нашли сундук")
    item_type = roll(["weapon", "armor"], [30, 10])
    rarity = roll(["common", "uncommon", "legendary"], [4, 6, 2])
    item = glass[item_type][rarity]
    item = item[rd(0, len(item) - 1)]
    print(f"Вы нашли {rarity} {item_type}")
    print(item)
    print("""Взять его?
1. Да
2. Нет""")
    if int(input()) == 1:
        print("Вы взяли предмет")
        if item_type == "armor":
            ch.armor = item
        else:
            ch.inventory["weapon"].append(ch.weapon)
            ch.weapon = item
        return
    else:
        print("Вы не взяли предмет")


def fight(ch):
    return ch.fight()


def forge(ch):
    print("Вы попали в кузню, тут достаточно жарко.")
    if not ch.inventory["weapon"]:
        print("Вы не можете воспользоваться услугами кузнеца \nиз-за отсутствия дополнительного оружия")
        return
    if ch.tocken == 0:
        print("У вас нет токенов, вам тут нечего делать")
        return
    print(f"У вас есть токен({ch.tocken}), потратить один?")
    print("1. Да")
    print("2. Нет")
    st = input()
    if st == "2":
        return
    print("Выберите оружие из которого будет браться характеристика:")
    for i in range(ch.inventory["weapon"]):
        print(f"{i + 1} {ch.inventory['weapon'][i]}")
    st = int(input())



events = [chest, fight]


def cross(ch):
    return roll(events, [10, 90])

    opt = []
    ev = events[:]
    for i in range(roll([1, 2], [40, 60])):
        opt.append(roll)


def stop(ch):
    print("""Желаете остановиться?
1. Да
2. Нет""")
    if input() == "1":
        f = True
        while f:
            print("""Ваши действия
1. Обернуться
2. Перекусить
3. Продолжить путь""")
            st = int(input())
            if st == 1:
                print("""Вы видите как за вами расплываются тьмой ваши следы, 
а мир за вами будто перестаёт существовать""")
            if st == 2:
                ch.health += 20
                print("Вы восстановили 20 здоровья")
    print("Вы продолжили путь")


ch = Chare(cl="knight", name="Чарминг")

ch.intro()

while ch.health > 0:
    roll(events, [10, 90])(ch)

print(f"Вы закончили с уровнем {ch.lvl}")
