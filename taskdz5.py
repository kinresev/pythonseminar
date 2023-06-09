'''Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8'''

def recAdegreeB(a, b):
    if b == 0:
        return 1
    return a * recAdegreeB(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(recAdegreeB(a, b))

'''Задача 28: Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2
4'''

def recsum(a, b):
    if b == 0:
        return a
    return 1 + recsum(a, b - 1)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(recsum(a, b))