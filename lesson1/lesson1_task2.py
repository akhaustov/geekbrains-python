# Урок №1 задание №2
# пользователь воодит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в
# формате "чч:мм:сс". Используйте форматирование строк.

#import datetime
user_input = int(input('Введите время в секундах: '))
#
#print(str(datetime.timedelta(seconds=user_input)))

hh = user_input // 3600
mm = user_input % 10000 // 60
ss = user_input % 60

print(f"{hh:02}:{mm:02}:{ss:02}")
