# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

path = input('Введите наименования директорий через "\\", в название главной директории должно = 5 символов = ') 
create = input ('Создать директории? y/n= ') 
if create == 'y' or create == 'Y':
       os.makedirs(path)
       print('Директории созданы')

remove = input ('Удалить созданные директории? y/n= ') 
if remove == 'Y' or remove == 'y':
       shutil.rmtree(path[0:5])#кажется я сделал костыль ))
       print('Директории удалены')
else:
       print('Скрипт завершен')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
import shutil

list = os.listdir()
for i in list:
    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil

shutil.copytree('C:\\python\\job\\тренировка', 'C:\\python\\job\\тренировка_backup')




