#!/usr/bin/python

import random

def letters(big_string):
	result=[]
	for temp in big_string:
		if temp.isupper():
			result.append(temp)
	return " ".join(result)


def palindrome(pali):
	if pali==pali[::-1]:
		return "True"
	else: return "False"		


def find_letter(where, letter):
	result=[]
	temp=where.split(" ")
	for word in temp:
		if word[0]==letter or word.lower()[0]==letter or word.upper()[0]==letter:
			result.append(word)
	return result


def mix_words(just_string):
	temp=just_string.split(" ")
	random.shuffle(temp)
	return " ".join(temp)


print letters("Trees Are So Kind")

print palindrome("avid diva")

print find_letter("Bears are the best animals ever", 'b')

print mix_words("Bears are the best animals ever")
