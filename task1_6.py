#!/usr/bin/python
#-*-coding:utf8-*-

import itertools

import random

import time
import getpass


#Вспомогательные переменные для демонстрации работы функций и алгоритмов
my_list=[5,6,-4,2,-3,1,5,-4]
my_short_list=[3,8,6]

#
#task1_6_1_a 3 примера list comprehensions, возвращающих итератор
#
#I Модификация списка
def list_comp1(my_list):
	my_list = [element**2 for element in my_list]
	return my_list
#
print list_comp1(my_short_list)

#
#II Содержит условие
def list_comp2(my_list):
	my_list = [element**2 for element in my_list if element%2==0]
	return my_list
#
print list_comp2(my_short_list)

#
#III Использует 2 списка
def list_comp3(my_list1,my_list2):
	my_list= [(element1,element2) for element1 in my_list1 for element2 in my_list2 if element1%element2==0]
	return my_list
#
print list_comp3(my_short_list,my_short_list)

#
#task1_6_1_b 3 примера list comprehensions, возвращающих генератор
#
#I Модификация списка
def list_comp4(my_list):
	my_list = (elem*elem for elem in my_list)
	return my_list
#
for i in list_comp4(my_list):	print i

#
#II Содержит условие
def list_comp5(my_list):
	my_list = (elem*elem for elem in my_list if elem<3)
	return my_list
#
for i in list_comp5(my_list):	print i

#
#III Использует 2 списка
def list_comp6(my_list1,my_list2):
	my_list = (elem1*elem2 for elem1 in my_list1 for elem2 in my_list2 if elem1+elem2>5)
	return my_list
#
for i in list_comp6(my_list,my_list):	print i

#
#task1_6_1_c Минимум 5 примеров работы с itertools
#
#Функция ifilter для фильтрации списка по заданному условию.
for i in itertools.ifilter(lambda x: x<4, my_list): 	print i
#Функция takewhile выбирает значения по заданному условию, до первого нарушения условия.
for i in itertools.takewhile(lambda x: x>0, my_list): 	print i
#Функция permutation составляет все возможные комбинации из элементов итерируемого объекта.
for i in itertools.permutations(my_short_list): 	print i
#Функция combination_with_replacement составляет все возможные комбинации из элементов итерируемого объекта, с повторяющимися элементами, заданной длинны
for i in itertools.combinations_with_replacement('abc',2): 	print i
#Функция product аналогичен вложенным циклам. Данная запись через функцию itertools аналогична записи [(x,y) for x in 'hello' for y in range(3)]. 
#На мой взгляд гораздо короче.
for i in itertools.product('hello',range(3)):	print i

#
#task1_6_2_a Написать функцию, возвращающую несколько значений
#
def func_multi(x):
	return x, x**2
#
print func_multi(2)

#
#task1_6_2_b Пишем генератор
#
#Пример своего генератора
def my_generator(start):
	for item in xrange(random.randrange(start)):
		yield item
#
for item in my_generator(10): print item

#
#task1_6_2_c Примеры использования lambda, nested function и closure
#
#Пример использования lambda function
my_lambda = lambda x: x**2+x
#
print my_lambda(5)

#
#Пример использования nested function
def my_func(x):
	def my_func2(y):
		return y*y
	return my_func2(x)
#
print my_func(5)

#
#Пример использования closure function
def my_func3(x):
	def my_func4(y):
		return x+y
	return my_func4
#
my_x5 = my_func3(5)
print my_x5(3)

#
#task1_6_2_d Примеры использования *args, **kwards, optional и named
#Пример на использование *args
def sample1(name,*args):
	print name
	for arg in args:
		print "-".join(arg)
#
sample1("one","two","three")

#Пример на использование **kwards
def sample2(name,**kwards):
	print name
	for key in kwards:
		print "%s - %s" % (key,kwards[key])
#
sample2(name="one",two="two",three="three")

#Пример на использование optonal и named аргументов
def sample3(one,two="2",three="3"):
	return "%s - %s - %s" % (one,two,three)
#
print sample3("1")
print sample3("1","4")
print sample3("1",three="5")

#
#task1_6_2_e Декораторы
#
#I Декоратор, показывающий время работы функции
def work_time(my_function):
	def my_wrapper(*args):
		start_time=time.time()
		my_function(*args)
		end_time=time.time()
		print "Elapsed time: {:.10f} sec".format(end_time - start_time)
	return my_wrapper
#
@work_time
def fibonaci(max):
	fi = [0, 1]
	for number in range(2, max + 1):
		fi.append(fi[number-1] + fi[number-2])
	print fi
#
fibonaci(10)

#
#II Декоратор, выводящий имя функции перед результатом ее работы
def name_func(my_function):
	def my_wrapper():
		print getattr(my_function,"__name__")
		my_function()
	return my_wrapper
#
@name_func
def haha_func():
	print "haha"
#
haha_func()

#
#III Декоратор, запрещающий выполнение функции, если скрипт запущен не от указанного пользователя
def def_user(my_function):
	def my_wrapper(*args):
		from_name=getpass.getuser()
		if from_name=='admin':
			my_function(args)
		else:
			print "Start from another user"
	return my_wrapper
#
@def_user
def return_my_args(*args):
	print args
#
return_my_args(1)

#
#IV Декоратор. Если функция вернула True, не делает ничего, если вернула строку, выбрасывает исключение, с этой строкой в качестве параметра.
def my_return(my_function):
	def my_wrapper():
		result = my_function()
		if result == True:
			pass
		else:
			raise SyntaxError(result)
	return my_wrapper
#
@my_return
def my_function():
	return True
#
my_function()