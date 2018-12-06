from repositories.CarRepository import CarRepository
from datetime import datetime, timedelta

class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()


    def getCars(self, action, typeAction,dateAvailable):
        return self.__carRepo.getCars(action, typeAction,dateAvailable)

    def addCar(self, newCar):
        self.__carRepo.addCar(newCar)

    def checkValidDate(self):
        while True:
            try:
                rentOutCar = input('Date created in this format DD-MM-YYYY: ') + '-12-00'
                day, month, year, hour, minutes = map(int, rentOutCar.split('-'))
                break
            except:
                print("\nplease input valid date\n")
        return rentOutCar

    def checkCarType(self):
        while True:
            try:
                carTypeInput = int(input('Choose car type number:  '))
                if 0 < carTypeInput < 6:
                    break
                else:
                    print('Please choose from available types\n')
            except:
                print("Please only insert integer values\n")
        return carTypeInput


    def checkPassengers(self):
        while True:
            try:
                passengers = int(input('Passengers: '))
                break
            except:
                print("\nPlease only insert integer values\n")
        return passengers
        


    def checkTransmission(self):
        print("Transmission:\n1. Auto\n2. Manual\n")

        while True:
            try:
                transmissionInput = int(input('Choose: '))
                if 0 < transmissionInput < 3:
                    break
                else:
                    print('Please choose from available transmissions\n')
            except:
                print("Please only insert integer values\n")
        return transmissionInput


    def checkLicenseplate(self):
        while True:
            licenseplate = input('License plate (F.x. LL-L00): ').upper()
            if len(list(licenseplate)) == 6:
                break
            else:
                print("Not a valid license plate")
        return licenseplate