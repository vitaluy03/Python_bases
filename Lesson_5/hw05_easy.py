# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
"""
import os
def make_dirs():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            # Создаем новую директорию
            os.mkdir(dir_path)
            print(f'Создана директория: dir_{i}')
        except FileExistsError:
            print(f'Такая директория уже существует: dir_{i}')

def remove_dirs():
    for i in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        try:
            # Удаляем существующую пустую директорию
            os.rmdir(dir_path)
            print('Удалена директория: {dir_path}')
        except FileNotFoundError:
            print('Такой директории не существует: {dir_path}')

make_dirs()
#remove_dirs()
"""

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
"""
import os
def list_current_dir():
    dirs = os.listdir(path=os.getcwd())
    print('Список файлов в текущей директории:')
    for dir in dirs:
         if os.path.isdir(dir):
          print(dir)
list_current_dir()

"""

# Задача-3:
#Здесь  я не разобрался. это скрипт создает пустую копию и с оригинала все удалает

"""
import os

def copy_file():
    f = open('copy_hw_05_easy.py.', 'x')
    os.system('copy copy_hw_05_easy.py hw05_easy.py')
copy_file()
"""
