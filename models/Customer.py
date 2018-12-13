class Customer():
    def __init__(self,name,age,ssn, address, number):
        self.__name = name
        self.__age = age
        self.__ssn = ssn
        self.__address = address
        self.__number = number

    def __str__(self):
        s = '{:24} {:15} {:15} {:20} {:<15}'.format(self.__name,self.__age,self.__ssn, self.__address, self.__number)
        return s 
    
    def __repr__(self):
        return self.__str__()

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age
    
    def getSsn(self):
        return self.__ssn

    def getAddress(self):
        return self.__address

    def getNumber(self):
        return self.__number