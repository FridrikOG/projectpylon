from repositories.CarRepository import CarRepository

class CarService:
    def __init__(self):
        self.__carRepo = CarRepository()


    def getCars(self, action):
        return self.__carRepo.getCars(action)