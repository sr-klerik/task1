#!/usr/bin/python
import math

def multipliers(number):
	outlist=[]
	temp=2
	while temp < number:
		if math.fmod(number,temp)==0:
			number/=temp
			outlist.append(temp)
			temp+=1
		else:   temp+=1	
	outlist.append(number)
	return outlist


def equation(a, b, c):
	outlist=[]
	outlist.append((-b+math.sqrt(4*b*c))/2*a)
	outlist.append((-b-math.sqrt(4*b*c))/2*a)
	return outlist


def simple(number):
	temp=2
	result=''
	while temp < number:
		if math.fmod(number,temp)==0:
			result="Not simple"
			break
		temp+=1
	if number==temp:
		result="Simple"
	return result


# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
	noteslist=[100,50,20,10,5,1]
	outlist=[]
	while summ!=0:
		for notes in noteslist:
			outlist.append((summ-math.fmod(summ,notes))/notes)
			summ=math.fmod(summ,notes)
	return outlist


print multipliers(30030)

print equation(1, 3, 3) # 2x^2 + 19x + 35 = 0

print simple(13)

print atm(287)
