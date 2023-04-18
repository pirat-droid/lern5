'''
2. Создать текстовый файл (не программно),
сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
'''


def count_lines():
    with open('my_file.txt', 'r') as f:
        l = 0
        for line in f:
            l += 1
        f.close()
    return l


def count_word():
    with open('my_file.txt', 'r') as f:
        arg_w = []
        for line in f:
            arg_w.append(len(line.split()))
        f.close()
    return arg_w


if __name__ == '__main__':
    line = count_lines()
    print(f'количество строк в файле - {str(line)}')
    arg_w = count_word()
    line = 1
    for word in arg_w:
        print(f'количество слов в {line} строке - {str(word)}')
        line += 1
