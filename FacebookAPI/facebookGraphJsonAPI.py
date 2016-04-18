#----------------------------------------------------------------------------
#		       SCRIPT PARA DESCARGARSE IMAGENES DE FACEBOOK
#----------------------------------------------------------------------------
# 
# Author  : Iker Burguera
# Date    : 18/04/2016
# Version : 1.0
#
# 1- Obtener el ACCESS TOKEN de la siguiente direccion : 
#      - https://developers.facebook.com/tools/explorer/
#      - Elegir 
#
# 2- Obtener los ALBUMES que tienes en Facebook
#      - https://graph.facebook.com/me/albums?access_token=<TU_TOKEN>
#      - Nos devuelve el ALBUM_ID de cada ALBUM en formato JSON
#
# 3- Obtener las FOTOS de cada ID del Album
#      - https://graph.facebook.com/<ALBUM_ID>/photos?access_token=<TU_TOKEN>
#----------------------------------------------------------------------------

import urllib2
import urllib
import json
import time

access_token 	= "<TU TOKEN>"
album_URL	= "https://graph.facebook.com/me/albums?access_token=%s" % access_token

def printAlbums(albums,lengthAlbum):
	""" Funcion para mostrar las propiedades de cada album """
	for album in range(0,lengthAlbum):
		print "-"*120
		print "[+] Name     : \t"+albums['data'][album]['name']
		print "[+] Time     : \t"+albums['data'][album]['updated_time']
		print "[+] Count    : \t"+str(albums['data'][album]['count'])
		print "[+] ALBUM ID : \t"+albums['data'][album]['id']
		print "[+] Album URL: \t"+albums['data'][album]['link']
		print ""*120
		getPictures(albums['data'][album]['id'],albums['data'][album]['name'])
		print ""*120
		print "-"*120

def printPicturesURL(albumID,albumName,lengthPictures):										
	""" Funcion para mostrar las URL de de las imagenes segun el Album ID"""
	cont = 0

	for picture in range(0,lengthPictures):
		unparsedPicture = albumID['data'][picture]['source']
		print "\t [-] " + albumID['data'][picture]['source']
		downloadAlbumPictures(albumName,unparsedPicture,str(albumID['data'][picture]['id']),cont)
		cont+=1
	print ""
	print "Contador imagenes obtenidas : " + str(cont)

def getAlbums(albums):
	""" Funcion para obtener todos los albumes de Facebook."""
	response = urllib2.urlopen(albums)
	data = json.load(response)  
	printAlbums(data,len(data['data']))
	

def getPictures(albumID,albumName):
	""" Funcion para obtener las URL de de las imagenes segun el Album ID   """
	""" 																	"""
	""" 18/04/2016 - Hay un limite de consulta de 100 items"""
	"""            - http://stackoverflow.com/questions/6718422/getting-more-than-25-photos-from-the-facebook-graph-api"""
	""" 19/04/2016 - Podemos utilizar la opcion PAGING NEXT para obtener la siguiente URL con las fotos"""

	pictures_URL = "https://graph.facebook.com/%s/photos?access_token=%s&limit=5000" % (albumID,access_token)
	response = urllib2.urlopen(pictures_URL)	
	data = json.load(response) 
	printPicturesURL(data,albumName,len(data['data'])) 

def downloadAlbumPictures(albumName,pictureURL,pictureID,cont):
		name = ""+albumName+"-"+pictureID+"-"+str(cont)+".jpg"
		f = open(name,'wb')
		f.write(urllib.urlopen(pictureURL).read())
		f.close()
		time.sleep(.5)

#Main

getAlbums(album_URL)
