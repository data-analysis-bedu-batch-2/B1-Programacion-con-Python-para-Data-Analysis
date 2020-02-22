import requests

contrataciones = []

for page in range(10):
    response = requests.get(
        'https://api.datos.gob.mx/v2/contratacionesabiertas?page={}'.format(page)
    )
    data = response.json()
    contrataciones = contrataciones + data['results']

dependencias = []
for contratacion in contrataciones:
    dependencias.append(contratacion['publisher']['name'])

set_dependencias = set(dependencias)

print(set_dependencias)