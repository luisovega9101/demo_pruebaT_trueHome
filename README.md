# demo_pruebaT_trueHome
## Prueba técnica - Desarrollador Backend

### Instalar las tecnologías:
* Django Web Framework
* Django API Rest Framework

### Modo de ejecución
La aplicación web como el API deben ser dos proyectos independientes montados en un ambiente de pruebas a elegir.

1. Item 1 La aplicación **"demo_api"** es la API Rest que maneja los eventos básicos para registrar, actualizar y eliminar propiedades de una base de datos básica; valida desde los métodos del API los datos indicando los formatos que cumplen, regresando los correspondientes mensajes de acuerdo a las validaciones realizadas en cada uno de los campos. También, mantiene un nivel de log de todas las acciones a nivel informativo y capturando las excepciones principales en ejecución. Además de generar un esquema de autorización por medio de tokens con una vigencia de 15 días.
En el ambiente de pipenv, se ejecuta con número de puerto:9000, de la siguiente manera: **manager.py runserver 0.0.0.0:9000**

2. Item 2 La aplicación **"demo_app"** es la APP donde de forma gráfica se muestre el listado de propiedades consumido de la API anterior.
En el ambiente de pipenv, se ejecuta con número de puerto:8000, de la siguiente manera: **manager.py runserver 0.0.0.0:8000**
