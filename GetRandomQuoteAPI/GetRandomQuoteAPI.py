#--------------------------------------------------------------
#     SCRIPT PARA OBTENER FRASE ALEATORIA con JSON y PYTHON
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

def printQuote(author,quote):
	print "\n" 
	print "-"*150
	print "\t[+] Author :%s" % author
	print "\t[+] Quote  :%s" % quote
	print "-"*150

def getRandomQuote():
	response = urllib2.urlopen('http://quotesondesign.com/api/3.0/api-3.0.json')
	data = json.load(response)                            
	printQuote(str(data['author']),str(data['quote']))
	#print json.dumps(data, indent=4, sort_keys=True) 

#Main
getRandomQuote()
