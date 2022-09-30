# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n = int(input('Введите число  '))
listN = [1]
for i in range (1, n):
    listN.append((i+1)*listN[i-1])
print(listN)