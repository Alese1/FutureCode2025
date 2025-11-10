health = int(input("Введите уровень здоровья : "))

if health >= 90:
    print("Персонаж здоров")
elif 70 <= health < 90:
    print("Вам нужно выпить зелье. согласны? (Y/H)")
    answer = input()
    if answer == "Y":
        health += 10
        print("Здоровье увеличено до :", health )
elif 30 <= health < 70:
    print("Вам нужно выпить зелье. согласны? (Y/H)")
    answer = input()
    if answer == "Y":
        health += 30
        print("Здоровье увеличено до :", health )
elif health <30:
    print("Вы  без сознания")