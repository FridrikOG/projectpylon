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
                print(Colors.WHITE+"\nInsert credit card information for insurance in this format XXXX-XXXX-XXXX-XXXX"+Colors.END)
                creditCard = input(Colors.WHITE+"Credit card: "+Colors.END).strip()
                if len(creditCard) == 19:
                    creditList = creditCard.split('-')
                    for split in creditList:
                        if len(split) == 4:
                            int(creditList[0])
                            int(creditList[1])
                            int(creditList[2])
                            int(creditList[3])
                            return creditCard
                        else:
                            self.insertValidCardPrint()
                else:
                    self.insertValidCardPrint()
            except:
                self.insertValidCardPrint()

    def insertValidCardPrint(self):
        print(Colors.BLUE+"\nPlease insert a valid credit card"+Colors.END)


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
                    print(Colors.WHITE+'Please insert valid end of rental time'+Colors.END)
        #ef ekki ný pöntun
        else:
            while True:
                print(Colors.BLUE+"\nInput time of return:"+Colors.END)
                returnCar = self.InputValidDate()
                returnCarTime = self.getTime(returnCar)
                if returnCarTime.day == datetime.now().day and returnCarTime.month == datetime.now().month:
                    break
                else:
                    print(Colors.BLUE+"Please insert valid end of rental time"+Colors.END)
            return returnCar

    def checkOrderNumber(self):
        numberExists = True
        while numberExists:
            try:
                orderNumber = input(Colors.BLUE+"Enter Order number: "+Colors.END).strip()
                intOrder = int(orderNumber)
                if numberExists == self.__orderRepo.checkOrderNumber(orderNumber):
                    orderInfo = self.__orderRepo.findOrder(orderNumber)
                    return orderNumber, orderInfo
                else:
                    print(Colors.RED+"Order number does not exist"+Colors.END)
            except:
                print(Colors.RED+"Order number does not exist"+Colors.END)
                print("\n" + Colors.BLUE + "Actions: " + Colors.END)
                print(Colors.WHITE+"0. Go back to main menu")
                print("1. Input order number again"+Colors.END)
                action = input(Colors.BLUE + "\nChoose action: " + Colors.END).strip()
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
            print(Colors.BLUE+"Not a valid time"+Colors.END)
            return datetime(1,1,1)

    def InputValidDate(self):
        while True:
            try:
                dateInput = input(Colors.WHITE+'1/2 - Input date in this format DD-MM-YYYY: '+Colors.END).strip()
                timeInput = input(Colors.WHITE+'2/2 - Input time in this format HH:MM: '+Colors.END).strip()
                day, month, year = map(int, dateInput.split('-'))
                hour, minutes = map(int,timeInput.split(':'))
                finalDateTime = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
                break
            except:
                print(Colors.BLUE+"\nplease input a valid date\n"+Colors.END)
        return finalDateTime

    def checkCarTypeSelection(self):
        while True:
            try:
                action = input(Colors.BLUE+"\nSelect car type for rental: "+Colors.END).strip()
                checkint = int(action)
                if '1' <= action <= '5':
                    return action
                else:
                    print(Colors.WHITE+"\nPlease choose from available options"+Colors.END)


            except:
                print(Colors.WHITE+"\nPlease choose from available options"+Colors.END)



    # def getNewOrderNumber(self):
    #     return self.__orderRepo.getHighestOrderNumber()


    # def addOrder(self, newOrder):
    #     self.__orderRepo.addOrder(newOrder)