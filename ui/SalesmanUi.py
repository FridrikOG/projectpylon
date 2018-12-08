from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Order import Order
from services.OrderService import OrderService
from datetime import datetime, timedelta



class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()
        self.__orderService = OrderService()

    def mainMenu(self):

        action = ''
        while action != 'q':
            self.mainMenuPrint()
            action = input('Action: ')

            if action == '1' or action == '2':
                typeAction = ''
                dateAvailable = datetime.now()
                cars = self.__carService.getCars(action, typeAction, dateAvailable)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action,dateAvailable)


            elif action == '3':
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)

            elif action == '5':
                self.findCustomerMenu()

            elif action == '4':
                orderNumber, customer, carNumber, carType, timeOfOrder, startDate, endDate, rentCost = self.createOrder()
                # newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
                # self.__carService.addCar(newCar)

            elif action == '6':####WORKING ON THIS
                #search for order by number
                pass
            
            elif action == '7':#####WORKING ON THIS
                orders, nothing = self.S.getAllOrders()
                self.displayAllOrders(orders)
                #print all orders and options

            elif action == '10':
                carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar = self.createCar()
                newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
                self.__carService.addCar(newCar)

    def mainMenuPrint(self):
        print("\nYou can do the following: ")
        print("1.  List all available cars")
        print("2.  List all unavailable cars")
        print("3.  Register customer.")
        print("4.  Create car reservation.")
        print("5.  Find a customer.")
        print("6.  Look up an order.")
        print("7.  Show list of orders.")
        print("8.  Return a car.")
        print("9.  Edit order.")
        print("10. Register car")
        print("press q to quit\n")




