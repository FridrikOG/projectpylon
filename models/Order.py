class Order(object):
    def __init__(self, orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, SSN):
        self.__orderNumber = orderNumber
        self.__customer = customer
        self.__carType = carType
        self.__timeOfOrder = timeOfOrder
        #self.__extras = extras
        self.__startDate = startDate
        self.__endDate = endDate
        self.__rentCost = rentCost
        self.__SSN = SSN
        #self.__status = status

    def __str__(self):
        return '{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:6} ISK'.format(self.__orderNumber,self.__customer,self.__SSN, self.__carType,\
        self.__timeOfOrder, self.__startDate, self.__endDate, self.__rentCost)
      
    
    def __repr__(self):
        return self.__str__()


    def getOrderNumber(self):
        return self.__orderNumber
    
    def getCustomer(self):
        return self.__customer

    def getCarType(self):
        return self.__carType

    #def getExtras(self):
     #   return self.__extras
    def getTimeOfOrder(self):
        return self.__timeOfOrder

    def getStartDate(self):
        return self.__startDate
    
    def getEndDate(self):
        return self.__endDate
    
    def getRentCost(self):
        return self.__rentCost

    def getSSN(self):
        return self.__SSN
    
    #def getStatus(self):
     #   return self.__status