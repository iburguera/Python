import urllib2																													
import urllib
import json

'''
|-----------------------------------------------|
|[+] Yahoo Weather API Checker                  |
|[+] Written by: Iker Burguera                  |
|[+] Version: 1.0                               |
|[+] Email me @: ikerburguera@gmail.com         |
|-----------------------------------------------|
|[-] https://developer.yahoo.com/weather/       |
|-----------------------------------------------|
'''

#Indicamos que cuidad queremos checkear
ciudad 		= raw_input("Introduce la cuidad de la que quieras saber el tiempo: ")													

#Damos formato  a la consulta a realizar y creamos la URL de la query a la API de Yahoo Weather 
baseurl 	= "https://query.yahooapis.com/v1/public/yql?"
yql_query 	= "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='%s')" % (ciudad)
yql_url 	= baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"

#Guardamos el resultado de la query a la API en la variable result. Nos devuelve un JSON
result 		= urllib2.urlopen(yql_url).read()

#Guardamos en la variable data el resultado con el JSON formateado
data 		= json.loads(result)

#Jugamos con los parametros que queremos mostrar o sacar del resultado data con el JSON
data 		= data['query']['results']['channel']['item']['forecast']

#Imprimimos en la pantalla los resultados
#print data['query']['results']

#Si queremos sacar los datos JSON con formato  e indentados lo haremos de la siguiente forma
print json.dumps(data, indent=4, sort_keys=True)

