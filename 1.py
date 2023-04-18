'''
1. Создать программный файл в текстовом формате,
записать в него построчно данные,
вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
'''
def create_file():
    with open("my_file.txt", "w") as f:
        while True:
            text = input()
            f.writelines(text + '\n')
            if text == '':
                f.close()
                break


if __name__ == '__main__':
    create_file()
