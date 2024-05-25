

x = int(input())

sign = "Рабочий стол"

for i in range(0, x): # i пробегает от 0 до x-1. Когда i = x - 1, цикл заканчивается 
    pass

# посчитать сумму квадратов первых 100 чисел

summa = 0

for i in range(1,101):
    summa = summa + i*i
print(summa)

# третий параметр. Рассмотрели два [a,b)

for i in range(1,10,4):
    print(i)
