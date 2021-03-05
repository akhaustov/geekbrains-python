# Урок № 1 задание №3
# Узнайте у пользователя число упользователя число n. Найдите сумму чисел
# n+nn+nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
#

user_num = input('Введите число: ')

a = user_num+user_num
b = user_num+user_num+user_num

try:
    user_num = int(user_num)
except ValueError:
    print('Расчёт невозможен.')
else:
    a = int(a)
    b = int(b)
    print(user_num+a+b)
