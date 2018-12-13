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

    def creditCardInfo(self):
        while True:
            try:
                print("\nInsert credit card information for insurance in this format XXXX-XXXX-XXXX-XXXX")
                creditCard = input("Credit card: ")
                if len(creditCard) == 19:
                    creditList = creditCard.split('-')
                    for split in creditList:
                        int(split)
                        if len(split) == 4:
                            return creditCard
                        else:
                            self.isnsertValidCardPrint()
                else:
                    self.isnsertValidCardPrint()
            except:
                self.isnsertValidCardPrint()

    def isnsertValidCardPrint(self):
        print("\nPlease insert a valid credit card")


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
                    print("Please input a valid date")
                    
            while True:
                print(Colors.BLUE+"\nInput time of return:"+Colors.END)
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime > rentOutCarTime:
                    return rentOutCar, returnCar, rentOutCarTime, returnCarTime
                else:
                    pass
        #ef ekki ný pöntun
        else:
            while True:
                print(Colors.BLUE+"\nInput time of return:"+Colors.END)
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime.day == datetime.now().day and returnCarTime.month >= datetime.now().month:
                    break
                else:
                    print("Please input a valid date")
            return returnCar

    def checkOrderNumber(self):
        numberExists = True
        while numberExists:
            try:
                orderNumber = input("Enter Order number: ")
                intOrder = int(orderNumber)
                if numberExists == self.__orderRepo.checkOrderNumber(orderNumber):
                    orderInfo = self.__orderRepo.findOrder(orderNumber)
                    return orderNumber, orderInfo
            except:
                print("Order number does not exist")
                print("\n" + Colors.BLUE + "Actions: " + Colors.END)
                print("0. Go back to main menu")
                print("1. Input order number again")
                action = input(Colors.BLUE + "\nChoose action: " + Colors.END)
                if action == '0':
                    break 
                elif action == '1':
                    pass

    def editTimeOfRental(self, startOfRental, endOfRental, rentCost, orderNumber):
        #     #edit order
        updatedOrder = self.__orderRepo.editOrderVariable('1', orderNumber, startOfRental, endOfRental, rentCost)
        return updatedOrder

    def editCarType(self, totalCost, carType, orderNumber):
        updatedCar = self.__orderRepo.editOrderVariable('2', orderNumber, totalCost, carType)
        return updatedCar

    def cancelOrder(self, orderNumber):
        canceledOrder = self.__orderRepo.editOrderVariable('3', orderNumber)
        return canceledOrder


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
                timeInput = input(Colors.WHITE+'2/2 - Input time of day in this format HH:MM: '+Colors.END)
                day, month, year = map(int, dateInput.split('-'))
                hour, minutes = map(int,timeInput.split(':'))
                finalDateTime = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
                break
            except:
                print('Please insert valid end of rental time')
                print("0. Go back to main menu")
                print("1. Input date again")
                action = input(Colors.BLUE + "\nChoose action: " + Colors.END)
                if action == '0':
                    break
                    
                elif action == '1':
                    pass
                
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