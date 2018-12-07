class Order(object):
    def __init__(self, orderNumber, customer, carNumber, timeOfOrder, startDate, endDate, rentCost):
        self.__orderNumber = orderNumber
        self.__customer = customer
        self.__carNumber = carNumber
        self.__timeOfOrder = timeOfOrder
        #self.__extras = extras
        self.__startDate = startDate
        self.__endDate = endDate
        self.__rentCost = rentCost
        #self.__status = status

    def __str__(self):
        return '{:15} {:15} {:15} {:15} {:15} {:15} {:6} ISK'.format(self.__orderNumber,self.__customer,self.__carNumber,\
        self.__timeOfOrder, self.__startDate, self.__endDate, self.__rentCost)
      
    
    def __repr__(self):
        return self.__str__()


    def getOrderNumber(self):
        return self.__orderNumber
    
    def getCustomer(self):
        return self.__customer

    def get_carNumber(self):
        return self.__carNumber

    #def getExtras(self):
     #   return self.__extras
    def getgetTimeOfOrder(self):
        return self.__timeOfOrder

    def getStartDate(self):
        return self.__startDate
    
    def getEndDate(self):
        return self.__endDate
    
    def getRentCost(self):
        return self.__rentCost
    
    #def getStatus(self):
     #   return self.__status