# ''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
        self.findCustomerMenuPrint()
        findCustomerAction = input("Choose action: ")

    #Going to menu
        if findCustomerAction == '0':
            self.mainMenu()

    #Finding customer
        elif findCustomerAction == '1':
            self.searchCustomerHeaderPrint()
            searchTerm = input("Input SSN or Customernumber to find: ")
            customer = self.__customerService.findCustomer(searchTerm)
            if customer == None:
                print()
                print("Customer not found!")
                self.findCustomerMenu()
            else:
                self.displayCustomerHeaderPrint() #This displays the customer
                print(customer)
                self.afterCustomerIsFoundPrint()
                self.afterCustomerIsFoundMenu(customer)

    #show all customers
        elif findCustomerAction == '2':
            customers = self.__customerService.getAllCustomers()
            self.displayAllCustomersPrint(customers)
            self.findCustomerMenu()

    def afterCustomerIsFoundPrint(self):
        print("\nActions:\n")
        print("0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer")

    def afterCustomerIsFoundMenu(self, customer):
        afterCustomerFoundAction = input("Choose action: ")
        if afterCustomerFoundAction == '0':
            self.findCustomerMenu()
        #elif afterCustomerFoundAction == '1':
        #    self.editCustomerInfo()
        elif afterCustomerFoundAction == '2':
            customerNumber = customer.getNumber()
            self.__customerService.deletingCustomer(customerNumber)

    def editCustomerInfoMenu(self):
            print("1. Edit customer name")
            print("2. Edit customer age")
            print("3. Edit customer SSN")
            print("4. Edit customer address")
            print("5. Edit All customer information")
            
    def editCustomerInfo(self,customer):
            self.editCustomerInfoMenu()
            cs = CustomerService()
            afterEditCustomerSelectedAction = input("Choose action: ")
            if afterEditCustomerSelectedAction == '5':
                cs.customerEdit(customer)

    def warningMessagePrint(self,customer):
        print("\n")
        print("Warning: Are you sure you want to delete this customer?")
        print(customer)
        print("\n")
        print("1. Yes, delete this customer")
        print("2. No, do not deleted this customer")

    def warningMessageMenu(self,customer):
        warningMessageAction = input("Choose action")
        while warningMessageAction:
            if warningMessageAction == '1':
                customerNumber = customer.getNumber()
                self.__customerService.deletingCustomer(customerNumber)
                self.afterCustomerIsFoundMenu(customer)
            elif warningMessageAction == '2':
                self.afterCustomerIsFoundMenu(customer)
            else:
                self.warningMessageMenu(customer)

    def createCustomer(self):
        print("-----------Creating customer account-----------")
        cs = CustomerService()
        name = cs.inputNameCheck()
        age = cs.inputAgeCheck()
        ssn = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = cs.getSumOfAllCustomers()
        return name,age,ssn,address,number

    def countingCustomers(self):
        listOfSsn = self.__customerService.countingCustomers()
        return len(listOfSsn)

    # Displays options that the user has.
    def findCustomerMenuPrint(self):
        print("0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")

    def displayCustomerHeaderPrint(self):
        print("{:15} {:15} {:15} {:15} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("---------------",\
        "---------------","---------------", "---------------", "---------------"))

    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(customer)

    
    def searchCustomerHeaderPrint(self):
        print("--------------------------------------------Search for customer-------------------------------------------")

    def invalidActionPrint(self):
        print("Invalid Action !")


    
    
    
# ''' -------------------- Car Functions -------------------- '''

    def findCarTypeMenuPrint(self):
        print("0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")

    def showCarsByTypeMenu(self, action,dateAvailable):
        while True:
            self.findCarTypeMenuPrint()
            typeAction = input('\nChoose action: ')
            if typeAction == '0':
                break
            elif typeAction == '1':
                typeAction = 'compact'
            elif typeAction == '2':
                typeAction = 'comfort'
            elif typeAction == '3':
                typeAction = 'CUV'
            elif typeAction == '4':
                typeAction = 'highland'
            elif typeAction == '5':
                typeAction = 'luxury'
            else:
                self.invalidActionPrint()
                self.showCarsByTypeMenu(action,dateAvailable)
            cars = self.__carService.getCars(action, typeAction,dateAvailable)
            self.displayAllCarsPrint(cars)

    def createCar(self):
        print("\nSelect from Car Types:\n1. Compact\n2. Comfort\n3. CUV\
                \n4. Highland\n5. Luxury\n")
        #car type
        carTypeInput = self.__carService.checkCarType()
        make = input('Make (f.x. Toyota Yaris): ').capitalize()
        color = input('Color: ').capitalize()
        passengers = self.__carService.checkPassengers()
        transmissionInput = self.__carService.checkTransmission()
        licenseplate = self.__carService.checkLicenseplate()

        transmission = self.getTransmission(transmissionInput)
        rentCost, carType = self.getCarTypeVariables(carTypeInput)
        status = 'available'
        rentOutCar = self.__carService.checkValidDate()
        returnCar = rentOutCar
        newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        print("\nCar successfully created!")
        self.printCarHeader()
        print(newCar)
        return carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar


    def getTransmission(self, transmissionInput):
        if transmissionInput == 1:
            transmission = 'Auto'
        else:
            transmission = 'Manual'
        return transmission

    def getCarTypeVariables(self,carTypeInput):
        if carTypeInput == '1':
            carType = 'Compact'
            rentCost = 14000
        if carTypeInput == '2':
            carType = 'Comfort'
            rentCost = 20000
        if carTypeInput == '3':
            carType = 'CUV'
            rentCost = 25000
        if carTypeInput == '4':
            carType = 'Highland'
            rentCost = 30000
        if carTypeInput == '5':
            carType = 'Luxury'
            rentCost = 35000
        return rentCost, carType

    def displayAllCarsPrint(self,cars):
        self.printCarHeader()
        for car in cars:
            print(car)

    def printCarHeader(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
        'Color', 'Passengers','Transmission','Rent Cost'))
        print("{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))


# '''----------------------------------ORDER FUNCTIONS-----------------------------------------------'''

    def rentOutToCustomerPrintMenu(self):
        print("\nActions:\n")
        print("0. Go back to main menu")
        print("1. Select customer")

    def customerNotFoundPrintMenu(self):
        print("\nActions:\n")
        print("0. Go back to main menu")
        print("1. Search again")

    def customerNotFoundMenu(self):
        self.customerNotFoundPrintMenu()
        action = input("Choose action: ")
        if action == '0':
            self.mainMenu()
        elif action == '1':
            self.createOrder()

    def rentOutToCustomerMenu(self):
        self.rentOutToCustomerPrintMenu()
        action = input("Choose action: ")
        if action == '0':
            self.mainMenu()
        elif action == '1':
            return
        else:
            print('\nPlease choose among available actions')
            self.rentOutToCustomerMenu()

    def selectCarType(self):
        self.selectCarTypePrintMenu()
        action = input('Select car type for rental: ')
        rentCost, carType = self.getCarTypeVariables(action)

        return rentCost, carType


    def selectCarTypePrintMenu(self):
        print("\nActions:")
        print("0. <-- Go back")
        print("1. Compact")
        print("2. Comfort")
        print("3. CUV")
        print("4. Highland")
        print("5. Luxury")

    def getCostOfOrder(self, rentOutCarTime, returnCarTime, rentCost):
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
        totalDaysRented = daysRentedCount.days

        print("Days Rented: ",totalDaysRented)

        totalCost = int(totalDaysRented) * rentCost

        print("Price: {} ISK".format(totalCost))

        return totalCost


    def createOrder(self):
        #Order Number
        print("--------------------- Find customer for car rental ---------------------")
        searchTerm = input("Enter customer SSN: ")
        try:
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            SSN = customer.getSsn()
            self.displayCustomerHeaderPrint()
            print(customer)
            self.rentOutToCustomerMenu()
        except:
            print("Customer not found")
            self.customerNotFoundMenu()
        nothing, orderNumber = self.__orderService.getAllOrders()
        rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate()
        rentCost, carType = self.selectCarType()
        totalCost = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        # cars = self.__carService.getCars(action, carType, rentOutCarTime)
        # self.displayAllCarsPrint(cars)
        # self.showCarsByTypeMenu(action,rentOutCarTime)



        # #car type
        # carTypeInput = self.__carService.checkCarType()
        # make = input('Make (f.x. Toyota Yaris): ').capitalize()
        # color = input('Color: ').capitalize()
        # passengers = self.__carService.checkPassengers()
        # transmissionInput = self.__carService.checkTransmission()
        # licenseplate = self.__carService.checkLicenseplate()

        # transmission = self.getTransmission(transmissionInput)
        # rentCost, carType = self.getCarTypeVariables(carTypeInput)
        # status = 'available'
        # rentOutCar = self.__carService.checkValidDate()
        # returnCar = rentOutCar
        # newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        # print("\nCar successfully created!")
        # self.printCarHeader()
        # print(newCar)
        # return orderNumber, customer, carNumber, carType, timeOfOrder, startDate, endDate, rentCost

    def displayAllOrders(self, orders):
        self.displayAllOrdersHeaderPrint()
        for order in orders:
            print(order) 
            #menu?   

    def listofOrdersMenu(self):
        print("0. Go back")
        print("1. Search for an order by order number")



    def displayAllOrdersHeaderPrint(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format('Order number', 'Customer', 'Car number',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))
