from repositories.OrderRepository import OrderRepository
from datetime import datetime, timedelta

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def getAllOrders(self):
        return self.__orderRepo.getOrders()#Problems <--------

    def addOrder(self, order):
        self.__orderRepo.addOrder(order)
    


    def checkValidDate(self, newOrder=False):#SEGJA AÐ SÉ SATT FYRIR NEW ORDER
        print("\nInput time of rental:")
        if newOrder == True:
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
                    return rentOutCar, returnCar, rentOutCarTime, returnCarTime
                else:
                    print('Please insert valid end of rental time')
        #ef ekki ný pöntun
        else:
            while True:
                print("\nInput time of return:")
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime.date >= datetime.now().date:
                    break
                else:
                    print('Please insert valid end of rental time')
                    return returnCar


        
        

    def getTime(self, date):
        try:
            day, month, year, hour, minutes = map(int, date.split('-'))
            return datetime(year, month, day, hour, minutes)
        except ValueError:
            print("Not a valid time")

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
                print("\nplease input a valid date\n")
        return finalDateTime

    def checkCarTypeSelection(self):
        while True:
            try:
                action = input("\nSelect car type for rental: ")
                checkint = int(action)
                if '0' <= action <= '5':
                    return action
            except:
                print("\nPlease choose from available options")



    # def getNewOrderNumber(self):
    #     return self.__orderRepo.getHighestOrderNumber()


    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)