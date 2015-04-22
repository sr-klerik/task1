#!/usr/bin/python
#
def find_string(dict,my_str):
	if my_str in dict:
		dict[my_str]=None
	else: return "String not find in dictionary"
	return dict

#
def merge_dict(dict1,dict2):
	for key,value in dict1.items():
		if key in dict2:
			del dict1[key]
			del dict2[key]
	dict1.update(dict2)
	return dict1

#Deception
def calc(func,oper1,oper2):
	kortezh=('add','multi')
	for key in filter(lambda x: func=='add', kortezh):
		return oper1+oper2
	for key in filter(lambda x: func=="multi", kortezh):
		return oper1*oper2
	

#
def invert(dict):
	for key,value in dict.items():
		dict[value]=key
		del dict[key]
	return dict
##
print find_string({"a":1,"b":2},"a")

print merge_dict({"a":1,"b":2},{"b":2,"c":3})

print calc('add',2,4)

print invert({"a":1,"b":2})
