import csv
from models.Car import Car

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
            carFile.write("{},{},{},{},{},{},{},{}\n".format(carType,make,licenseplate,color,passengers,transmission,rentCost,status))


    # def addCustomer(self,customer):
    #     with open('./data/customers.csv','a',) as customerFile:
    #         name = customer.getName()
    #         age = customer.getAge()
    #         ssn = customer.getSsn()
    #         customerFile.write(f'{name},{age},{ssn}\n')
       
    def getCars(self, action, typeAction):
        
        with open('./data/cars.csv', 'r') as carFile:
            csvReader = csv.DictReader(carFile)

            for line in csvReader:
                carType = line['type']
                make = line['make']
                color = line['color']
                passengers = line['passengers']
                transmission = line['transmission']
                licenseplate = line['licenseplate']
                rentcost = line['rentcost']
                status = line['status']
                

                if licenseplate not in self.__carLicenseplates:
                    self.__carLicenseplates.add(licenseplate)
                    newCar = Car(carType, make,licenseplate, color, passengers,transmission, rentcost, status)

                    if status == 'available':
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
                    if status == 'unavailable':
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
            