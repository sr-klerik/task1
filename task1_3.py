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
	list.sort(key=lambda letter: letter[-1])
	return list

def insert_in_sort(list,string):
	pass


def insert_in_list(list1,list2,element):
	if element in list1:
		list2.insert(list1.index(element),element)
	return list2
	

def remove_odd_str(big_string):
	temp=[]
	for word in big_string.split(" "):
		if len(word)%2==0:
			temp.append(word)
	return " ".join(temp)


def find_sequence(list):
	pass



print iteration(['adf','afs','fsa','adf'])

print end_sort(["Hello","How are you","I'm fine","And","Right"])

print insert_in_list(['asd','vre','gfd','ldkdf','sdf','vtr'],['sdfa','nhc','xgf','bng'],'gfd')

print remove_odd_str("Bears are the best animals ever")
