"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from math import pow


def sum_n(n):
    if n == 1:
        return 1
    else:
        result = (1 / (pow(2, (n - 1))) * pow(-1, (n-1)))
        return result + sum_n(n - 1)


num = int(input('Введите число элемнтов последовательности: '))
print(sum_n(num))
# print(sum_n(3))
# print(sum_n(2))
# print(sum_n(1))
