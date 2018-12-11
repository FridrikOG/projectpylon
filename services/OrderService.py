from repositories.OrderRepository import OrderRepository
from datetime import datetime, timedelta
from models.Colors import Colors

class OrderService:
    
    def __init__(self):
        self.__orderRepo = OrderRepository()

    def getAllOrders(self):
        return self.__orderRepo.getOrders()#Problems <--------

    def addOrder(self, order):
        self.__orderRepo.addOrder(order)

    def createDate(self, rentDate):
        day, month, year, hour, minutes = map(int, rentDate.split('-'))
        return datetime(year, month, day, hour, minutes)

    def checkValidDate(self, newOrder=False):#SEGJA AÐ SÉ SATT FYRIR NEW ORDER

        if newOrder == True:
            while True:
                print(Colors.BLUE+"\nInput time of rental:"+Colors.END)
                rentOutCar = self.InputValidDate()
                rentOutCarTime = self.getTime(rentOutCar)
                if rentOutCarTime > datetime.now():
                    break
                else: 
                    print(Colors.WHITE+'\nPlease insert valid start of rental time\n'+Colors.END)
                    
            while True:
                print(Colors.BLUE+"\nInput time of return:"+Colors.END)
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime > rentOutCarTime:
                    return rentOutCar, returnCar, rentOutCarTime, returnCarTime
                else:
                    print('Please insert valid end of rental time')
        #ef ekki ný pöntun
        else:
            while True:
                print(Colors.BLUE+"\nInput time of return:"+Colors.END)
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime.day >= datetime.now().day and returnCarTime.month >= datetime.now().month:
                    break
                else:
                    print('Please insert valid end of rental time')
            return returnCar


        
        

    def getTime(self, date):
        try:
            day, month, year, hour, minutes = map(int, date.split('-'))
            return datetime(year, month, day, hour, minutes)
        except ValueError:
            print(Colors.WHITE+"Not a valid time"+Colors.END)

    def InputValidDate(self):
        while True:
            try:
                dateInput = input(Colors.WHITE+'1/2 - Input date in this format DD-MM-YYYY: '+Colors.END)
                timeInput = input(Colors.WHITE+'2/2 - Input time in this format HH:MM: '+Colors.END)
                day, month, year = map(int, dateInput.split('-'))
                hour, minutes = map(int,timeInput.split(':'))
                finalDateTime = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
                break
            except:
                print(Colors.WHITE+"\nplease input a valid date\n"+Colors.WHITE)
        return finalDateTime

    def checkCarTypeSelection(self):
        while True:
            try:
                action = input(Colors.BLUE+"\nSelect car type for rental: "+Colors.END)
                checkint = int(action)
                if '0' <= action <= '5':
                    return action
            except:
                print(Colors.WHITE+"\nPlease choose from available options"+Colors.END)



    # def getNewOrderNumber(self):
    #     return self.__orderRepo.getHighestOrderNumber()


    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)