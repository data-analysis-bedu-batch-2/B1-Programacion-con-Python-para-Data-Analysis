## Ejemplo 01
## Consumiendo información

Un API es una manera de interactuar con el servicio de un tercero, del cual normalmente se puede obtener, editar o agregar información. Las APIs pueden extender la funcionalidad de un programa. El término se asocia con APIs web, pero también existen para librerías o hardware.

Para familiarizarnos y explorar un API siempre se recomienda hacerlo primero desde un REST Client, uno de los más modernos es Insomnia.

Se puede instalar desde:

(https://insomnia.rest/)

## Uso de Insomnia

Explorar la API PokeAPI (http://pokeapi.co) con Insomnia, para obtener información acerca de algún Pokemon.

## Códigos de estado

Una Web API entrega códigos de estado para indicar el resultado de la operación realizada. Los tipos mas importantes son:

* 2xx: La petición fue relizada exitosamente
* 3xx: El recurso se ha movido
* 4xx: Error por parte del cliente
* 5xx: Error por parte del servidor

![Status codes](./status_codes.png)

## Métodos HTTP y su manejo con requests

En una Web API, se utilizan los métodos o verbos HTTP para indicar el tipo de operación que se desa realizar.

Los más utilizados son:

* GET: Obtiene el recurso
* POST: Agrega un nuevo recurso
* PUT: Edita un recurso existente
* DELETE: Borra un recurso

`http_metodos.py`

```python
In [1]: import requests

In [2]: requests.get("https://jsonplaceholder.typicode.com/posts") # Obtener múltiples elementos
Out[2]: <Response [200]>

In [3]: requests.get("https://jsonplaceholder.typicode.com/posts/1") # Obtener un elemento
Out[3]: <Response [200]>

In [4]: requests.post("https://jsonplaceholder.typicode.com/posts", json={"post": "Nuevo post de ejemplo"}) # Nuevo elemento
Out[4]: <Response [201]>

In [5]: requests.put("https://jsonplaceholder.typicode.com/posts/1", json={"post": "Editado"}) # Editar elemento
Out[5]: <Response [404]>

In [12]: requests.delete("https://jsonplaceholder.typicode.com/posts/1")  # Borrar elemento
Out[12]: <Response [200]>

In [13]: requests.delete("https://jsonplaceholder.typicode.com/noexiste")  # Elemento no existente
Out[13]: <Response [404]>
````

