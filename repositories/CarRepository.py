import csv
from models.Car import Car

class CarRepository:
    
    def __init__(self):
        self.__cars_unavailable = []
        self.__cars_available = []

    def add_car(self, car):
       pass
       
    def get_cars(self,action):

        with open('data/cars.csv', 'r') as carFile:
            csv_reader = csv.DictReader(carFile)

            for line in csv_reader:
                type = line['type']
                make = line['make']
                color = line['color']
                passengers = line['passengers']
                transmission = line['transmission']
                licenseplate = line['licenseplate']
                rentcost = line['rentcost']
                available = line['available']

                newCar = Car(type, make,licenseplate, color, passengers,\
                transmission, rentcost, available)
                if available == 'available':
                    if licenseplate not in self.__cars_available:
                        self.__cars_available.append(newCar)                
                if available == 'unavailable':
                    if licenseplate not in self.__cars_unavailable:
                        self.__cars_unavailable.append(newCar)       
        if action == '2':
            return self.__cars_available
        if action == '3':
            return self.__cars_unavailable