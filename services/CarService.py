from repositories.CarRepository import CarRepository

class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()


    def getCars(self, action, typeAction):
        return self.__carRepo.getCars(action, typeAction)

    def addCar(self, newCar):
        self.__carRepo.addCar(newCar)

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
                if 1 < passengers < 13:
                    break
                else:
                    print("Please only insert passenger size from 2-12")
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