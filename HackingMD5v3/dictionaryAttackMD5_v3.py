
import md5
import sys
import os


def banner():
	print '''
	|-----------------------------------------------|
	|[+] MD5 Password HASH Dictorionary Attack      |
	|[+] Written by: Iker Burguera                  |
	|[+] Version: 3.0                               |
	|[+] Email me @: ikerburguera@gmail.com         |
	|-----------------------------------------------|
	'''
	print "\nUso:"
	print "-"*90
	print "%s \t--hashFile [md5HashFile]\t --dictionary [dictionaryPath]" % sys.argv[0]
	print "-"*90


def uso():
  if len(sys.argv) <4 or sys.argv[1]!='--hashFile' or sys.argv[3]!='--dictionary':
    banner()
    sys.exit(1)

uso()

commandHash  = sys.argv[1]											# Recogemos el comando '--hash' de la consola
commandDict  = sys.argv[3]											# Recogemos el comando '--dictionary' de la consola

contador  = 1
cracked   = 0
numHashes = 0
hashFound = 0

hashNotFound=""

banner()

if commandHash == '--hashFile' and commandDict == '--dictionary' :      # Comprobamos que han introducido bien los comandos
	md5HashFile         = sys.argv[2]
	dictionaryPath   	= sys.argv[4]

	print "MD5 Hash Decryting..."

	try:
		hashFile = open(md5HashFile,"r")
	except:
		print "\nFichero no encontrado."
		print "CommandHash: %s " % sys.argv[1]
		print "CommandDict: %s " % sys.argv[3]
		quit()

	for hashmd5 in hashFile:
		try:
			pwfile = open(dictionaryPath,"r")
		except:
			print "\nFichero no encontrado."
			print "CommandHash: %s " % sys.argv[1]
			print "CommandDict: %s " % sys.argv[3]
			quit()

		for password in pwfile:													  	  # Recorremos todo el fichero de palabras para obtener el Hash y compararlo con el que hemos introducido
			filemd5 = md5.new(password.strip()).hexdigest()			# Cogemos solamente la palabra del fichero y la convertimos en Hash MD5
			if hashmd5.strip() == filemd5:											# Comparamos el Hash introducido y el Hash de la palabra del diccionario y las comparamos 
				print " [+] %s\t->\t%s" % (hashmd5.rstrip(),password.rstrip())
				cracked +=1
				hashFound=1
				pwfile.close()
				break
			else:
				hashFound=0
		if hashFound == 0:
			hashNotFound = hashNotFound+"\n"+hashmd5.strip()
		else:
			hashFound=1
		numHashes+=1
	hashFile.close()	

print ""
print "-"*90
print "Cracked MD5 Hashes       : (%d/%d) " % (cracked,numHashes)
print "-"*90
print "-"*90
print "Unable to get MD5 Hashes :         " 
print "-"*90
print hashNotFound
print "-"*90
