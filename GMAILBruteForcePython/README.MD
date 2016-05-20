### Ataque Diccionario a Correo GMAIL con Python  

**[!]** No me hago responsable del mal uso de esta herramienta. Utilizala con cuentas de GMAIL que administres tu y con fines didacticos.

Este script intenta realizar una conexión al servidor SMTP de GMAIL utilizando una dirección de correo electronico y multiple contraseñas que se listan en una hoja.
Basicamente es un ataque de diccionario a GMAIL.

## Pasos antes de ejecutar el script

1. Necesitamos descargarnos el diccionario con el que vamos a probar los Password  (Nosotros hemos bajado el rockyou.txt)
  - https://wiki.skullsecurity.org/Passwords 
  - **[!]** Este diccionario tiene cerca de 14 millones de contraseñas y probablemente GMAIL cerraría la conexión, baneando la IP. Mi recomendación es acortar la lista de posibles contraseñas y realizar el ataque con un listado mas pequeño.
2. Ejecutamos el siguiente código 
```
gmailBruteForcePython.py 	--email [correo gmail ]	 --pwdlist [diccionario con passwords]
```
- Donde pondremos el correo a **atacar** a continuación del comando **--email**
- Donde pondremos nuestra ruta del diccionario que utilizaremos para crackear a continuación del comando **--pwdlist**
3. Por ejemplo si queremos atacar el correo **madafaka@gmail.com**  con el diccionario **rockyou.txt**
```
gmailBruteForcePython.py  	--email madafaka@gmail.com	 --pwdlist rockyou.txt
```
Esperar que encuentre un Match :)


