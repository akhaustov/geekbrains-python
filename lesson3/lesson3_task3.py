# Урок №3 задание №3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(var1, var2, var3):
    if var1 == min(var1, var2, var3):
        return var2 + var3
    elif var2 == min(var1, var2, var3):
        return var1 + var3
    else:
        return var1 + var2


print(my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
              int(input("Введите третье число: "))))
