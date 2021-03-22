# Урок№5 задание №3
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('task3.txt', 'r', encoding='utf-8') as f:
    salary = {}
    for read_str in f:
        salary[read_str.split()[0]] = float(read_str.split()[1])
    print(salary)
    print("Сотрудники с окладом менее 20 тыс:")
    for name, sal in salary.items():
        if sal < 20000:
            print(name)
    print(f"Средний доход сотрудников равен: {sum(salary.values()) / len(salary)}")
