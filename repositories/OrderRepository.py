from models.Order import Order
import csv
# form datetime import datetime
# CURRENTTIME = datetime.now()

class OrderRepository:
    def __init__(self):
        self.__orderNumbers = set()
        self.__orders = []
        self.__highestOrderNumber = []
        #self.__ordersInRental = []

    #geta sett inn og náð í gögn
    #hvernig fara gögnin inn í skránna
    #number, customer, car, cost, startDate, endDate
    #orderNumber, customer, carNumber, timeOfOrder, startDate, endDate, rentCost
    def getOrders(self):
        with open('./data/orders.csv', 'r') as orderFile:
            csvReader = csv.DictReader(orderFile, delimiter=',')
#orderNumber,customer,carNumber,timeOfOrder,startDate,endDate,rentCost
            for line in csvReader:#Problems <-----
                orderNumber= line['orderNumber']
                customer = line['customer']
                SSN = line['SSN']
                carType = line['carType']
                timeOfOrder = line['timeOfOrder']
                startDate= line['startDate']
                endDate = line['endDate']
                rentCost = line['rentCost']
                
                if orderNumber not in self.__orderNumbers:
                    self.__orderNumbers.add(int(orderNumber))
                    newOrder = Order(orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, SSN)
                    self.__orders.append(newOrder)
            newOrderNumber = max(self.__orderNumbers) + 1
        return self.__orders, newOrderNumber
            

    def addOrder(self, order):
        with open('./data/orders.csv', 'a') as orderFile:
            orderNumber = order.getOrderNumber()
            customer = order.getCustomer()
            carType = order.getCarType()
            timeOfOrder = order.getTimeOfOrder()
            startDate = order.getStartDate()
            endDate = order.getEndDate()
            rentCost = order.getRentCost()
            SSN = order.getSSN()

            orderFile.write("{},{},{},{},{},{},{},{}\n".format(orderNumber,customer,SSN,carType,timeOfOrder,startDate,endDate,rentCost))
        
            ###