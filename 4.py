'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One - 1
Two - 2
Three - 3
Four - 4
Напишите программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''


def replace():
    numer = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_file = []
    with open('my_file.txt', 'r') as f:
        for line in f:
            line = line.split(' - ', 1)
            new_file.append(numer[line[0]] + '  ' + line[1])
        f.close()

    with open('my_new_file.txt', 'w') as f:
        f.writelines(new_file)


if __name__ == '__main__':
    replace()
