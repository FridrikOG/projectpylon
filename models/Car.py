class Car:

    def __init__(self,type, make,licenseplate, color, passengers, \
    transmission, rentcost, available):
        self.__type = type
        self.__make = make
        self.__licenseplate = licenseplate
        self.__color = color
        self.__passengers = passengers
        self.__transmission = transmission
        self.__rentcost = rentcost
        self.__available = available


    def __str__(self):
        return "{:15} {:15} {:15} {:15} {:15} {:15} {:6} ISK ".format(self.__type, \
        self.__make,self.__licenseplate,self.__color ,self.__passengers,self.__transmission,\
        self.__rentcost)
    
    def __repr__(self):
        return self.__str__()

    def get_type(self):
        return self.__type
    
    def get_make(self):
        return self.__make
    
    def get_color(self):
        return self.__color
    
    def get_licenseplate(self):
        return self.__licenseplate

    def get_passengers(self):
        return self.__passengers

    def get_transmission(self):
        return self.__transmission
    
    def get_rentcost(self):
        return self.__rentcost

    def get_available(self):
        return self.__available


