from repositories.OrderRepository import OrderRepository

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def getAllOrders(self):
        return self.__orderRepo.getOrders()#Problems <--------

    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)