from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer
from models.Order import Order
from services.OrderService import OrderService
from datetime import datetime, timedelta
from models.Colors import Colors



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
            action = self.chooseAction()

            if action == '1' or action == '2':
                self.spaces()
                print(Colors.WHITE + "\nPath: Menu/Available_Cars/" + Colors.END)
                typeAction = ''
                dateAvailable = datetime.now()
                cars = self.__carService.getCars(action, typeAction, dateAvailable)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action,dateAvailable)
            
            # elif action == '2':
                # print("\n\033[1;37mPath: Menu/Unavailable_cars/\033[1;m")


            elif action == '3':
                self.spaces()
                print(Colors.WHITE + "\nPath: Menu/Creating_Customer/\n" + Colors.END)
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)
                print(Colors.GREEN + "\nCustomer has been created!\n" + Colors.END)
                action = self.pressAnythingToContinue()

            elif action == '5':
                self.spaces()
                self.findCustomerMenu()

            elif action == '4':
                self.spaces()
                self.createOrder()

            elif action == '6':####WORKING ON THIS
                #search for order by number
                pass
            
            elif action == '7':#####WORKING ON THIS
                self.spaces()
                orders, nothing = self.getAllOrders()
                self.displayAllOrders(orders)
                #print all orders and options

# Register a car
            elif action == '10':
                self.spaces()
                carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar = self.createCar()
                newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
                self.__carService.addCar(newCar)

# Prints out the pricelist for cars.
            elif action == '11':
                self.spaces()
                print(open('./data/pricelist.txt').read())
                action = self.pressAnythingToContinue()

# Prints exit message and exits the program.
            elif action == 'q':
                self.spaces()
                self.exitPrint()
                exit()

# Prints the mainMenuPage.
    def mainMenuPrint(self):
        print(Colors.BLUE + "___  ___     _       ___  ___")
        print("|  \/  |__ _(_)_ _   |  \/  |___ _ _ _  _ ")
        print("| |\/| / _` | | ' \  | |\/| / -_) ' \ || |")
        print(Colors.WHITE + "|_|  |_\__,_|_|_||_| |_|  |_\___|_||_\_,_|")
        print("\nPath: Menu/\n" + Colors.END)
        print(Colors.BLUE + "You can do the following:" + Colors.END)
        print(Colors.WHITE + "1.  List all available cars")
        print("2.  List all unavailable cars")
        print("3.  Register customer.")
        print("4.  Create car reservation.")
        print("5.  Find a customer.")
        print("6.  Look up an order.")
        print("7.  Show list of orders.")
        print("8.  Return a car.")
        print("9.  Edit order.")
        print("10. Register car")
        print("11. Prints out pricelist for cars."+Colors.END)
        print(Colors.BLUE+"Press q to quit\n"+Colors.END)
    

    '''----------Functions for repetitive code-----------'''
    def spaces(self):
        print('\n'*43)

    def chooseAction(self):
        action = input(Colors.BLUE + "\nChoose action: " + Colors.END)
        return action

    def pressAnythingToContinue(self):
        action = input(Colors.BLUE + "\nPress anything to continue: " + Colors.END)
        return action

    def actionsPrint(self):
        print("\n" + Colors.BLUE + "Actions: " + Colors.END)

    def customerFound(self):
        print(Colors.GREEN + "Customer found!" + Colors.END)

    def customerNotFound(self):
        print(Colors.RED + "Customer not found!" + Colors.END)

    def searchTermInput(self):
        searchTerm = input(Colors.BLUE + "Enter SSN or Customer number to find: " + Colors.END)
        return searchTerm

    def exitPrint(self):
        print(Colors.GREEN + "\nHave a nice day!"+ Colors.END)
        print(Colors.GREEN + "Exiting program.." + Colors.END)

    def allCustomersHeaderPrint(self):
        print(Colors.GREEN +
        "----------------------------------All Customers----------------------------------\n"
         + Colors.END)

    def allDeletedCustomerHeaderPrint(self):
        print(Colors.RED +
        "------------------------------All Deleted Customers------------------------------\n"
         + Colors.END)

    def creatingCustomerPrintHeader(self):
        print(Colors.GREEN + 
        "-----------Creating customer account-----------"
        + Colors.END)

    ''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
        self.spaces()
        self.findCustomerMenuPrint()
        action = self.chooseAction()

# Redirects the user to the mainMenuPage.
        if action == '0':
            self.mainMenu()

