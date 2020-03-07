#Case 7
# Develop - Kuznecov B - 60% Odoevcev S - 35% Makarov A - 5%

import os
import local
import stat


def countFiles(path):
    cnt = 0
    try:
        for i in os.listdir(path):
            j = os.path.join(path, i)
            if stat.S_ISDIR(os.stat(j)[stat.ST_MODE]):
                cnt += countFiles(j)
            elif stat.S_ISREG(os.stat(j)[stat.ST_MODE]):
                cnt += 1
        print(f'----------------------\nКоличество файлов в этом каталоге  - {cnt}')
        main()
    except FileNotFoundError:
        print('----------------------\n')
        print('!Ошибка, некорректный ввод дериктории!')
        main()


def findFiles(target, path):
    lst = []
    for i in os.listdir(path):
        j = os.path.join(path, i)
        if stat.S_ISDIR(os.stat(j)[stat.ST_MODE]):
            lst.extend(findFiles(target, j))
        elif stat.S_ISREG(
                os.stat(j)[stat.ST_MODE]) and target in i:  # Проверка что это файл и в названии содержит target
            lst.append(j)
    print(lst)
    main()


def moveUp():
    ok_new = str(os.getcwd())[::-1]
    slash_ind = ok_new.find('/')
    new_cat = ok_new[slash_ind:]
    os.chdir(new_cat[::-1])
    main()


def moveDown(dir):
    try:
        os.chdir(f'{os.getcwd()}/{dir}')
        main()
    except FileNotFoundError:
        print('----------------------\n')
        print('!Ошибка, некорректный ввод дериктории!')
        main()


def runCommand(command):
    if command == 2:
        print(moveUp())
    elif command == 3:
        dir = input('Введите имя директории - ')
        moveDown(dir)
    elif command == 4:
        ff = input('Введите имя директории')
        countFiles(ff)
    elif command == 5:
        byt = input('Введите имя директории - ')
        print(countBytes(byt))
    elif command == 6:
        print('Мы не знаем как это сделать')
        main()
    elif command == 7:
        print('Программа остановленна')
        quit()
    elif command == 1:
        print(os.listdir(os.getcwd()))
        main()
    main()


def acceptCommand():
    print('Введите номер команды - ')
    try:
        command_input = int(input())
    except ValueError:
        print('----------------------\n')
        print('!Ошибка ввода!')
        main()
    return command_input


def main():
    print('----------------------\n')
    print(f'Текущий каталог - {os.getcwd()}')
    print(local.MENU)
    command = acceptCommand()
    runCommand(command)


x = main()
