# Урок №1 задание №4
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

num = int(input('Введите целое положительное число: '))

max=0
n = num

while num > 0:
    n = num % 10
    num = num / 10
    if max < n:
        max = n

print("Максимальная цифра в числе: ", max)
