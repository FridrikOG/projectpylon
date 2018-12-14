class Order(object):
    def __init__(self, orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, Ssn):
        self.__orderNumber = orderNumber
        self.__customer = customer
        self.__carType = carType
        self.__timeOfOrder = timeOfOrder
        self.__startDate = startDate
        self.__endDate = endDate
        self.__rentCost = rentCost
        self.__Ssn = Ssn

    def __str__(self):
        return '{:13} {:20} {:12} {:10} {:18} {:18} {:18} {} ISK'.format(self.__orderNumber,self.__customer,self.__Ssn, self.__carType,\
        self.__timeOfOrder, self.__startDate, self.__endDate, self.__rentCost)
      
    
    def __repr__(self):
        return self.__str__()


    def getOrderNumber(self):
        return self.__orderNumber
    
    def getCustomer(self):
        return self.__customer

    def getCarType(self):
        return self.__carType

    def getTimeOfOrder(self):
        return self.__timeOfOrder

    def getStartDate(self):
        return self.__startDate
    
    def getEndDate(self):
        return self.__endDate
    
    def getRentCost(self):
        return self.__rentCost

    def getSsn(self):
        return self.__Ssn
    
 