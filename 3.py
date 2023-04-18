'''
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32
'''


def count_salary():
    with open('my_file.txt', 'r') as f:
        little_salary = []
        all_salary = []
        name = []
        list = f.read().split('\n')
        for i in list:
            i = i.split()
            try:
                if int(i[1]) < 20000:
                    name.append(i[0])
                all_salary.append(i[1])
            except:
                pass
        f.close()
    return name, all_salary


if __name__ == '__main__':
    arg_name, arg_all_salary = count_salary()
    print('Следующие сотрудники имеют зарплату ниже 20 000:')
    for i in arg_name:
        print(i)

    print(f'Средняя зарплата всех сотрудников состовляет: {sum(map(int, arg_all_salary)) / len(arg_all_salary)}')
