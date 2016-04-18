#--------------------------------------------------------------
#		       SCRIPT PARA OBTENER IP PUBLICA con JSON
#--------------------------------------------------------------
# 
# Author  : Iker Burguera
# Date    : 18/04/2016
# Version : 1.0
#
# Note    : Read README.MD For further instructions
#--------------------------------------------------------------

import urllib2
import json

def printIP(ip):
	print "\n" 
	print "-"*150
	print "[+] %s" % ip
	print "-"*150

def getIP():
	response = urllib2.urlopen('http://jsonip.com/')
	data = json.load(response)                            # Response -> {"ip":"XX.XX.XX.XX","about":"/about","Pro!":"http://getjsonip.com"}
	printIP(str(data['ip']))
	#print json.dumps(data, indent=4, sort_keys=True)     # Esto es para imprimirlo bonito por consola

#Main
getIP()
