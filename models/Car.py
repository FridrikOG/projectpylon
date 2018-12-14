class Car:

    def __init__(self,type, make,licenseplate, color, passengers, \
    transmission, rentcost, status, rentOutCar,returnCar):
        self.__type = type
        self.__make = make
        self.__licenseplate = licenseplate
        self.__color = color
        self.__passengers = passengers
        self.__transmission = transmission
        self.__rentcost = rentcost
        self.__status = status
        self.__rentOutCar = rentOutCar
        self.__returnCar = returnCar

    def __str__(self):
        return "{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<6} ISK ".format(self.__type, \
        self.__make,self.__licenseplate,self.__color ,self.__passengers,self.__transmission,\
        self.__rentcost)
    
    def __repr__(self):
        return self.__str__()

    def getType(self):
        return self.__type
    
    def getMake(self):
        return self.__make
    
    def getColor(self):
        return self.__color
    
    def getLicenseplate(self):
        return self.__licenseplate

    def getPassengers(self):
        return self.__passengers

    def getTransmission(self):
        return self.__transmission
    
    def getRentcost(self):
        return self.__rentcost

    def getStatus(self):
        return self.__status

    def getRentOutCar(self):
        return self.__rentOutCar

    def getReturnCar(self):
        return self.__returnCar