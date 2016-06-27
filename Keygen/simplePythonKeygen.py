import random 
import sys
import time

""" 
	Este script en Python nos sirve para crear un simple Keygen para un programa Crackme

	Después de analizarlo con el debugger GDB, hemos observado que el programa testea la 
	licencia introducida con la suma de los caracteres introducidos hasta llegar al valor 916.

	Hacemos un simple script para concatenar caracteres random y hacer que su valor sea
	el valor de comparacion de la licencia del programa, es decir, 916.

	Iker Burguera
"""

def check_key(key):
	char_sum = 0
	for c in key:
		char_sum += ord(c)
	sys.stdout.write("{0:3} | {1}	\r".format(char_sum, key))
	sys.stdout.flush()
	return char_sum

key = ""

while True:
		key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
		s = check_key(key)
		if s > 916:						
			key = ""
		elif s==916:										
			print "-"*100
			print "Found valid key: {0}".format(key)
			print "-"*100
			time.sleep(1)
