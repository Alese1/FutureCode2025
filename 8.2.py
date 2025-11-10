a = int(input("Введите значение числа a"))
b = int(input("Введите значение числа b "))
c = int(input("Введите значение числа c "))

if a**2 + b**2 == c**2:
    print("Прямоугольный")
elif a**2 + b**2 < c**2:
    print("Тупоугольный")
elif a**2 + b**2 > c**2:
    print("Остроугольный")
elif a+b<=c or a+c<=b or c+b<=a:
    print("Не существует")