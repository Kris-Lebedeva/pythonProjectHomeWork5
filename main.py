# This is a sample Python script.
# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def chek(number):
#     for i in range(2, number):
#         if number%i == 0:
#             return (f"No")
#         return (f"Yes")
# number = int(input ("Ввeдите число: "))
# res = chek(number)
# print(res)

# Задача №37.
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def reverse_sequence(n):
    if n > 1:
        reverse_sequence(n-1)
    x = int(input())
    print(x, end=' ')

reverse_sequence(int(input()))