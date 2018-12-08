from repositories.OrderRepository import OrderRepository
from datetime import datetime, timedelta

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def getAllOrders(self):
        return self.__orderRepo.getOrders()#Problems <--------
    



    def checkValidDate(self):
        print("\nInput time of rental:")
        
        while True:
            rentOutCar = self.InputValidDate()
            rentOutCarTime = self.getTime(rentOutCar)
            if rentOutCarTime > datetime.now():
                break
            else: 
                print('\nPlease insert valid start of rental time\n')
                
        while True:
            print("\nInput time of return:")
            returnCar = self.InputValidDate()
            returnCarTime = self.getTime(returnCar)
            if returnCarTime > rentOutCarTime:
                break
            else:
                print('Please insert valid end of rental time')

        return rentOutCar, returnCar, rentOutCarTime, returnCarTime
        

    def getTime(self, date):
        day, month, year, hour, minutes = map(int, date.split('-'))
        return datetime(year, month, day, hour, minutes)

    def InputValidDate(self):
        while True:
            try:
                dateInput = input('1/2 - Input date in this format DD-MM-YYYY: ')
                timeInput = input('2/2 - Input time in this format HH:MM: ')
                day, month, year = map(int, dateInput.split('-'))
                hour, minutes = map(int,timeInput.split(':'))
                finalDateTime = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
                break
            except:
                print("\nplease input valid date\n")
        return finalDateTime

    # def getNewOrderNumber(self):
    #     return self.__orderRepo.getHighestOrderNumber()


    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)