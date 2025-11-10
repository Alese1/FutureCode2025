money = int(input())
persent = 0.1

year = 5

while year > 0 :
  delta = money * persent
  money += delta
  year -=1

print(int(money))