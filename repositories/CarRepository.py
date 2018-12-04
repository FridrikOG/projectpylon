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
                status = line['status']

<<<<<<< HEAD
                newCar = Car(type, make,licenseplate, color, passengers,\
                transmission, rentcost, available)
                if available == 'available':
                    if licenseplate not in self.__cars_available:
                        self.__cars_available.append(newCar)                
                if available == 'unavailable':
                    if licenseplate not in self.__cars_unavailable:
                        self.__cars_unavailable.append(newCar)       
        if action == '2':
=======
                new_car = Car(type, make,licenseplate, color, passengers,\
                transmission, rentcost, status)
                if status == 'available':
                    if licenseplate not in self.__cars_available:
                        self.__cars_available.append(new_car)                
                if status == 'unavailable':
                    if licenseplate not in self.__cars_unavailable:
                        self.__cars_unavailable.append(new_car)       
        if action == '1':
>>>>>>> 76a40aa9da3098c6b40351afc35eeb0f5b62b6e9
            return self.__cars_available
        if action == '2':
            return self.__cars_unavailable