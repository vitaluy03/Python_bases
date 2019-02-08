# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py


import os
import hw05_easy

def option_1():
    dir_name = input("Укажите название папки")
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
    except Exception:
        print('Такой папки не существует')

def option_3():
    dir_name = input("Укажите название папки")
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.rmdir(dir_path)

def option_4():
    dir_name = input("Укажите название папки")
    dir_path = os.path.join(os.getcwd(), dir_name)
    os.mkdir(dir_path)


command = 'start'
while command != '':
    command = input("Выберите действие: 1-перейти в папку, 2-просмотреть папку, 3-удалить папку, 4-создать папку")
    if command == str(1):
        option_1()
    elif command == str(2):
        hw05_easy.list_current_dir()
    elif command == str(3):
        option_3()
    elif command == str(4):
        option_4()












