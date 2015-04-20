#!/usr/bin/python
#
def iteration(list):	
	result=[]
	for element in list:
		if list.count(element) > 1:
			if element in result: continue
			else: result.append(element)
	return result

#
def statistics(list):
	type_dictionary={}
	for element in list:
		if type(element) in type_dictionary:
			type_dictionary[type(element)]+=1
		else:
			type_dictionary[type(element)]=1
	return type_dictionary

#
def end_sort(list):
	list.sort(key=lambda letter: letter[-1])
	return list

#
def insert_in_sort(list,string):
	for element in list:
		if element[-1]>string[-1]:
			list.insert(list.index(element),string)
			break
	return list

#
def insert_in_list(list1,list2,element):
	if element in list1:
		list2.insert(list1.index(element),element)
	return list2
	
#
def remove_odd_str(big_string):
	temp=[]
	for word in big_string.split(" "):
		if len(word)%2==0:
			temp.append(word)
	return " ".join(temp)


#Too difficult
def find_sequence(list):
	temp=[]
	out_list=[]
	for number in list:
		temp.append(number)
		if temp == range(temp[0],number+1):
			if len(temp)>len(out_list):
                                out_list=temp
		else:
			temp.pop()
			if len(temp)>len(out_list):
				out_list=temp
			temp=[]
			temp.append(number)
	return out_list


print iteration(['adf','afs','fsa','adf'])

print statistics([['vsdf',[1,"df"]],'sdc',4.12,[3.4,'assf'],'w','Dow',123,3.5])

print end_sort(["Hello","How are you","I'm fine","And","Right"])

print insert_in_sort(["And", "I'm fine", "Hello", "Right", "How are you"],"Gas")

print insert_in_list(['asd','vre','gfd','ldkdf','sdf','vtr'],['sdfa','nhc','xgf','bng'],'gfd')

print remove_odd_str("Bears are the best animals ever")

print find_sequence([1,2,3,5,7,8,9,10,11,12])
