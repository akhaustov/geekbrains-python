# Урок№5 задание №4
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator

with open('task4_rus.txt', 'w', encoding='utf-8') as f_new:
    with open('task4.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        f_new.write(Translator().translate(text, dest='ru').text)
