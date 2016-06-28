# coding=utf-8

from ftplib import FTP                                                                      # Importamos la libreria ftplib desde FTP

import sys

def imprimirMensaje():                                                                      # Definimos la funcion para Imprimir el mensaje de bienvenida
    print "------------------------------------------------------"
    print "--               COMMAND LINE EXAMPLE               --"
    print "------------------------------------------------------"
    print ""
    print ">>>             Cliente FTP  en Python                "
    print ""
    print ">>> python <appname>.py <host> <port> <user> <pass>   "
    print " Iker Burguera     v0                                 "
    print "------------------------------------------------------"

def f(s):                                                                                   # Funcion para imprimir por pantalla los datos 
    print s

def download(j):                                                                            # Funcion para descargarnos el fichero que indiquemos según numero    
    print "Descargando=>",files[j]      
    fhandle = open(files[j], 'wb')
    ftp.retrbinary('RETR ' + files[j], fhandle.write)                                       # Imprimimos por pantalla lo que estamos descargando        #fhandle.close()
    fhandle.close()                                                     

ip          = sys.argv[1]                                                                   # Recogemos la IP       desde la linea de comandos sys.argv[1] 
puerto      = sys.argv[2]                                                                   # Recogemos el PUERTO   desde la linea de comandos sys.argv[2]
usuario     = sys.argv[3]                                                                   # Recogemos el USUARIO  desde la linea de comandos sys.argv[3]
password    = sys.argv[4]                                                                   # Recogemos el PASSWORD desde la linea de comandos sys.argv[4]


ftp = FTP(ip)                                                                               # Creamos un objeto realizando una instancia de FTP pasandole la IP
ftp.login(usuario,password)                                                                 # Asignamos al objeto ftp el usuario y la contraseña

files = ftp.nlst()                                                                          # Ponemos en una lista los directorios obtenidos del FTP

for i,v in enumerate(files,1):                                                              # Imprimimos por pantalla el listado de directorios enumerados
    print i,"->",v

print ""
i = int(raw_input("Pon un Nº para descargar el archivo or pulsa 0 para descargarlos\n"))    # Introducimos algun numero para descargar el fichero que queramos. Lo convertimos en integer

if i==0:                                                                                    # Si elegimos el valor 0 nos decargamos todos los ficheros del directorio                                                                               
    for j in range(len(files)):                                                             # Hacemos un for para la lista files y
        download(j)                                                                         # llamamos a la funcion download para descargar los ficheros
if i>0 and i<=len(files):                                                                   # Si elegimos unicamente un numero para descargarnos el elemento nos lo descargamos. Comprobamos que sea mayor de 0 y menor que la longitud de files 
    download(i-1)                                  
