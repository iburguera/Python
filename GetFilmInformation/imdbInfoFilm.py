#coding=utf-8

#--------------------------------------------------------------
#         SCRIPT INFORMACION PELICULAS con JSON y PYTHON
#--------------------------------------------------------------
# 
# Author  : Iker Burguera
# Date    : 19/07/2016
# Version : 1.0
#
#--------------------------------------------------------------
# http://www.omdbapi.com/?t=<film>&y=&plot=full&r=json
#--------------------------------------------------------------

import urllib2
import json

def printFilmInformation(title,director,actors,year,rating):
	print "\n" 
	print "-"*150
	print "\t[+] Titulo     :\t%s" % title
	print "\t[+] Director   :\t%s" % director
	print "\t[+] Actores    :\t%s" % actors
	print "\t[+] Año        :\t%s" % year
	print "\t[+] Puntuación :\t%s" % rating	
	print "-"*150

def getFilmInformation(urlFilm):
	response = urllib2.urlopen(url)
	data = json.load(response)                            
	#printQuote(str(data['author']),str(data['quote']))
	printFilmInformation(str(data['Title']),str(data['Director']),str(data['Actors']),str(data['Year']),str(data['imdbRating']))
	#print json.dumps(data, indent=4, sort_keys=True) 

#Main

try:
  film = raw_input("Introduce el nombre de la pelicula que quieras conseguir informacion: ")
  url  = "http://www.omdbapi.com/?t="+film+"&y=&plot=full&r=json" 
	getFilmInformation(url)
except:
	print " :(  - Ha habido un error en la petición . asegúrate de escribir bien el nombre de la película"
