#---------------------------------------------------------------------------------------
#                               SCRIPT LOGIN CREATESPACE
#---------------------------------------------------------------------------------------
#
#	|-----------------------------------------------|
#	|[+] Selenium WebBrowser Python Script Example  |
#	|[+] Written by: Iker Burguera                  |
#	|[+] Version: 4.0                               |
#	|[+] Email me @: ikerburguera@gmail.com         |
#	|-----------------------------------------------|
# 
#---------------------------------------------------------------------------------------
# Based on: http://stackoverflow.com/questions/17540971/how-to-use-selenium-with-python
#---------------------------------------------------------------------------------------

from selenium import webdriver
import time

#Following are optional required
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException

baseurl = "http://www.createspace.com"
username = "ikerburguera@gmail.com"
password = ""

def calcularTotalEuros(dolares,libras,euros):
	number=[dolares*0.8971,libras*1.1780,euros]                         # Agregamos a una lista los valores convertidos a Euros
	return sum(number)

def imprimirInformacionConsola(dolares,libras,euros):
	print "-"*30
	print " Unidades Vendidas: {0}".format(ventas.text)
	print "-"*30
	print " Dolares - \t %s " % (dollars.text)                          # <dollar simbol>+value = <dollar simbol>+53.35
	print " Libras  - \t %s " % (pounds.text)                           # <pound simbol>+value =  <pound simbol>+123.35
	print " Euros   - \t %s " % (euros.text)                            # <euro simbol>+value = <euro simbol>+75.35
	print "-"*30
	print "TOTAL = %2f Euros" % (calcularTotalEuros(float(str(dollars.text[1::])),float(str(pounds.text[1::])),float(str(euros.text[1::]))))   # Pasamos los datos en formato float quitandole el primer caracterer del simbolo de moneda
	print "-"*30

#He sacado un pantallazo (estas en Dropbox) sobre como se saca el xPath usando Firebug. Captura de pantalla 2016-05-16 17.05.17

xpaths = { 'usernameTxtBox' : "/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/form/input[4]",                                    # Campo de Email
           'passwordTxtBox' : "/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/form/input[5]",                                    # Campo de Contrasena	
           'submitButton'   : "/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/form/div/div/div[2]/a",                            # Campo de Boton de Login
           'salesDollar'    : "/html/body/div[2]/div[12]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/span[1]",  # Campo Ventas en Dolares
           'salesPound'     : "/html/body/div[2]/div[12]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/span[1]",  # Campo Ventas en Libras
           'salesEuro'      : "/html/body/div[2]/div[12]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/span[1]",  # Campo Ventas en Euros
           'UnitSold'       : "/html/body/div[2]/div[12]/div/div[2]/div[13]/div[2]/div/table/tfoot/tr[2]/td[2]"                 # Campo Unidades Vendidas
         }

profile = webdriver.FirefoxProfile()                                          # Creamos el WebDriver con Firebox 
profile.accept_untrusted_certs = True
mydriver = webdriver.Firefox(firefox_profile=profile)
mydriver.get(baseurl)                                                         # Asignamos el URL al webDriver para que pueda trabajar con ello
mydriver.maximize_window()                                                    # Ponemos la ventana a maxima resolucion

mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()              # Limpiamos el campo de Email si tenemos puesto el Remember me
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)  # Mandamos el dato Email
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()              # Limpiamos el campo de Password si tenemos puesto el Remember me
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)  # Mandamos el dato Password

mydriver.find_element_by_xpath(xpaths['submitButton']).click()                # Hacemos click en el boton

#mydriver.close()

dollars = mydriver.find_element_by_xpath(xpaths['salesDollar'])             # Obtenemos el valor de las ventas realizadas en Dolares
pounds  = mydriver.find_element_by_xpath(xpaths['salesPound'])              # Obtenemos el valor de las ventas realizadas en Libras
euros   = mydriver.find_element_by_xpath(xpaths['salesEuro'])               # Obtenemos el valor de las ventas realizadas en Euros
ventas  = mydriver.find_element_by_xpath(xpaths['UnitSold'])                # Obtenemos el numero de ventas realizadas en el Mes

imprimirInformacionConsola(dollars,pounds,euros)






