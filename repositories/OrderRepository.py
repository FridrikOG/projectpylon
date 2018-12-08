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
            HIGHEST = 0
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
            

    def addCar(self, newCar):
        with open('./data/cars.csv', 'a') as carFile:
            carType = newCar.getType()
            make = newCar.getMake()
            color = newCar.getColor()
            passengers = newCar.getPassengers()
            transmission = newCar.getTransmission()
            licenseplate = newCar.getLicenseplate()
            rentCost = newCar.getRentcost()
            status = newCar.getStatus()
            rentOutCar = newCar.getRentOutCar()
            returnCar = newCar.getReturnCar()
            
            carFile.write("{},{},{},{},{},{},{},{},{},{}\n".format(carType,make,licenseplate,color,passengers,transmission,\
            rentCost,status,rentOutCar,returnCar))
        
            ###