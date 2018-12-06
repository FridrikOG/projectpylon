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

    def getOrders(self):
        with open('./data/orders.csv', 'r') as carFile:
            csvReader = csv.DictReader(carFile)

        for line in csvReader:
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
    # def getOrderFrameTime(self, start, end):#input from car datetime
    #     for order in self.__orders:
    #         if  


                
