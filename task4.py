# Реализуйте алгоритм перемешивания списка.
array = [1, 2, 3, 4, 5]
import random
for i in range (len(array)):
    j = random.randint(0, len(array)-1)  # случайный выбор индекса
    elem = array.pop(j)  #удаление элемента с выбранным индексом
    array.append(elem)  #вставка удаленного элемента в список
print(array)
