import csv
from models.Car import Car

class CarRepository:
    
    def __init__(self):
        self.__carsUnavailable = []
        self.__carsAvailable = []
        self.__carLicenseplates = set()

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
       
    def getCars(self,action):
        
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
                    if status == 'unavailable':
                        self.__carsUnavailable.append(newCar)       
            if action == '1':
                return self.__carsAvailable
            if action == '2':
                return self.__carsUnavailable
            