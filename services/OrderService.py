from repositories.OrderRepository import OrderRepository

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def getAllOrders(self):
        return self.__orderRepo.getOrders()#Problems <--------
    
    def checkValidDate(self):
        while True:
            try:
                dateInput = input('1/2 - Input date in this format DD-MM-YYYY: ')
                timeInput = input('2/2 - Input time in this format HH:MM: ')
                day, month, year = map(int, dateInput.split('-'))
                hour, minutes = map(int,timeInput.split(':'))
                finalDateTime = str(day + '-' + month + '-' + year + '-' + hour + '-' + minutes)
                break
            except:
                print("\nplease input valid date\n")
        return finalDateTime

    # def getNewOrderNumber(self):
    #     return self.__orderRepo.getHighestOrderNumber()


    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)