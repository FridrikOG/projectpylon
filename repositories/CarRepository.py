import csv
from models.Car import Car
from datetime import datetime, timedelta
import operator


class CarRepository:
    
    def __init__(self):
        self.__carsUnavailable = []
        self.__carsAvailable = []

    def createDate(self, rentDate):
        # takes date string and changes it to datetime format
        day, month, year, hour, minutes = map(int, rentDate.split('-'))
        return datetime(year, month, day, hour, minutes)

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
       
    def getCars(self, action, typeAction, dateAvailable):
        
        with open('./data/cars.csv', 'r') as carFile:
            csvReader = csv.DictReader(carFile, delimiter=',')
            self.__carsAvailable.clear()
            self.__carsUnavailable.clear()

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
                newCar = Car(carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar)

                if rentOutCar < dateAvailable < returnCar or status == 'unavailable':
                    if typeAction.upper() == '':
                        self.__carsUnavailable.append(newCar)
                    elif carType.upper() == typeAction.upper():
                        self.__carsUnavailable.append(newCar)
                else:
                    if typeAction.upper() == '':
                        self.__carsAvailable.append(newCar)
                    elif carType.upper() == typeAction.upper():
                        self.__carsAvailable.append(newCar)     

            if action == '1':
                return self.__carsAvailable
            elif action == '2':
                return self.__carsUnavailable   

    def duplicateLicensePlateCheck(self, newLicensePlate):
        # Check if car is already in the system
        with open('./data/cars.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    licensePlate = line['licenseplate']
                    if newLicensePlate == licensePlate:
                        return False
            return True

    def returnCar(self, licenseplate, timeOfReturn):
        with open ('./data/cars.csv') as carFile:
            header = ('type','make','licenseplate','color','passengers','transmission','rentcost','status','rentout','return')
            csvReader = csv.DictReader(carFile, header)
            next(carFile, None)
            lines = []
            for line in csvReader:
                if line['licenseplate'] == licenseplate:
                    # Return car befor changes
                    carType = line['type']
                    make = line['make']
                    color = line['color']
                    passengers = line['passengers']
                    transmission = line['transmission']
                    rentcost = line['rentcost']
                    status = line['status']
                    rentOutCar = self.createDate(line['rentout'])
                    returnCar = self.createDate(line['return'])
                    returnCarInfo = Car(carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar)
                    # Change car status
                    line['status'] = 'available'
                    line['return'] = timeOfReturn #strengur
                    lines.append(line)
                else:
                    lines.append(line)
        with open('./data/cars.csv', 'w') as carFile:
            writer = csv.DictWriter(carFile, fieldnames=header)
            writer.writeheader()
            writer.writerows(lines)
            
        return returnCarInfo

    def LicensePlateCheck(self, newLicensePlate):
        with open('./data/cars.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    licensePlate = line['licenseplate']
                    if newLicensePlate == licensePlate:
                        carType = line['type']
                        make = line['make']
                        color = line['color']
                        passengers = line['passengers']
                        transmission = line['transmission']
                        rentcost = line['rentcost']
                        status = line['status']
                        rentOutCar = self.createDate(line['rentout'])
                        returnCar = self.createDate(line['return'])
                        returnCarInfo = Car(carType, make,licensePlate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar)
                        return returnCarInfo
            return None

    def editCar(self, carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar):
        with open ('./data/cars.csv') as carFile:
            header = ('type','make','licenseplate','color','passengers','transmission','rentcost','status','rentout','return')
            csvReader = csv.DictReader(carFile, header)
            next(carFile, None)
            lines = []
            for line in csvReader:
                if line['licenseplate'] == licenseplate:
                    # Edit car info.
                    line['status'] = status
                    line['type'] = carType
                    line['make'] = make
                    line['color'] = color
                    line['passengers'] = passengers
                    line['transmission'] = transmission 
                    line['rentcost'] = rentcost
                    line['rentout'] = rentOutCar
                    line['return'] = returnCar
                    lines.append(line)
                    returnCarInfo = Car(carType, make,licenseplate, color, passengers,transmission, rentcost, status,rentOutCar,returnCar)

                else:
                    lines.append(line)
        with open('./data/cars.csv', 'w') as carFile:
            writer = csv.DictWriter(carFile, fieldnames=header)
            writer.writeheader()
            writer.writerows(lines)

        return returnCarInfo