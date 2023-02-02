<h1 align="center">My-movie-app</h1>

<p align="center">

<img src="https://github.com/ManeDM/my_movie_app/blob/main/assets/crud.jpeg" width="400px"> 

</p>


<p align="center">
Este proyecto se basa en aprender a realizar consultas CRUD, mediante el uso de FAStApi.
</p>

<h2 align="center">Descripción del proceso para consultas CRUD con FastApi</h2>


<p >
El manejo de base de datos mediante el uso de FastApi nos permite manipular informacion de tablas mediante el uso de logica de progrmacion orientada a objetos, en esta caso haciendo uso de python, para esto hace manejo de la siguiente estructura Models - Schemas - Services - Routes
</p>

<h2 align="center">Models</h2>

<p align="center">

<img src="https://github.com/ManeDM/my_movie_app/blob/main/assets/model.png" width="400px"> 

</p>

<p>
primero se importar desde SQlalchemy, los tipos de datos que llevara el modelo y la creacion de la columna.

Luego se importa la base de datos, para proseguir con la creacion de la tabla, una vez creada, la tabla contendra variables nombradas con base al contenido de la informacion que contendra esta, cada varaible sera igual a una columna y a su vez cada columna soportara un tipo de dato especifico.
</p>

<h2 align="center">Schemas</h2>

<p align="center">

<img src="https://github.com/ManeDM/my_movie_app/blob/main/assets/schema.png" width="400px"> 

</p>

<p>
Los esquemas sirven para definir las caracteristicas especificas de cada campo en nuestra tabla mediante la creacion de varaibles que hagan referencia a los datos previamente creados en los modelos, se definen caracteristicas espcificas con las cuales estos deben contar, como por ejemplo un minimo y un maximo de caracteres, en el caso de que estuvieramos esperando un dato tipo String.
</p>

<h2 align="center">Service</h3>

<p align="center">

<img src="https://github.com/ManeDM/my_movie_app/blob/main/assets/service.png" width="400px"> 

</p>

<p>
Los servicios son lo que nos permite utilizar la logica de programacion orientada a objetos, ya que es aqui donde podremos crear funciones especficas para captar y manipular la informacion de nuestras bases de datos, en este caso usando python.

Una función siempre se contiene a si misma como parametro y agregado a esta los demas parametros con los que la funcion va a trabajar, luego dentro de la funcion se crea una variable que sea igual al Modelo de la tabla con la que estamos trabajando, dicha variable contiene los datos especificos que se prentenden captar y/o manipular.
</p>

<h2 align="center">Routes</h3>

<p align="center">

<img src="https://github.com/ManeDM/my_movie_app/blob/main/assets/routes.png" width="400px"> 

</p>

<p>
Ahora con  modelos, esquemas y servicios contruidos podemos atribuirles una ruta, la cual ejecutara una accion especifica aqui ya podemos hacer consultas CRUD, mediante los metodos get, post,put, delete.

con el decorador @ se invoca una ruta previamente creada en el archivo main.py mediante el API Router, luego se ejecuta el tipo de consulta que vamos a realizar (Get, post, put, delete), seguido a esto se establece una ruta para que el servidor tenga donde cargar la informacion consultada y un tag para poder ejecutar la consulta en el servidor.

luego se crea un funcion que contenga como parametro el dato con el cual se espera trabajar.

A continuacion se debe abrir una sesion que nos permita trabajar con la base de datos.

Ahora mediante la creacion de una varaible, normalmente llamada result, se llama el servicio previamente creado, el parametro de esta varaible debe ser la base de datos, seguido a esto se llama el servicio especifico que ejecutara la logica de llamada de datos, este servicio tendra como parametro el tipo de dato con el que trabajara.

Despues de esto la funcion nos puede retonar uno o mas respuestas dependiendo de las condiciones establecidas.
</p>


