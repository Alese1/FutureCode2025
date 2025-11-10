from random import randint

x = randint(1000, 10000)
x = str(x)

i = 10
while i > 0:
     n = input("Введите ваш код")
     for ii in range(0,4):
         if n[ii] == x[ii]:
             print("совпаденте по", ii,"числу")

