from repositories.OrderRepository import OrderRepository

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def getAllOrders(self):#ekki endilega rétt nöfn
        return self.__orderRepo.getOrders()

    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)

