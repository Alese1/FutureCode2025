n = int(input())
c = 0
for n in range(10,n):
    if n % 2 == 0 and(n % 10 == 4 or n % 10 == 8):
        c += 1
print(c)