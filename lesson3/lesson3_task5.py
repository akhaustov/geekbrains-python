# Урок №3 задание №5
# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def func_summ():
    summ = 0
    while 1:
        input_list = input('Введите числа через пробел. Для завершения введите q: ').split()
        for i in input_list:
            if i == 'q':
                print(summ)
                break
            summ += int(i)
        else:
            print(summ)
            continue
        break
    return summ


func_summ()
