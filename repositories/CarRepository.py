import csv
from models.Car import Car

class CarRepository:
    
    def __init__(self):
        self.__carsUnavailable = []
        self.__carsAvailable = []
        self.__entries = set()

    def addCar(self, car):
       pass
       
    def getCars(self,action):
        
        with open('./data/cars.csv', 'r') as carFile:
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
                

                if licenseplate not in self.__entries:
                    self.__entries.add(licenseplate)
                    newCar = Car(type, make,licenseplate, color, passengers,transmission, rentcost, status)

                    if status == 'available':
                        self.__carsAvailable.append(newCar)                
                    if status == 'unavailable':
                        self.__carsUnavailable.append(newCar)       
            if action == '1':
                return self.__carsAvailable
            if action == '2':
                return self.__carsUnavailable