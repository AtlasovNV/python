__author__ = 'Атласов Николай'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.


print('==Задача 1==')
x = input('x= ')
for y in x:
	print(y * 1)
print ('Конец')
print(' \n  /\_/\ \n ( o.o )\n  = ^ = ')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!
dey = input ('==Показать задачу 2?== (y/n) ')
if dey == 'y':
	print('==Задача 2==')
	num_1 = list(input('Значение num_1: '))
	num_2 = list(input('Значение num_2: '))
	i = input ('==Давайте развернем цифры?== (y/n) ') 
	if i == 'y':
		num_1.reverse()
		num_2.reverse()
		print(num_1,num_2)
		if i == 'n':
			print('До Свидания')
if dey == 'n':
	print('До Свидания')

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"
dey = input ('==Показать задачу 3?== (y/n) ')
if dey == 'y':
	print('==Задача 3==')
	age = int(input('Введите ваш возраст: '))
	if age >= 18:
		print ('Доступ открыт')
	if age < 18:
		print('Извините, пользование данным ресурсом только с 18 лет', ' \n  /\_/\ \n ( o.o )\n  = o = ')
if dey == 'n':
	print('До Свиданияx')