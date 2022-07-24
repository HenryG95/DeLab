-Lo primero que hacemos es crear una funcion que retorne una lista con todas las organizaciones a las que se tiene acceso con el API Key
-Luego se implementa una validacion de estado para verificar si la pagina esta funcionando
-se añade una carpeta .gitignore para ignorar el __pycache__ cuando se haga push hacia github

-luego de ver la lista vemos que el numero de id de DeLab es "681155", con esto podemos crear un nuevo url que nos mostrara una lista de todos los dispositivos asociados con esta compañia
-el codigo get se utiliza de igual forma para buscar organizaciones y dispositivos entonces se renombra el archivo getOrganizations a get
-se crea un nuevo archivo listMaker.py que recibe una lista y una palabra clave. En este caso queremos buscar equipos de tipo "wireless" y "appliance". la funcion este archivo procedera a crear una lueva lista donde inserte todos los dispositivos que se quieren.
-primero se importa en listMaker.py la libreria re la cual se utilizara para ver el firmware de cada dispositivo para ver si es tipo "wireless" o "appliance". los parametros de esta funcion seran la lista que contiene los diccionarios para cada dispositivo y el segundo parametro sera el nombre del firmware que se quiere buscar. si se quiere buscar mas de uno se utiliza un "|" entre las palabras, por ejemplo "wireless|appliance"

-para la parte final, se crea un archivo csvMaker.py que tome la lista que se requiere y de esa informacion se hace un archivo .csv

-cabe destacar que este programa funciona para cualquier tipo de firmware que se desee ya que con solo poner la palabra que se quiera, el codigo filtrara la lista hasta seleccionar los dispositivos deseados

