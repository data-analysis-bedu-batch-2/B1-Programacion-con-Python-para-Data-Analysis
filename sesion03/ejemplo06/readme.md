## Ejemplo 06

### Ambientes virtuales con pipenv

Además de crear nuestros propios paquetes y módulos podemos importar módulos desde repositorios en internet.

Sin embargo, para evitar mezclar esos paquetes en diferentes proyectos (dependencias) podemos asociar una instancia de python a cada proyecto, esto se le conoce como un *ambiente virtual* de python

La biblioteca pipenv nos ayuda a asociar de manera fácil un ambiente virtual a cada carpeta en la que estamos trabajando. 

Instalación de pipenv (Sólo se hace una vez)
```
$ pip install pipenv
```

Navegamos hasta la carpeta de nuestro proyecto y creamos el ambiente virtual
```
$ pipenv install
```

Entramos al ambiente virtual
```
$ pipenv shell
```

Podemos instalar las dependencias que queramos y éstas quedarán asociadas sólo a ese ambiente
```
$ pipenv install jupyter
```

Podemos observar que se crean los archivos Pipfile y Pipfile.lock, que nos indican las dependencias que hemos instalado en nuestro ambiente virtual.

Para salir del ambiente virtual podemos hacerlo con CTRL + D