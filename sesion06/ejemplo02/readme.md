## Ejemplo 02
## Flask

Flask es un micro framework para crear un servidor web con Python. Fue creado para ser lo más sencillo posible pero con la posibilidad de hacerlo escalable.

Podemos instalar Flask de manera muy sencilla con pip.

```
$ pip install flask
```

`flask-hello-world.py`

Para iniciar el servidor lo podemos hacer desde la línea de comandos.

```
$ python flask-hello-world.py
 * Serving Flask app "flask-hello-world" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Si queremos que el servidor detecte nuestros cambios, entonces debemos de pasar la variable de ambiente FLASK_DEBUG como True en la línea de comandos:

```
$ FLASK_ENV=development python flask-hello-world.py
```

Flask además nos permite regresar diccionarios en forma de json con su función jsonify Flask podemos crear una REST API de manera muy sencilla.

`flask-rest-api.py`

```
$ curl --request GET --url http://localhost:5000/users/1
{"firstname":"Jhon","gender":"M","lastname":"Doe"}

```


