# Selenium Python Createspace

Vamos a utilizar este script en Python para obtener la información de ventas de la páginas [Createspace](https://www.createspace.com/)

En el código solamente tenemos que modificar los siguientes valores:

```python
...
baseurl = "http://www.createspace.com"        # Login a la pagina de Createspace
username = "<nuestroCorreo>"                  # Introducimos nuestro correo electrónico
password = "<nuestroPassword>"                # Introducimos nuestro Password
...
```

Una vez modificado, ejecutamos el script

```python
>>> python loginCreatespacePython2.py
```

El resultado muestra el Top10 de los libros más vendidos de [ARBI](http://www.arbibook.com/) junto con el Total de Ventas en Divisas, Libros y el Calculo en Euros Total del Mes.

```bash
>>> python loginCreatespacePython2.py 
------------------------------------------------------------
 ARBI and the Fire Breathing... 		       X
 ARBI and the Treasure Chest... 		       X
 ARBI y el cofre del tesoro - Libro... 		   X
 ARBI y el temible dragon Drako 		       X
 ARBI e il drago sputafuoco 		           X
 ARBI eta Drako Herensugea 		               X
 ARBI et le dragon cracheur... 		           X
 ARBI and the Fire Breathing... 		       X
 ARBI and the Fire Breathing... 		       X
 ARBI Och den eldsprutande... 		           X
------------------------------------------------------------
 Unidades Vendidas: X
------------------------------------------------------------
 Dolares - 	 $X 
 Libras  - 	 £X 
 Euros   - 	 €X 
------------------------------------------------------------
TOTAL = X Euros
------------------------------------------------------------
```

NOTA1: Hay que instalar el PhantomJS para que actue en silencio

```bash
brew install phantomjs
```

NOTA2:  Createspace utiliza un login con JavaScript y no hemos podido implementar el mecanismo de login en la aplicacion de Android con JSOUP. Utilizamos Eeste script en Python para obtener los datos y para crear un web Service e implementarlo con una aplicación en **Android** ya que no hemos podido crear la conexion con JSOUP ni el WebDriver.
