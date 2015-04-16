#!/usr/bin/python

import random

def letters(big_string):
	result=""
	if big_string.istitle():
		for temp in big_string:
			if 'A'<=temp<='Z':
				result+=temp
	return result


def palindrome(pali):
	temp=0
	while temp < len(pali)/2-1:
		if pali[temp]==pali[-temp-1]:
			temp+=1
			result="True"
		else: 
			result="False" 
			break
	return result


def find_letter(where, letter):
	result=[]
	temp=where.split(" ")
	for word in temp:
		if word[0]==letter or word.lower()[0]==letter or word.upper()[0]==letter:
			result.append(word)
	return result


def mix_words(just_string):
	result=""
	temp=just_string.split(" ")
	while temp:
		i=random.randrange(len(temp))
		result+=temp.pop(i)+" "
	return result.capitalize()


print letters("Trees Are So Kind")

print palindrome("avidsf fsdiva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")
