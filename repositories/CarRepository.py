import csv
from models.Car import Car

class CarRepository:
    
    def __init__(self):
        self.__cars_unavailable = []
        self.__cars_available = []

    def add_car(self, car):
       pass
       
    def get_cars(self,action):

        with open('data/cars.csv', 'r') as car_file:
            csv_reader = csv.DictReader(car_file)

            for line in csv_reader:
                type = line['type']
                make = line['make']
                color = line['color']
                passengers = line['passengers']
                transmission = line['transmission']
                licenseplate = line['licenseplate']
                rentcost = line['rentcost']
                available = line['available']

                new_car = Car(type, make,licenseplate, color, passengers,\
                transmission, rentcost, available)
                if available == 'available':
                    if licenseplate not in self.__cars_available:
                        self.__cars_available.append(new_car)                
                if available == 'unavailable':
                    if licenseplate not in self.__cars_unavailable:
                        self.__cars_unavailable.append(new_car)       
        if action == '2':
            return self.__cars_available
        if action == '3':
            return self.__cars_unavailable