# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр  123.987
num = input('введите вещественное число: ')
stringNum = num.replace('-', '0')
stringNum = stringNum.replace('.', '0')
listNum = list(stringNum)
i = 0
for i in range (len(listNum)):
    listNum[i] = int(listNum[i])
sum = 0
for i in range (len(listNum)):
    sum = sum + listNum[i]
print(listNum)
print(f'Сумма цифр числа = {sum}')