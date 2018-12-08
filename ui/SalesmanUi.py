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
            self.spaces()
            self.mainMenuPrint()
            action = input('Action: ')

            if action == '1' or action == '2':
                print("\n\033[1;37mPath: Menu/Available_Cars/\033[1;m")
                typeAction = ''
                dateAvailable = datetime.now()
                cars = self.__carService.getCars(action, typeAction, dateAvailable)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action,dateAvailable)
            
            # elif action == '2':
                # print("\n\033[1;37mPath: Menu/Unavailable_cars/\033[1;m")


            elif action == '3':
                print("\n\033[1;37mPath: Menu/Creating_Customer/\n\033[1;m")
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)

            elif action == '5':
                self.findCustomerMenu()

            elif action == '4':
                self.createOrder()

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

            elif action == '11':
                print(open('./data/pricelist.txt').read())
                action = input("Press any button to return to main menu: ")

            elif action == 'q':
                print('\n\033[1;94mHave a nice day!\033[1;m')
                print('\033[1;94mExiting program..\033[1;m')
                exit()

    def mainMenuPrint(self):
        print("\033[1;94m___  ___     _       ___  ___")
        print("|  \/  |__ _(_)_ _   |  \/  |___ _ _ _  _ ")
        print("| |\/| / _` | | ' \  | |\/| / -_) ' \ || |")
        print("\033[1;37m|_|  |_\__,_|_|_||_| |_|  |_\___|_||_\_,_|")
        print("\nPath: Menu/")
        print("\n\033[1;94mYou can do the following:\033[1;m")
        print("1.  List all available cars")
        print("2.  List all unavailable cars")
        print("3.  Register customer.")
        print("4.  Create car reservation.")
        print("5.  Find a customer.")
        print("6.  Look up an order.")
        print("7.  Show list of orders.")
        print("8.  Return a car.")
        print("9.  Edit order.")
        print("10. Register car\033[1;m")
        print("\033[1;94mPress q to quit\033[1;m\n")
    
    def spaces(self):
        print('\n'*43)




#''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
        self.spaces()
        self.findCustomerMenuPrint()
        findCustomerAction = input("\033[1;94mChoose action: \033[1;m")
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
        print("\n\033[1;94mActions:\033[1;m")
        print("0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer")

    def afterCustomerIsFoundMenu(self, customer):
        afterCustomerFoundAction = input("Choose action: ")
        if afterCustomerFoundAction == '0':
            self.findCustomerMenu()
        elif afterCustomerFoundAction == '1':
            self.editCustomerInfo(customer)
        elif afterCustomerFoundAction == '2':
            self.warningMessagePrint(customer)
            self.warningMessageMenu(customer)
    
    def editCustomerInfoMenu(self):
            print("1. Edit customer name")
            print("2. Edit customer age")
            print("3. Edit customer SSN")
            print("4. Edit customer address")
            print("5. Edit All customer information")
            
