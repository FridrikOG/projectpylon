import csv
from models.Car import Car
from datetime import datetime, timedelta
import operator


class CarRepository:
    
    def __init__(self):
        self.__carsUnavailable = []
        self.__carsAvailable = []
        self.__carLicenseplates = set()
        self.__carsCUVAvailable= []
        self.__carsLuxuryAvailable = []
        self.__carsHighlandAvailable = []
        self.__carsCompactAvailable = []
        self.__carsComfortAvailable = []
        self.__carsCUVUnavailable= []
        self.__carsLuxuryUnavailable = []
        self.__carsHighlandUnavailable = []
        self.__carsCompactUnavailable = []
        self.__carsComfortUnavailable = []

    def addCar(self, newCar):
        with open('./data/cars.csv', 'a') as carFile:
            carType = newCar.getType()
            make = newCar.getMake()
            color = newCar.getColor()
            passengers = newCar.getPassengers()
            transmission = newCar.getTransmission()
            licenseplate = newCar.getLicenseplate()
            rentCost = newCar.getRentcost()
            status = newCar.getStatus()
            rentOutCar = newCar.getRentOutCar()
            returnCar = newCar.getReturnCar()
            
            carFile.write("{},{},{},{},{},{},{},{},{},{}\n".format(carType,make,licenseplate,color,passengers,transmission,\
            rentCost,status,rentOutCar,returnCar))

    def createDate(self, rentDate):
        day, month, year, hour, minutes = map(int, rentDate.split('-'))
        return datetime(year, month, day, hour, minutes)
       
    def getCars(self, action, typeAction, dateAvailable):
        
        with open('./data/cars.csv', 'r') as carFile:
            csvReader = csv.DictReader(carFile, delimiter=',')

            for line in csvReader:
                carType = line['type']
                make = line['make']
                color = line['color']
                passengers = line['passengers']
                transmission = line['transmission']
                licenseplate = line['licenseplate']
                rentcost = line['rentcost']
                status = line['status']
                rentOutCar = self.createDate(line['rentout'])
                returnCar = self.createDate(line['return'])
                   

                if licenseplate not in self.__carLicenseplates:
                    self.__carLicenseplates.add(licenseplate)
                    newCar = Car(carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar)

                    if rentOutCar < dateAvailable < returnCar:
                        self.__carsUnavailable.append(newCar)  
                        if carType == 'Compact':
                            self.__carsCompactUnavailable.append(newCar)
                        if carType == 'Comfort':
                            self.__carsComfortUnavailable.append(newCar)  
                        if carType == 'Luxury':
                            self.__carsLuxuryUnavailable.append(newCar)
                        if carType == 'CUV':
                            self.__carsCUVUnavailable.append(newCar)  
                        if carType == 'Highland':
                            self.__carsHighlandUnavailable.append(newCar) 
                    else:
                        self.__carsAvailable.append(newCar)  
                        if carType == 'Compact':
                            self.__carsCompactAvailable.append(newCar)
                        if carType == 'Comfort':
                            self.__carsComfortAvailable.append(newCar)  
                        if carType == 'Luxury':
                            self.__carsLuxuryAvailable.append(newCar)
                        if carType == 'CUV':
                            self.__carsCUVAvailable.append(newCar)  
                        if carType == 'Highland':
                            self.__carsHighlandAvailable.append(newCar)               
                       
            if action == '1' and typeAction == '':
                return self.__carsAvailable
            if action == '1' and typeAction == 'compact':
                return self.__carsCompactAvailable
            if action == '1' and typeAction == 'comfort':
                return self.__carsComfortAvailable
            if action == '1' and typeAction == 'luxury':
                return self.__carsLuxuryAvailable
            if action == '1' and typeAction == 'highland':
                return self.__carsHighlandAvailable
            if action == '1' and typeAction == 'CUV':
                return self.__carsCUVAvailable
            if action == '2' and typeAction == '':
                return self.__carsUnavailable
            if action == '2' and typeAction == 'compact':
                return self.__carsCompactUnavailable
            if action == '2' and typeAction == 'comfort':
                return self.__carsComfortUnavailable
            if action == '2' and typeAction == 'luxury':
                return self.__carsLuxuryUnavailable
            if action == '2' and typeAction == 'highland':
                return self.__carsHighlandUnavailable
            if action == '2' and typeAction == 'CUV':
                return self.__carsCUVUnavailable

    def duplicateLicensePlateCheck(self, newLicensePlate):
        with open('./data/cars.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    licensePlate = line['licenseplate']
                    if newLicensePlate == licensePlate:
                        print("License plate already registered!")
                        return False
            return True
            