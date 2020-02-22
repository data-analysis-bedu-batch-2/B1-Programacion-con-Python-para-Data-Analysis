recorridos = [
    {
        "origen" : "Roma Norte",
        "destino" : "Tabacalera",
        "distancia" : 3.5,
        "tiempo" : 15
    },
    {
        "origen" : "Reforma",
        "destino" : "Juárez",
        "distancia" : 1.2,
        "tiempo" : 15
    },
    {
        "origen" : "Alameda",
        "destino" : "Condesa",
        "distancia" : 5.4,
        "tiempo" : 15
    },
    {
        "origen" : "Roma Sur",
        "destino" : "Roma Norte",
        "distancia" : 0.8,
        "tiempo" : 4
    },
    {
        "origen" : "Buenavista",
        "destino" : "Del Valle Norte",
        "distancia" : 7.4,
        "tiempo" : 30
    }
]

tiempo_total = 0
distancia_total = 0

for recorrido in recorridos:
    tiempo_total = tiempo_total + recorrido['tiempo']
    distancia_total = distancia_total + recorrido['distancia']

line = '-'*65
print(line)
print("{:15}| {:18}| {:15}| {:10}".format('ORIGEN', 'DESTINO', 'DISTANCIA', 'TIEMPO'))
print(line)
for recorrido in recorridos:
    print("{:15}| {:18}| {:11} km | {:2} min".format(
            recorrido['origen'],
            recorrido['destino'],
            recorrido['distancia'],
            recorrido['tiempo']
        )
    )
print(line)
print("{:>51} | {} min".format('Tiempo total', tiempo_total))
print("{:>51} | {:.1f} km".format('Distancia total', distancia_total))