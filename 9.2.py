from operator import truediv
from random import randint

x = randint(0,11)
i = 5
while i<=5 :
    i -= 1
    n = int(input("Введите ваш число"))
    if n == x:
        print("Дверь открыт")
    else:
        print("Код не подошел... попробуйте еще раз отсалось",i,"попыток")


