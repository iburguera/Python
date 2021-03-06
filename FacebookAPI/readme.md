## DESCARGAR IMAGENES DE FACEBOOK CON PYTHON

El siguiente script está programado para descargarse todas las fotos de tu usuario en Facebook a un directorio local.
Hay algunos bugs y mejoras que se le pueden hacer al programa (ver sección BUGS & MEJORAS) pero funciona bien.

IMPORTANTE: El Script no funciona si no tienes el TOKEN o se ha caducado. El TOKEN que obtenemos es de corta duración por lo que normalmente durará una hora más o menos (https://developers.facebook.com/docs/facebook-login/access-tokens)



### Antes de ejecutar el script

  1. Obtener el **ACCESS TOKEN** de la siguiente direccion : 
    1. https://developers.facebook.com/tools/explorer
      1. Pulsar el boton **Get Token** -> **Get User Access Token** 
      2. Habilitar los permisos **user_photos** 
      
### Logica del Script
  1. Obtener los **ALBUMES** de tu perfil de Facebook
    1. Ejemplo: https://graph.facebook.com/me/albums?access_token=**TU_TOKEN**
    2. Nos devuelve un texto en formato **JSON** 
      1. ```json {"data": [{"id": "numero_album_ID","can_upload": false,"count": 8,"cover_photo": "numeros","created_time": "2011-01-12T14:30:25+0000","from": {"name": "Iker Burguera","id": "fdsafsdfds"},"link": "https://www.facebook.com/album.php?fbid=asdfasdf","name": "Timeline Photos","privacy": "everyone","type": "wall","updated_time": "2016-04-11T12:08:02+0000"}],"paging": {"cursors": {"before": "asdfasdfdsf","after": "asdfasdfasdf"}}```
  2. Obtener los **ID** de todos los ALBUMES de fotos que tenemos en Facebook para que luego podamos iterar sobre ellos en la siguiente direccion
    1. Ejemplo: https://graph.facebook.com/**ALBUM_ID**/photos?access_token=**TU_TOKEN**
    2. Nos devuelve un string en formato **JSON** y podemos obtener la **URL** de las fotos de cada ALBUM 
  3. Extraemos las **URL** y nos descargamos las fotos utilizando la libreria **URLLIB** 

### BUGS 
 - [x] Por defecto Facebook solo nos muestra 25 objetos de JSON (limit=25). Se arregla poniendo **limit=1000** o un numero mas grande en la URL a la hora de hacer la peticion
 - [ ] No deja obtener más de 100 objetos 

### MEJORAS
 - [ ] Crear carpetas y meter las fotos dentro (Ahora las almacena en una misma ubicación). El nombre de las fotos contiene el Album al que pertenece
 - [ ] Utilizar la opcion PAGING NEXT de la respuesta **JSON** para saber la siguiente URL y obtener los datos de forma iterativa hasta que no haya una siguiente página. Por cada pagina obtendríamos 25 valores


