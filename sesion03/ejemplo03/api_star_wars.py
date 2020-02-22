import requests

people = []
page = 1
_next = 1
while _next != None:
    response = requests.get(
        'https://swapi.co/api/people/?page={}'.format(page)
    )
    data = response.json()
    _next = data['next'] 
    people = people + data['results']
    page = page + 1

people_height = []
for person in people:
    height_str = person['height']
    if not height_str.isdigit():
        height = 0
    else:
        height = int(height_str)
    people_height.append({
        'name': person['name'],
        'height': height
    })

people_height.sort(key=lambda p: p['height'])

print('Personaje más alto: {} con  {} cm'.format(
    people_height[-1]['name'],
    people_height[-1]['height'],
))
