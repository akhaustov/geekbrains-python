# Урок №2 задание №1
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list = [1, 25.2, True, None, "Text"]

for l in list:
    print("Тип переменной",l ,'это', type(l).__name__)