# The menu for editing the customer information, Number stays the same
    def editCustomerInfo(self,customer):
            self.editCustomerInfoMenu()
            cs = CustomerService()
            afterEditCustomerSelectedAction = input("Choose action: ")
        # Edit customer name
            if afterEditCustomerSelectedAction =='1':
                name = cs.inputNameCheck()
                age = customer.getAge()
                ssn = customer.getSsn()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
        #Edit customer age
            if afterEditCustomerSelectedAction =='2':
                name = customer.getName()
                age = cs.inputAgeCheck()
                ssn = customer.getSsn()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
        #Edit customer ssn
            if afterEditCustomerSelectedAction =='3':
                name = customer.getName()
                age = customer.getAge()
                ssn = cs.inputSsnCheck()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
        #Edit customer address
            if afterEditCustomerSelectedAction =='4':
                
                name = customer.getName()
                age = age = customer.getAge()
                ssn = customer.getSsn()
                address = cs.inputAddressCheck()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)


        #Edit all customer information
            if afterEditCustomerSelectedAction == '5':
                cs = CustomerService()
                name = cs.inputNameCheck()
                age = cs.inputAgeCheck()
                ssn = cs.inputSsnCheck()
                address = cs.inputAddressCheck()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)


    def warningMessagePrint(self,customer):
        print("\n")
        print("Warning: Are you sure you want to delete this customer?")
        print(customer)
        print("\n")
        print("1. Yes, delete this customer")
        print("2. No, do not deleted this customer")

    def warningMessageMenu(self,customer):
        warningMessageAction = input("033[1;94mChoose action\033[1;m")
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

    # Displays options that the user has.
    def findCustomerMenuPrint(self):
        print("\n\033[1;94mActions\033[1;m")
        print("\n0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")

    def displayCustomerHeaderPrint(self):
        print("\n")
        print("{:15} {:15} {:15} {:15} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("---------------",\
        "---------------","---------------", "---------------", "---------------"))

    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(customer)
    
    
    def searchCustomerHeaderPrint(self):
        print("--------------------------------------------Search for customer-------------------------------------------")

    
    
    
# ''' -------------------- Car Functions -------------------- '''

    def findCarTypeMenuPrint(self):
        print("\n\033[1;94m0. <-- Go back\033[1;m")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")

    def showCarsByTypeMenu(self, action,dateAvailable):
        while True:
            self.findCarTypeMenuPrint()
            typeAction = input('\n\033[1;94mChoose action: \033[1;m')
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
        rentOutCar, unusedValue = self.getTimeOfOrder()
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
        elif carTypeInput == '2':
            carType = 'Comfort'
            rentCost = 20000
        elif carTypeInput == '3':
            carType = 'CUV'
            rentCost = 25000
        elif carTypeInput == '4':
            carType = 'Highland'
            rentCost = 30000
        elif carTypeInput == '5':
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
        else:
            totalDaysRented = daysRented.days

        print("\nDays Rented: ",totalDaysRented)

        totalCost = int(totalDaysRented) * rentCost

        print("Price: {} ISK".format(totalCost))

        return totalCost, totalDaysRented

    def addInsurance(self, cost):
        self.addInsurancePrint()
        action = input('\nChoose action: ')
        insurance = 0
        if action == '1':
            totalCost = cost * 1.05
            insurance = cost * 0.05
        elif action == '2':
            totalCost = cost
            pass
        return int(totalCost), int(insurance)


    def addInsurancePrint(self):
        print("\nActions:")
        print("1. Add SCDW:\n-Front window\n-Sandstorm\n-Chassis\n-Theft insurance")
        print("2. No additional insurance")

    def getTimeOfOrder(self):
        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day
        hour = datetime.now().hour
        minutes = datetime.now().minute
        timeOfOrder = datetime(year, month, day, hour, minutes)
        stringTimeOfOrder = '{}-{}-{}-{}-{}'.format(day, month, year, hour, minutes)
        return stringTimeOfOrder, timeOfOrder

    def areYouSure(self):
        self.areYouSurePrint()
        action = input("Choose action: ")
        if action == '1':
            return True
        elif action == '2':
            return False

    def areYouSurePrint(self):
        print("\nAre you sure?")
        print("1. Yes")
        print("2. Go back")


    def finalStepOrderPrint(self):
        print("\nActions")
        print("1. Save and complete order")
        print("2. Cancel order")

    def finalStepOrder(self, order):
        self.finalStepOrderPrint()
        action = input("Choose action")
        if action == '1':
            status = self.areYouSure()
            if status == True:
                self.__orderService.addOrder(order)
                print("Order complete!")
            else:
                self.finalStepOrder(order)
        elif action == '2':
            status = self.areYouSure()
            if status == True:
                self.mainMenu()
            else:
                self.finalStepOrder(order)


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
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
        # Print out order
        # self.displayAllOrdersHeaderPrint()
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, SSN)
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        self.finalStepOrder(order)
        return 


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
        print("\n{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:15}".format('Order number', 'Customer', 'SSN', 'Car Type',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE, LINE))

    def displayOrderInfo(self,order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
        print("\n--------------------------- Order Info ---------------------------\n")
        print("Order Number: {}".format(order.getOrderNumber()))
        print("{} | {}".format(order.getCustomer(), order.getSSN()))
        print("Car type rented: {} from: {} To: {} | Date rented: {}".format(order.getCarType(), rentOutCarTime, \
        returnCarTime, timeOfOrder))
        print("\nCost of {} days without VAT: {} ISK".format(totalDaysRented, carCost))
        if insurance != 0:
            print("Insurance: {} ISK".format(insurance))
            print("\nTotal cost of {} days without VAT: {} ISK".format(totalDaysRented, order.getRentCost()))