# Search engine that finds the customer.
        elif action == '1':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/Search_Existing/"+Colors.END)
            self.searchCustomerHeaderPrint()
            searchTerm = self.searchTermInput()
            customer = self.__customerService.findCustomer(searchTerm)

# If the customer is not found it prints not found message.
            if customer == None:
                self.spaces()
                print(Colors.WHITE+"Path: Menu/Find_Customer/Not_Found/\n"+Colors.END)
                self.customerNotFound()
                self.pressAnythingToContinue()
                self.findCustomerMenu()
    
# If the customer is found it prints found message.
            else:
                self.spaces()
                print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/\n"+Colors.END)
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print(customer)
                self.afterCustomerIsFoundMenu(customer)
#show all customers
        elif action == '2':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/All_Customers/\n"+Colors.END)
            self.allCustomersHeaderPrint()
            customers = self.__customerService.getAllCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressAnythingToContinue()
            self.findCustomerMenu()

# Shows all deleted customers.
        elif action == '3':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/All_Deleted_Customers/\n"+Colors.END)
            self.allDeletedCustomerHeaderPrint()
            customers = self.__customerService.getAllDeletedCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressAnythingToContinue()
            self.findCustomerMenu()

# Search engine in the deleted customers dir.
        elif action == '4':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/Search_Deleted/\n"+Colors.END)
            self.searchCustomerHeaderPrint()
            searchTerm = self.searchTermInput()
            customer = self.__customerService.findDeletedCustomer(searchTerm)

# If the customer is not found it prints not found message.
            if customer == None:
                self.spaces()
                self.customerNotFound()
                self.pressAnythingToContinue()
                self.findCustomerMenu()
            
# If the customer is found it prints found message.
            else:
                self.spaces()
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print(customer)
                self.afterDeletedCustomerIsFoundMenu(customer)

# After the customer is found the user can go back or reinstate the customer.
    def afterDeletedCustomerIsFoundMenu(self,customer):
        self.afterDeletedCustomerIsFoundPrint()
        action = self.chooseAction()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            customerNumber = customer.getNumber()
            self.__customerService.restoringCustomer(customerNumber)
        
# After the customer is found the user can go back and search another, edit or delete the customer.
    def afterCustomerIsFoundMenu(self, customer):
        self.afterCustomerIsFoundPrint()
        action = self.chooseAction()
        self.spaces()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            self.editCustomerInfo(customer)
        elif action == '2':
            self.warningMessageMenu(customer)
    
            
# The menu for editing the customer information, Number stays the same
    def editCustomerInfo(self,customer):
            self.editCustomerInfoMenu()
            cs = CustomerService()
            action = self.chooseAction()
# Edit customer name
            if action =='1':
                name = cs.inputNameCheck()
                age = customer.getAge()
                ssn = customer.getSsn()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
#Edit customer age
            if action =='2':
                name = customer.getName()
                age = cs.inputAgeCheck()
                ssn = customer.getSsn()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
#Edit customer ssn
            if action =='3':
                name = customer.getName()
                age = customer.getAge()
                ssn = cs.inputSsnCheck()
                address = customer.getAddress()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)
#Edit customer address
            if action =='4':
                
                name = customer.getName()
                age = age = customer.getAge()
                ssn = customer.getSsn()
                address = cs.inputAddressCheck()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)


#Edit all customer information
            if action == '5':
                cs = CustomerService()
                name = cs.inputNameCheck()
                age = cs.inputAgeCheck()
                ssn = cs.inputSsnCheck()
                address = cs.inputAddressCheck()
                number = customer.getNumber()
                newCustomer = Customer(name,age,ssn,address,number)
                cs.customerEdit(newCustomer)

# Safety function that asks the user if he is certain that he wants to delete the selected customer.
    def warningMessageMenu(self,customer):
        self.warningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.deletingCustomer(customerNumber)
                self.spaces()
                print(Colors.RED+"Customer "+Colors.GREEN+f"'{customer.getName()}'"+Colors.RED+" Deleted."+Colors.END)
                self.pressAnythingToContinue()
                self.spaces()
                self.afterCustomerIsFoundMenu(customer)
            elif action == '2':
                self.spaces()
                self.afterCustomerIsFoundMenu(customer)
            else:
                self.warningMessageMenu(customer)
        
# Creates a customer, calls a function in the service class to validate the input.
    def createCustomer(self):
        self.creatingCustomerPrintHeader()
        cs = CustomerService()
        name = cs.inputNameCheck()
        ssn, age = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = cs.getSumOfAllCustomers()
        return name,age,ssn,address,number


    '''-------------------------- CUSTOMER PRINT FUNCTIONS -----------------------'''
