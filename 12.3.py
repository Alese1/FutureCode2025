
from random import randint
hp = 100
rooms = 4
rooms_content = ["лава", "пустая комнота", "орк"]


while hp > 0 and rooms > 0:
    print("перед тобой три двери какую ты выберишь (1/2/3) ")
    answer = int(input())
    if 0 < answer < 3:
        content = rooms_content[randint(0, len(rooms_content) - 1)]
        print("вам открылась комнота -",content)
        if content != "пустая комнота":
            damage = randint(10, 31)
            hp -= damage
            print("вам нанесен урон", damage, "осталось здоровья", hp)
    rooms -= 1
    print("осталось комнат - ", rooms, "комнот для победы ")
if hp > 0:
    print("вы ввыиграли")
else:
    print("вы проиграли ")