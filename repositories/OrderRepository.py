from models.Order import Order
import csv
# form datetime import datetime
# CURRENTTIME = datetime.now()

class OrderRepository:
    def __init__(self):
        self.__orderNumbers = set()
        self.__orders = []
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
                carNumber = line['carNumber']
                timeOfOrder = line['timeOfOrder']
                startDate= line['startDate']
                endDate = line['endDate']
                rentCost = line['rentCost']
                
                if orderNumber not in self.__orders:
                    self.__orderNumbers.add(orderNumber)
                    newOrder = Order(orderNumber, customer, carNumber, timeOfOrder, startDate, endDate, rentCost)
                    self.__orders.append(newOrder)
        return self.__orders
        
            ###