import random, string, sys

def menu():
	''' Menu option showing the usage of the script'''
	print "-"*60
	print "Use: python generate.py <length_of_string> <menu_option>"
	print " "
	print "OPTIONS:"
	print "	# 0 - Digits"
	print "	# 1 - Lowercase"
	print "	# 2 - Uppercase"
	print "	# 3 - Digits+Uppercase"
	print "	# 4 - Digits+Lowercase"
	print "	# 5 - Uppercase+Lowercase"
	print "	# 6 - Digits+Uppercase+Lowercase"
	print " "
	print "Example: Generate 5 length Digits+Uppercase(3) string " 
	print ">>>"
	print ">>> python generate.py 5 3"
	print ">>> A4TBS"
	print " "
	print "-"*60

def opcion_elegida(opcion):
	if   opcion == 0:
	    print (random_string_digitos(int(longitud)))
	elif opcion == 1: 
	    print (random_string_minusculas(int(longitud)))
	elif opcion == 2:
	    print (random_string_mayusculas(int(longitud)))
	elif opcion == 3:
	    print (random_string_digitos_mayusculas(int(longitud)))
	elif opcion == 4: 
	    print (random_string_digitos_minusculas(int(longitud)))
	elif opcion == 5: 
	    print (random_string_digitos__mayusculas_minusculas(int(longitud)))
	elif opcion == 6: 
	    print (random_string_digitos__digitos_mayusculas_minusculas(int(longitud)))
	else:
		menu()

def random_string_digitos(length):																# Opcion - 0	Digitos
   return ''.join(random.choice(string.digits) for i in range(length))

def random_string_minusculas(length):															# Opcion - 1 	Minusculas
   return ''.join(random.choice(string.lowercase) for i in range(length))

def random_string_mayusculas(length):															# Opcion - 2    Mayusculas
   return ''.join(random.choice(string.uppercase) for i in range(length))

def random_string_digitos_mayusculas(length):													# Opcion - 3    Digitos + Mayusculas
   return ''.join(random.choice(string.uppercase + string.digits) for i in range(length))

def random_string_digitos_minusculas(length):													# Opcion - 4    Digitos + Minusculas
   return ''.join(random.choice(string.lowercase + string.digits) for i in range(length))

def random_string_digitos__mayusculas_minusculas(length):										# Opcion - 5    Mayusculas + Minusculas
   return ''.join(random.choice(string.lowercase + string.uppercase) for i in range(length))

def random_string_digitos__digitos_mayusculas_minusculas(length):								# Opcion - 6    Digitos + Mayusculas + Minusculas
   return ''.join(random.choice(string.digits + string.lowercase + string.uppercase) for i in range(length))


if len(sys.argv)>1:
	longitud 	= sys.argv[1]
	opcion 		= sys.argv[2]
	opcion_elegida(int(opcion))
else:
	menu()
	exit();



