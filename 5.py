'''
5. Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''


def create_file():
    text = input()
    with open('my_file.txt', 'w') as f:
        number = text.split(' ')
        true_number = []
        for i in number:
            if i.isdigit():
                f.writelines(f'{i} ')
                true_number.append(i)
        f.close()
        print(f'Сумма всех чисел равна {sum(map(int, true_number))}')


if __name__ == '__main__':
    create_file()
