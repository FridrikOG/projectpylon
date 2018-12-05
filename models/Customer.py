class Customer():
    def __init__(self,name,age,ssn):
        self.__name = name
        self.__age = age
        self.__ssn = ssn

    def __str__(self):
        return '{:15} {:15} {:15}'.format(self.__name,self.__age,self.__ssn)
    
    def __repr__(self):
        return self.__str__()

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age
    
    def getSsn(self):
        return self.__ssn