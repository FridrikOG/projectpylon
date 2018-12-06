from repositories.CarRepository import CarRepository

class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()


    def getCars(self, action, typeAction):
        return self.__carRepo.getCars(action, typeAction)

    def addCar(self, newCar):
        self.__carRepo.addCar(newCar)