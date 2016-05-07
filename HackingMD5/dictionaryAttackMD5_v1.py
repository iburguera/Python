'''
|-----------------------------------------------|
|[+] MD5 Password HASH Dictorionary Attack      |
|[+] Written by: Iker Burguera                  |
|[+] Version: 1.0                               |
|[+] Email me @: ikerburguera@gmail.com         |
|-----------------------------------------------|
'''

import md5

contador = 1

pass_in = raw_input("Introduce el Hash MD5: ")
pwfile  = raw_input("Introduce el diccionario de passwords: ")

try:
	pwfile = open(pwfile,"r")
except:
	print "\nFichero no encontrado."
	quit()

for password in pwfile:																# Recorremos todo el fichero de palabras para obtener el Hash y compararlo con el que hemos introducido
	filemd5 = md5.new(password.strip()).hexdigest()									# Cogemos solamente la palabra del fichero y la convertimos en Hash MD5
	print "Probando Password numero %d: %s " % (contador,password.strip())
	contador +=1

	if pass_in == filemd5:															# Comparamos el Hash introducido y el Hash de la palabra del diccionario y las comparamos 
		print "-"*120
		print "\tPassword encontrado!"
		print "-"*70
		print ""
		print " [+] Hash : %s" % pass_in
		print " [+] Pass : %s" % password.rstrip()									# Imprimimos el passwor sin el retorno de carro
		print ""
		print "-"*70
		break

else:	print "Password no encontrado :("

