
### Ataque Diccionario a Hash MD5 con Python  v2

Este script intenta adivinar el password de un Hash que hemos introducido en la consola utilizando un ataque de diccionario.

## Pasos antes de ejecutar el script

1. Necesitamos descargarnos el diccionario con el que vamos a probar los Hashes  (Nosotros homes bajado el rockyou.txt)
  - https://wiki.skullsecurity.org/Passwords 
2. Ejecutamos el siguiente código 
```
md5pythonHash_v2.py 	--hash [md5Hash]	 --dictionary [dictionaryPath]
```
- Donde pondremos nuestro **Hash MD5** a Crackear a continuación del comando **--hash**
- Donde pondremos nuestra ruta del diccionario que utilizaremos para crackear a continuación del comando **--dictionary**
3. Por ejemplo si queremos Crackear el Hash **e9fd4cddf2a027fabb7217f3623d531a**    (beatjudge) con el diccionario **rockyou.txt**
```
md5pythonHash_v2.py 	--hash e9fd4cddf2a027fabb7217f3623d531a	 --dictionary rockyou.txt
```
Esperar que encuentre un Match :)
