import md5
import sys
import os


def banner():
	print '''
	|-----------------------------------------------|
	|[+] MD5 Password HASH Dictorionary Attack      |
	|[+] Written by: Iker Burguera                  |
	|[+] Version: 2.0                               |
	|[+] Email me @: ikerburguera@gmail.com         |
	|-----------------------------------------------|
	'''
	print "\nUso:"
	print "-"*90
	print "%s \t--hass [md5Hash]\t --dictionary [dictionaryPath]" % sys.argv[0]
	print "-"*90


def uso():
  if len(sys.argv) <4 or sys.argv[1]!='--hash' or sys.argv[3]!='--dictionary':
    banner()
    sys.exit(1)

      

uso()

commandHash  = sys.argv[1]											# Recogemos el comando '--hash' de la consola
commandDict  = sys.argv[3]											# Recogemos el comando '--dictionary' de la consola

contador = 1

banner()

if commandHash == '--hash' and commandDict == '--dictionary' :      # Comprobamos que han introducido bien los comandos
	md5HashToCrack      = sys.argv[2]
	dictionaryPath   	= sys.argv[4]

	try:
		pwfile = open(dictionaryPath,"r")
	except:
		print "\nFichero no encontrado."
		print "CommandHash: %s " % sys.argv[1]
		print "CommandDict: %s " % sys.argv[3]
		quit()

	for password in pwfile:														# Recorremos todo el fichero de palabras para obtener el Hash y compararlo con el que hemos introducido
		filemd5 = md5.new(password.strip()).hexdigest()							# Cogemos solamente la palabra del fichero y la convertimos en Hash MD5
		#banner()																# Es para verlo mas limpio y cool. Si lo descomentamos perdemos velocidad
		print "Probando Password numero %d: %s " % (contador,password.strip())
		#os.system('clear')														# Es para limpiar la pantalla

		contador +=1

		if md5HashToCrack == filemd5:													# Comparamos el Hash introducido y el Hash de la palabra del diccionario y las comparamos 
			print "-"*70
			print "\tPassword encontrado!"
			print "-"*70
			print ""
			print " [+] Hash : %s" % md5HashToCrack
			print " [+] Pass : %s" % password.rstrip()							# Imprimimos el passwor sin el retorno de carro
			print ""
			print "-"*70
			break

	else:	print "Password no encontrado :("


else:																# Si los comandos no son correctos les mostramos como se usa-> uso()
	uso()





