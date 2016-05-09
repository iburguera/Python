### Ataque Diccionario a Hash MD5 con Python  v3

Este script intenta adivinar el password de los Hashes que tenemos almacenados en algún ficheros de texto. Para ello utiliza un ataque de diccionario.

## Pasos antes de ejecutar el script

1. Necesitamos descargarnos el diccionario con el que vamos a probar los Hashes  (Nosotros hemos bajado el rockyou.txt)
  - https://wiki.skullsecurity.org/Passwords 
2. Ejecutamos el siguiente código 
```
md5pythonHash_v3.py 	--hashFile [md5HashFilePath]	 --dictionary [dictionaryPath]
```
- Donde pondremos la ruta a nuestro fichero con el contenido de Hashes a Decrypt a continuación del comando **--hashFile**
- Donde pondremos nuestra ruta del diccionario que utilizaremos para crackear a continuación del comando **--dictionary**
3. Por ejemplo si queremos Decrypt el fichero con los Hashes MD5 **MD5HashFile.txt** con el diccionario **rockyou.txt**
```
md5pythonHash_v2.py 	--hashFile MD5HashFile.txt	 --dictionary rockyou.txt
```
Al finalizar nos mostrará el resultado de los Hashes Decryptados y tambien una lista de los Hashes que no  ha podido sacar de la lista de passwords (Podrías utilizar una lista que contengo mas contraseñas)

Esperar que encuentre un Match :)
