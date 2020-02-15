origen1 = "Roma Norte"
destino1 = "Tabacalera"
distancia1 = 3.5
tiempo1 = 15

origen2 = "Reforma"
destino2 = "Juárez"
distancia2 = 1.2
tiempo2 = 8

origen3 = "Alameda"
destino3 = "Condesa"
distancia3 = 5.4
tiempo3 = 20

origen4 = "Roma Sur"
destino4 = "Roma Norte"
distancia4 = 0.8
tiempo4 = 4

origen5 = "Buenavista"
destino5 = "Del Valle Norte"
distancia5 = 7.4
tiempo5 = 30

line = '-'*65
tiempo_total = tiempo1 + tiempo2 + tiempo3 + tiempo4 + tiempo5 
distancia_total = distancia1 + distancia2 + distancia3 + distancia4 + distancia5 

print(line)
print("{:15}| {:18}| {:15}| {:10}".format('ORIGEN', 'DESTINO', 'DISTANCIA', 'TIEMPO'))
print(line)
print("{:15}| {:18}| {:11} km | {:2} min".format(origen1, destino1, distancia1, tiempo1))
print("{:15}| {:18}| {:11} km | {:2} min".format(origen2, destino2, distancia2, tiempo2))
print("{:15}| {:18}| {:11} km | {:2} min".format(origen3, destino3, distancia3, tiempo3))
print("{:15}| {:18}| {:11} km | {:2} min".format(origen4, destino4, distancia4, tiempo4))
print("{:15}| {:18}| {:11} km | {:2} min".format(origen5, destino5, distancia5, tiempo5))
print(line)
print("{:>51} | {} min".format('Tiempo total', tiempo_total))
print("{:>51} | {:.1f} km".format('Distancia total', distancia_total))
