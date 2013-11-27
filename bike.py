# _*_ coding: utf-8 *_*

import asc_colors
import os
import sys
import time

colors = asc_colors.asc_colors()

def clear_screen():
	os.system('clear')
	
def print_asterisks():
	print colors.WHITE
	for i in range(0, 114):
		sys.stdout.write("*")
		sys.stdout.flush()
		time.sleep(0.01)

clear_screen()	

print_asterisks()	 
print colors.GREEN + "\n\t\t\t\t\tWelcome to the bike game!"
print_asterisks()

print colors.GREEN +"\n\n\t\t\t\t-------- __@      __@       __@       __@      __~@"
print "\t\t\t\t----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_"
print "\t\t\t\t---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)"
print "\t\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print_asterisks()