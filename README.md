# Test Properties

_Backend with Python_

### Pre-requisitos 📋

_Herramientas necesarias para levantar el proyecto._

```
Python 3.8.10
```

## Construido con 🛠️

* [Python](https://www.python.org/downloads/) - Lenguaje en el que esta escrito la prueba.
* [VS Code](https://code.visualstudio.com/) - Editor de Código.

### Instalación 🔧

_Para poder correr el script de python será necesario tener instalado Python en tu sistema._

_Es Recomendable descargar sus versiones 3.x,ejemplo:_

```
Python 3.8.10
```

_De lo contrario si usas versiones como:_

```
Python 2.x
```

_deberas modificar el codigo ya que muchas de las sentencias y sintaxis del lenguaje han sido actualizadas en sus versiones 3.x de Python_

## Como Correr el Proyecto 📌

.-Deberas primero instalar las librerias que encuentras en el requirements.txt (recomendable esto lo hagas en un entorno virtual, como por ejemplo venv).

.-Luego correr el siguiente comando:
```
uvicorn controllers.main:app --host 127.0.0.1 --port 8000 --reload
```

.-Listo ya puedes empezar hacer pruebas.

##  Respuestas en Relación a las Instrucciones de la prueba:

En base al segundo requerimiento surge lo siguiente:

+ Para poder continuar con el otro micro debemos pensar tambien en crear una tabla para relacionar las tablas como de "Me Gusta" por usuarios como las propiedas, esta incluye las respectivas ForeignKeys de la tabla de usuarios y de la tabla property.
+ En el Microservice de "Me Gusta", solo construiriamos la logica de identificar el id de la propiedad y marcar o desmarcar en su defecto el "Me Gusta" de la propiedad, para esto necesitaremos la info de la propiedad que ya nuestro primer microservice esta realizando, esta info la podemos obtener de microservice en paralelo, cosumiendo la misma api que ya creamos o, dos, utilizando gRPC, siendo gRPC la mejor opcion en cuanto a rendimiento y velocidades de respuesta.
### En relacion al punto extra:
++ Proponer una mejor extructura es viable. De mi parte adjunto tambien en el repo un archivo de extension ".drawio".

++ Yo distribuiria el schema de esta manera: Para las ciudades haria una tabla con todas las ciudades que manejemos y las referenciaria por un City_Code, Lo mismo que para el manejo de la tabla Status(ya que luego pueden darse la posibilidad de que hayan mas tipos de estados para una vivienda) ya que como esta actualente para poder hacer el curce de informacion debo hacer por string cosa que me parece una mala practica.

++ Para la propuesta de los "Me gusta" propongo una nueva tabla donde se lleve el registro las llaves foraneas de las tabla Property y User, permitiendo la data de historicos de cada usuario y ademas de llevar el resgistro de que propiedades les han dado "Me Gusta", tambien puedo contabilizar y llevar un registro de las propiedades mas atractivas para los usuarios en una muestra general.


## Autor ✒️

* **Johnny Stefan Ordoñez Mazurek** - *Backend Developer* -

---
⌨️ con ❤️ hecho en Colombia, 19 de septiembre de 2022 por [Johnny Stefan](https://github.com/johnnystefan) 😊