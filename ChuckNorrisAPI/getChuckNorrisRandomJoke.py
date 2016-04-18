#----------------------------------------------------------------------------
#		       SCRIPT PARA OBTENER CITAS SOBRE CHUCK NORRIS
#----------------------------------------------------------------------------
# 
# Author  : Iker Burguera
# Date    : 18/04/2016
# Version : 1.0
#
# Note    : Read README.MD For further instructions
#----------------------------------------------------------------------------

import urllib2
import json

def printRandomJoke(joke):
	print "\n" 
	print "-"*150
	print "[+] - %s" % joke
	print "-"*150

def getRandomJoke():
	response = urllib2.urlopen('http://api.icndb.com/jokes/random')
	data = json.load(response) 
	printRandomJoke(str(data['value']['joke']))
  #print json.dumps(data, indent=4, sort_keys=True) 

#Main
getRandomJoke()