# Actions the user has after 5 is pressed on the mainPage.
    def findCustomerMenuPrint(self):
        print(Colors.WHITE+"Path: Menu/Find_Customer/"+Colors.END)
        self.actionsPrint()
        print(Colors.WHITE + "0. <-- Go back")
        print("1. Search for a customer")
        print("2. Show all customers")
        print("3. Show all deleted customers")
        print("4. Search for deleted customer"+Colors.END)

# The format which the customer is printed out on.
    def displayCustomerHeaderPrint(self):
        print("{:15} {:15} {:15} {:15} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("---------------",\
        "---------------","---------------", "--------------------", "---------------"))
# Comes after the displayCustomerHeaderPrint, prints out all the customers.
    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(customer)
    
# Header which is printed when user is searching for a customer.
    def searchCustomerHeaderPrint(self):
        print(Colors.YELLOW + 
        "--------------------------------------------Search for customer-------------------------------------------"
        + Colors.END)

# Prints the option to go back or reinstate the customer back into the main customer dir file.   VANTAR PATH
    def afterDeletedCustomerIsFoundPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Reinstate selected customer"+Colors.END)

# 
    def afterCustomerIsFoundPrint(self):                                                           # VANTAR PATH
        print("Path")
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer"+Colors.END)

# Print function that displays users action choice.
    def editCustomerInfoMenu(self):                                                                # VANTAR PATH
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Edit customer name")
        print("2. Edit customer age")
        print("3. Edit customer SSN")
        print("4. Edit customer address")
        print("5. Edit All customer information"+Colors.END)

# Prints when user chooses to delete a user.
    def warningMessagePrint(self,customer):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Deleted_Selected_Customer/"+Colors.END)
        print(Colors.GREEN + "\nSelected customer: " + Colors.END)
        self.displayCustomerHeaderPrint()
        print(customer)
        print(Colors.RED + "\nWarning: " + Colors.BLUE + "Are you sure you want to delete this customer?" + Colors.END)
        print(Colors.WHITE+"1. Yes, delete this customer")
        print("2. No, do not deleted this customer"+Colors.END)
    
    
    
    ''' -------------------- Car Functions -------------------- '''

    def showCarsByTypeMenu(self, typeAction,dateAvailable):
        while True:
            self.findCarTypeMenuPrint()
            action = self.chooseAction()
            if action == '0':
                break
            elif action == '1':
                action = 'compact'
            elif action == '2':
                action = 'comfort'
            elif action == '3':
                action = 'CUV'
            elif action == '4':
                action = 'highland'
            elif action == '5':
                action = 'luxury'
            else:
                self.invalidActionPrint()
                self.showCarsByTypeMenu(typeAction,dateAvailable)
            cars = self.__carService.getCars(typeAction, action,dateAvailable)
            self.displayAllCarsPrint(cars)

    def createCar(self):
        self.createCarPrint()
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

    '''----------------------------------CAR PRINT FUNCTIONS-----------------------------------------------'''
    def displayAllCarsPrint(self,cars):
        self.printCarHeader()
        for car in cars:
            print(car)

    def findCarTypeMenuPrint(self):
        print(Colors.BLUE + "\nShow only:" + Colors.END)
        print("0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")

    def createCarPrint(self):
        print("\nSelect from Car Types:")
        print("\n1. Compact")
        print("\n2. Comfort")
        print("\n3. CUV")
        print("\n4. Highland")
        print("\n5. Luxury")

    def printCarHeader(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
        'Color', 'Passengers','Transmission','Rent Cost'))
        print("{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))


    '''----------------------------------ORDER FUNCTIONS-----------------------------------------------'''
    def customerNotFoundMenu(self):
        self.customerNotFoundPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            self.createOrder()

    def rentOutToCustomerMenu(self):
        self.rentOutToCustomerPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            return
        else:
            print('\nPlease choose among available actions')
            self.rentOutToCustomerMenu()

    def selectCarType(self):
        self.selectCarTypePrintMenu()

        action = self.__orderService.checkCarTypeSelection()
        rentCost, carType = self.getCarTypeVariables(action)

        return rentCost, carType

    def getCostOfOrder(self, rentOutCarTime, returnCarTime, rentCost):
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
            totalDaysRented = daysRentedCount.days
        else:
            totalDaysRented = daysRented.days

        print("\nPrice for {} days: ".format(totalDaysRented))         

        totalCost = int(totalDaysRented) * rentCost

        print("Price: {} ISK".format(totalCost))

        return totalCost, totalDaysRented

    def addInsurance(self, cost):
        self.addInsurancePrint()
        action = self.chooseAction()
        insurance = 0
        if action == '1':
            totalCost = cost * 1.05
            insurance = cost * 0.05
        elif action == '2':
            totalCost = cost
            pass
        return int(totalCost), int(insurance)

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
        action = self.chooseAction()
        if action == '1':
            return True
        elif action == '2':
            return False

    def finalStepOrder(self, order):
        self.finalStepOrderPrint()
        action = self.chooseAction()
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
        self.searchCustomerForCarRentalHeaderPrint()
        searchTerm = self.searchTermInput()
        try:
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            ssn = customer.getSsn()
            self.customerFound()
            self.displayCustomerHeaderPrint()
            print(customer)
            self.rentOutToCustomerMenu()
        except:
            self.customerNotFound()
            self.customerNotFoundMenu()
        nothing, orderNumber = self.__orderService.getAllOrders()
        rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
        rentCost, carType = self.selectCarType()
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
        # Print out order
        # self.displayAllOrdersHeaderPrint()
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, ssn)
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        self.finalStepOrder(order)
        return 

    def displayAllOrders(self, orders):
        self.displayAllOrdersHeaderPrint()
        for order in orders:
            print(order) 
            #menu? 
    
    def returnCar(self):
        licenseplate = self.__carService.checkLicenseplate(False)
        self.printReturnMenu()
        action = input("Choose action: ")#error check
        if action == '0':
            self.returnCar()
        elif action == '1':
            timeOfReturn = self.__carService.checkValidDate()
            searchedCar = self.__carService.findCar(licenseplate, timeOfReturn)

    '''--------------------------ORDER PRINT FUNCTIONS--------------------------'''
    def rentOutToCustomerPrintMenu(self):
        print("\nActions:\n")
        print("0. Go back to main menu")
        print("1. Select customer")

    def customerNotFoundPrintMenu(self):
        print("\nActions:\n")
        print("0. Go back to main menu")
        print("1. Search again")

    def rentOutToCustomerPrintMenu(self):
        print("\nActions:\n")
        print("0. Go back to main menu")
        print("1. Select customer")

    def customerNotFoundPrintMenu(self):
        print("\nActions:\n")
        print("0. Go back to main menu")
        print("1. Search again")

    def selectCarTypePrintMenu(self):
        print("\nActions:")
        print("0. <-- Go back")
        print("1. Compact")
        print("2. Comfort")
        print("3. CUV")
        print("4. Highland")
        print("5. Luxury")

    def addInsurancePrint(self):
        print("\nActions:")
        print("1. Add SCDW(Includes):\n\t{0}\n\t{1}\n\t{2}\n\t{3}".format("-Front window","-Sandstorm","-Chassis", "-Theft insurance"))
        print("2. No additional insurance")

    def areYouSurePrint(self):
        print("\nAre you sure?")
        print("1. Yes")
        print("2. No, go back")

    def finalStepOrderPrint(self):
        self.actionsPrint()
        print("1. Save and complete order")
        print("2. Cancel order")

    def displayAllOrdersHeaderPrint(self):
        LINE = '---------------'
        print("\n{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:15}".format('Order number', 'Customer', 'SSN', 'Car Type',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE, LINE))

    def displayOrderInfo(self,order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
        print("\n-------------------------------------------------- Order Info --------------------------------------------------\n")
        print("Order Number: {}".format(order.getOrderNumber()))
        print("{} | {}".format(order.getCustomer(), order.getSSN()))
        print("Car type rented: {} | from: {} To: {} | Date rented: {}".format(order.getCarType(), rentOutCarTime, \
        returnCarTime, timeOfOrder))
        print("\nCost of {} days without VAT: {} ISK".format(totalDaysRented, carCost))
        if insurance != 0:
            print("Extra insurance: {} ISK".format(insurance))
            print("\nTotal cost of {} days without VAT: {} ISK".format(totalDaysRented, order.getRentCost()))

    def searchCustomerForCarRentalHeaderPrint(self):
        print("--------------------- Find customer for car rental ---------------------")
    
    def editOrderInfoMenu(self):
        print("0. Go back")
        print("1. ")
        #edit time of order, cancel, add/discard insurance, 

    def editCar(self):
        self.editCarInfoMenu()
        print("----------------Return a Car----------------")

    def printReturnMenu(self):
        print("0. Go back")
        print("1. Return selected car")

    def listofOrdersMenu(self):
        print("0. Go back")
        print("1. Search for an order by order number")