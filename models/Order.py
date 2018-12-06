class Order(object):
    def __init__(self, number, customer, car, cost, extras, startDate, endDate):
        self.__number = number
        self.__customer = customer
        self.__car = car
        self.__cost = cost
        self.__extras = extras
        self.__startDate = startDate
        self.__endDate = endDate
        self.__status = status
    

    #def __str__(self):
     #   return '{:15} {:15} {:15} {:15} {:15}'.format(self.__name,self.__age,self.__ssn, self.__address, self.__number)
      
    
    #def __repr__(self):
     #   return self.__str__()


    def getNumber(self):
        return self.__number
    
    def getCustomer(self):
        return self.__customer

    def get_car(self):
        return self.__car

    def getCost(self):
        return self.__cost

    def getExtras(self):
        return self.__extras

    def getStartDate(self):
        return startDate
    
    def getEndDate(self):
        return endDate
    
    def getStatus(self):
        return self.__status

    
    