from operator import truediv
from random import randint

x = randint(1000,10000)
is_guess = False
while not is_guess:
    n = int(input("Введите ваш код"))
    if n == x:
        print("Сундук открыт")
        is_guess = True
    elif n ==0:
        is_guess = True
        print("Код - ",x)
    else:
        print("Код не подошел... попробуйте еще раз")

