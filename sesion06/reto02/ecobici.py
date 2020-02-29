""" Modulo para leer información del csv de Ecobici """
import csv

def get_data():
    """ Reads csv data as dict """
    data = []
    with open('ecobici.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

if __name__ == "__main__":
    data = get_data()
    print(data[0])
