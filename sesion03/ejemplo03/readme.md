## Ejemplo 03

### Requests

Requests es una librería de Python que nos permite hace peticiones HTTP desde Python. Es especialmente útil para consumir REST APIS.
Para instalarlo basta con correr `pip3 install requests`.

`consumo_apis.py`

```python
In  [1]: import requests

In  [2]: r = requests.get('https://swapi.co/api/people/1')

In  [3]: print(r)
Out [3]: print(r)

{
	"name": "Luke Skywalker",
	"height": "172",
	"mass": "77",
	"hair_color": "blond",
	"skin_color": "fair",
	"eye_color": "blue",
	"birth_year": "19BBY",
	"gender": "male",
	"homeworld": "https://swapi.co/api/planets/1/",
       ...
}
```

`personajes_star_wars.py`

Consume el API de Star Wars y detecta cuál es el personaje más viejo 

