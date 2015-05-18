#!/usr/bin/python
#-*-coding:utf8-*-

import itertools


#Вспомогательные переменные для демонстрации работы функций и алгоритмов
my_list=[5,6,-4,2,-3,1,5,-4]
my_short_list=[3,8,6]


#task1_6_1_a
#3 примера list comprehensions, возвращающих итератор
#
def list_comp1(my_list):
	my_list = [element**2 for element in my_list]
	return my_list

#
def list_comp2(my_list):
	my_list = [element**2 for element in my_list if element%2==0]
	return my_list

#
def list_comp3(my_list1,my_list2):
	my_list= [(element1,element2) for element1 in my_list1 for element2 in my_list2 if element1%element2==0]
	return my_list

#Функции для демонстрации работы алгоритмов по заданию task1_6_1_a. Раскомментировать при необходимости.
#print list_comp1(my_list)
#print list_comp2(my_list)
#print list_comp3(my_list,my_list)


#task1_6_1_b
#3 примера list comprehensions, возвращающих генератор
#
def list_comp4(my_list):
	my_list = (elem*elem for elem in my_list)
	return my_list

#
def list_comp5(my_list):
	my_list = (elem*elem for elem in my_list if elem<3)
	return my_list

#
def list_comp6(my_list1,my_list2):
	my_list = (elem1*elem2 for elem1 in my_list1 for elem2 in my_list2 if elem1+elem2>5)
	return my_list

#Функции для демонстрации работы алгоритмов по заданию task1_6_1_b. Раскомментировать при необходимости.
#for i in list_comp4(my_list):	print i

#for i in list_comp5(my_list):	print i

#for i in list_comp6(my_list,my_list):	print i

#task1_6_1_c
#Минимум 5 примеров работы с itertools
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

#task1_6_2_a
#Several value in function
def func_multi(x):
	return x, x**2

print func_multi(2)

#task1_6_2_b
#My generator
def my_generator():
	item = [5,4]
	return item

for i in my_generator(): print i


#task1_6_2_c
#Lambda
my_lambda = lambda x: x**2+x
#Nested
def my_func(x):
	def my_func2(y):
		return y*y
	return my_func2(x)
#Closure
def my_func3(x):
	def my_func4(y):
		return x+y
	return my_func4
#
print my_lambda(5)
#
print my_func(5)
#
my_x5 = my_func3(5)
print my_x5(3)

#task1_6_1_d
#