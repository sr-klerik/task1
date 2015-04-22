#!/usr/bin/python
import argparse
from sys import version_info
from os import listdir,getlogin
from datetime import datetime


#
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

#
parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-t','--time', action="store_true", help="Print current time")
parser.add_argument('-d','--date', action="store_true", help="Print current date")
parser.add_argument('-u','--uname', action="store_true", help="Print name currnet user")
parser.add_argument('-v','--version', action="store_true",  help="Print current version of python")
parser.add_argument('-T','--tree', action="store_true", help="Print list of file in current directory")
parser.add_argument('--number',action='store', help="Input parameter for function. This function divide 1 on you number")

result=parser.parse_args()
if result.time:
	current_time=datetime.today()
	print current_time.timetz()
if result.date:
	current_date=datetime.today()
	print current_date.date()
if result.uname:
	print getlogin()
if result.version:
	print version_info
if result.tree:
	print listdir(".")

try:
	for_except(int(result.number))
except:
	pass
