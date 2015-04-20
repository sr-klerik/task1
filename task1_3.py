#!/usr/bin/python

def iteration(list):	
	result=[]
	for element in list:
		if list.count(element) > 1:
			if element in result: continue
			else: result.append(element)
	return result


def statistics(list):
	pass


def end_sort(list):
	pass


def insert_in_sort(list,string):
	pass


def insert_in_list(list1,list2,element):
	pass


def remove_odd_str(string):
	pass


def find_sequence(list):
	pass



print iteration(['adf','afs','fsa','adf'])
