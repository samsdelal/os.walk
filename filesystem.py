import os
import local


def countFiles(dir):
    name_files = []

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
    """for root, dirs, files in os.walk(os.getcwd()):
        print(root)"""


x = main()
