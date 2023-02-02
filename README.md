<h1 align="center">My-movie-app</h1>


<p>
Este proyecto se basa en aprender a realizar consultas CRUD, mediante el uso de FAStApi.
</p>

<h2 align="center">Descripción ddle proceso para consultas CRUD con FastApi</h2>

<p align="center">

<img src="https://github.com/ManeDM/Cafereflejo/blob/main/src/assets/readme_img/Service_products.png" width="600px"> 

</p>

<p>
Primero se establece una varieble que llame a lista de productos, luego para trabajar con estos se crear una variable items que recupere las caracteristicas especficas de cada producto, nombre, peso, disponibilidad etc.

Ya con esto se crean 5 funciones que interactuaran con los demas componentes del proytecto.

addToCart() sirve para agregar productos al carrito, cada vez que se agrega uno se suma a la tarjeta ya pintada en el carrito.

removeFromCart() sirve para eliminar productos del carrito, cada vez que se quita uno se elimina uno de la cantidad total de productos del carrito.

totalPrice() es una funcion que calcula el precio total con base al precio y el subtotal de cada productos cargado al carrito.

CartList() permite llamar las caracteristicas del los productos para hacer plantillas de html que reflejen una tarjeta de cada producto. 

 reduceAmount() esta funcion permite reducir los subtotales para que las otras funciones puedan hacer los calculos.
</p>

<p align="center">

<img src="https://github.com/ManeDM/Cafereflejo/blob/main/src/assets/readme_img/Service_wp.png" width="400px"> 

</p>

<p>
Se establece un variable que se iguale a la API de Whatsapp y otro varaible que se igual al codigo d eun salto de linea, luego de esto se crean dos funciones.

skipLine() se encarga de implementar la variable para el salto de linea e igualarlo a un mensaje pre fijado.

skipLine() se encarga de enviar el mensaje al Wp del vendedor con los productos que requiere el cliente.
</p>

<h2 align="center">Shared y sus componentes</h2>

<h3 align="center">Header</h3>

<p align="center">
<img src=https://github.com/ManeDM/Cafereflejo/blob/main/src/assets/readme_img/Burgue_function.png width="400px"> 
</p>

<p align="center">
Es la cabecera general de la página, trabaja con un booleano y mediante la directiva *NgIf se abre o cierra el menu.
</p>

<h3 align="center">Hero-section</h3>
<p align="center">
En este componente muestra un primer plano del producto y un frase de copy, no tiene funcionalidad.
</p>

<h3 align="center">Slider</h3>
<p align="center">
En este componente se muestra un carrusel de imagenes, no tiene funcionalidad.
</p>

<h3 align="center">Carrito
<p align="center">

<img src="https://github.com/ManeDM/Cafereflejo/blob/main/src/assets/readme_img/cart_component.png" width="400px" align="center"> 

</p>

<p align="center">
El carrito cuenta con dos funciones básicas haciendo uso de del servicio previamente mencionado.

addToCart() permite agregar productos al carrito.

filterProducts() permite filtrar productos basandose en una categoria, esta funcion pinta en pantalla solo los productos filtrados.
</p>

<h3 align="center">About-us</h3>
<p align="center">
Descripcion de las condicones de csiembra y cultivo del cafe, no tiene funcionalidad.
</p>

<h3 align="center">Footer</h3>
<p align="center">
Datos de contacto, no tiene funcionalidad.
</p>

<h3 align="center">List-cart</h3>
<p align="center">

<img src="https://github.com/ManeDM/Cafereflejo/blob/main/src/assets/readme_img/list_component.png" width="400px" align="center"> 

</p>

<p align="center">
En este componente  establecen tres funcionalidades.

deleteProduct() Permite borrar productos previamente cargados al carrito.

sendWhatsapp() toma los dos servicios creados, el de wp permite cargar informacion llamado por el primer servicio y con esta info se envia la informacion de los costes y cantidades al vendedor.

removeProduct() esta funcion permite calcular el valor de los subtotales y totales, conforme se van quitando productos.
</p>

