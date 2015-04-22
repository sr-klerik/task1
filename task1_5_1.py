#!/usr/bin/python
import sys

def for_except(number):
	class Alarm(Exception):
        	def __init__(self,value):
			self.messages="May be modify your number?"

	try:
		result=1/number
		raise Alarm(number)
	except ArithmeticError:
		print "You can not divide by zero."
	except Alarm as a:
		print a.messages
	else:
		print result
	finally:
		print "You number =",number


for_except(1)
