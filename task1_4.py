#!/usr/bin/python
#
def find_string(input_dict,my_str):
	if my_str in input_dict:
		input_dict[my_str]=None
	else: return "String not find in dictionary"
	return input_dict

#
def merge_dict(input_dict1,input_dict2):
	temp=[]
	for key,value in input_dict1.iteritems():
		if key in input_dict2:
			temp.append(key)
	for key in temp:
		del input_dict1[key]
		del input_dict2[key]
	input_dict1.update(input_dict2)
	return input_dict1

#
def calc(function,operand1,operand2):
	output_dict={"add":operand1+operand2,"multi":operand1*operand2,"sub":operand1-operand2,"div":operand1/operand2}
	return output_dict[function]

#
def invert(input_dict):
	temp={}
	for key,value in input_dict.iteritems():
		temp[value]=key
	return temp
##
print find_string({"a":1,"b":2},"a")

print merge_dict({"a":1,"b":2},{"b":2,"c":3})

print calc('add',2,4)

print invert({"a":1,"b":2})
