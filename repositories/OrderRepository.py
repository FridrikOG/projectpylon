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

    #number, customer, car, cost, startDate, endDate
    #orderNumber, customer, carNumber, timeOfOrder, startDate, endDate, rentCost
    def getOrders(self):
        with open('./data/orders.csv', 'r') as orderFile:
            csvReader = csv.DictReader(orderFile, delimiter=',')
#orderNumber,customer,carNumber,timeOfOrder,startDate,endDate,rentCost
            for line in csvReader:#Problems <-----
                orderNumber= line['orderNumber']
                customer = line['customer']
                ssn = line['SSN']
                carType = line['carType']
                timeOfOrder = line['timeOfOrder']
                startDate= line['startDate']
                endDate = line['endDate']
                rentCost = line['rentCost']
                if int(orderNumber) not in self.__orderNumbers:
                    self.__orderNumbers.add(int(orderNumber))
                    newOrder = Order(orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, ssn)
                    self.__orders.append(newOrder)
            try:
                newOrderNumber = max(self.__orderNumbers) + 1
            except:
                newOrderNumber = 1
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
            ssn = order.getSsn()

            orderFile.write("{},{},{},{},{},{},{},{}\n".format(orderNumber,customer,ssn,carType,timeOfOrder,startDate,endDate,rentCost))
        
    def checkOrderNumber(self, orderNumber):
        with open ('./data/orders.csv', 'r') as orderFile:
            csvReader = csv.DictReader(orderFile)
            for line in csvReader:
                orderNumberInFile = line['orderNumber']
                if orderNumber == orderNumberInFile:
                    return True         
            return False

    def findOrder(self, searchedOrderNumber):#duplicate code of checkordernumber
        with open ('./data/orders.csv', 'r') as orderFile:
            csvReader = csv.DictReader(orderFile)
            for line in csvReader:
                orderNumber= line['orderNumber']
                customer = line['customer']
                SSN = line['SSN']
                carType = line['carType']
                timeOfOrder = line['timeOfOrder']
                startDate= line['startDate']
                endDate = line['endDate']
                rentCost = line['rentCost']
                if searchedOrderNumber == orderNumber:
                    foundOrder = Order(orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, SSN)
                    return foundOrder

#VARIABLES BELOW ARE FROM 3 INPUTS
# '2', totalCost, carType, orderNumber
# ('2', orderNumber, totalCost, carType)
# ('1', orderNumber, startOfRental, endOfRental, rentCost)

# '2', totalCost, carType, orderNumber
    def editOrderVariable(self, variable, orderNumber, variable1=0, variable2=0, variable3=0):#fá fyrst hvaða gildum á að breyta áður en farið hingað
        with open ('./data/orders.csv', 'r') as orderFile:
            header = ('orderNumber','customer','SSN','carType','timeOfOrder','startDate','endDate','rentCost')
            csvReader = csv.DictReader(orderFile, header)
            next(orderFile, None)
            lines = []
            for line in csvReader:
                if line['orderNumber'] == orderNumber:
                    orderNumber= line['orderNumber']
                    customer = line['customer']
                    SSN = line['SSN']
                    carType = line['carType']
                    timeOfOrder = line['timeOfOrder']
                    startDate= line['startDate']
                    endDate = line['endDate']
                    rentCost = line['rentCost']
                    
                    if variable == '1':
                        startDate = variable1
                        endDate = variable2
                        rentCost = variable3
                        lines.append(line)
                        updatedOrder = Order(orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, SSN)

                    elif variable == '2':
                        rentCost = variable1
                        carType = variable2
                        lines.append(line)
                        updatedOrder = Order(orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, SSN)
                    
                    elif variable == '3':
                        updatedOrder = Order(orderNumber, customer, carType, timeOfOrder, startDate, endDate, rentCost, SSN)
                else:
                    lines.append(line)

        
        with open ('./data/orders.csv', 'w') as orderFile:
            writer = csv.DictWriter(orderFile, fieldnames=header)
            writer.writeheader()
            writer.writerows(lines)
        #return car info
        return updatedOrder