# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
n = int(input('Введите число  '))
if n == 0:
    print('ошибка, делить на 0 нельзя')
listN = []
for i in range (n):
    listN.append((1+1/(i+1))**(i+1))
print(listN)
sum = 0
for i in range (n):
    sum += listN[i]
print(sum)