#!/usr/bin/python
import argparse
from sys import version_info
from sys import argv
from os import listdir,getlogin
from datetime import datetime

class AlarmError(Exception):
	def __init__(self,value):
		self.value=value
		self.messages='May be modify your number?'
	def __str__(self):
		return repr(self.messages)

#
def for_except(number):
	try:
		result=1/number
		raise AlarmError(number)
	except ArithmeticError:
		print "You can not divide by zero."
	except AlarmError as a:
		print a
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
parser.add_argument('--number',action='store', type=float, help="Input parameter for function. This function divide 1 on your number")

result=parser.parse_args()
#
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
#
if len(argv) == 1:
	parser.print_help()
else:
	for_except(result.number)
