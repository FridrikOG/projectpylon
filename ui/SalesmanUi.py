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
            self.mainMenuPrint()
            action = self.chooseAction()

            if action == '1' or action == '2':
                typeAction = ''
                dateAvailable = datetime.now()
                if action == '1':
                    self.allAvailableCars()
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/" + Colors.END)
                elif action == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/" + Colors.END)
                    self.allUnAvilableCars()
                cars = self.__carService.getCars(action, typeAction, dateAvailable)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action,dateAvailable)

            
# Find a customer
            elif action == '3':
                print(Colors.WHITE + "\nPath: Menu/Find_Customer/" + Colors.END)
                self.findCustomerMenu()
# Register a customer
            elif action == '4':
                print(Colors.WHITE + "\nPath: Menu/Creating_Customer/\n" + Colors.END)
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)
                print(Colors.GREEN + "\nCustomer has been created!\n" + Colors.END)
                action = self.pressEnterToContinue()

# Create a car order
            elif action == '5':
                print(Colors.WHITE + "\nPath: Menu/Create_Car_Order/" + Colors.END)
                self.createOrder()
# Lookup an Order
            elif action == '6':####WORKING ON THIS
                print(Colors.WHITE + "\nPath: Menu/Look_Up_Order/" + Colors.END)

                self.editOrderInfoMenu()

# Show a list of orders
            elif action == '7':#####WORKING ON THIS
                print(Colors.WHITE + "\nPath: Menu/List_Of_Orders/" + Colors.END)
                orders, nothing = self.__orderService.getAllOrders()
                self.displayAllOrders(orders)
                self.pressEnterToContinue()
                #print all orders and options
# Rent out a car
            elif action == '8':
                print(Colors.WHITE + "\nPath: Menu/Rent_Out_Car/" + Colors.END)
                self.rentOutACar()
# Return a car
            elif action == '9':
                print(Colors.WHITE + "\nPath: Menu/Return_Car/" + Colors.END)
                self.returnCar()

# Register a car
            elif action == '10':
                print(Colors.WHITE + "\nPath: Menu/Register_New_Car/" + Colors.END)
                newCar = self.createCar()
                self.__carService.addCar(newCar)
# Edit a car
            elif action == '11':
                print(Colors.WHITE + "\nPath: Menu/Edit_Car/" + Colors.END)
                self.editCar()

# Prints out the pricelist for cars.
            elif action == '12':
                print(Colors.WHITE + "\nPath: Menu/Pricelist/" + Colors.END)
                print(open('./data/pricelist.txt').read())
                action = self.pressEnterToContinue()

# Prints exit message and exits the program.
            elif action == 'q':
                self.spaces()
                self.exitPrint()
                exit()
# unwanted action gets recognized and gives feedback to the user.
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.mainMenu()

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
        print("3.  Find a customer")
        print("4.  Register customer")
        print("5.  Create a car order")
        print("6.  Look up an order")
        print("7.  Show list of orders")
        print("8.  Rent out a car")
        print("9.  Return a car")
        print("10. Register car")
        print("11. Edit a car")
        print("12. Pricelist for cars."+Colors.END)
        print(Colors.BLUE+"Press q to quit\n"+Colors.END)
    

    '''----------Functions for repetitive code-----------'''
    def spaces(self):
        print('\n'*43)

    def chooseAction(self):
        action = input(Colors.BLUE + "\nChoose action: " + Colors.END)
        return action

    def pressEnterToContinue(self):
        action = input(Colors.BLUE + "\nPress enter to continue: " + Colors.END)
        return action

    def actionsPrint(self):
        print("\n" + Colors.BLUE + "Actions: " + Colors.END)

    def customerFound(self):
        print(Colors.GREEN + "Customer found!\n" + Colors.END)

    def customerNotFound(self):
        print(Colors.RED + "\nCustomer not found!" + Colors.END)

    def searchTermInput(self):
        searchTerm = input(Colors.BLUE + "\nEnter SSN or Customer number to find: " + Colors.END)
        return searchTerm

    def exitPrint(self):
        print(Colors.GREEN + "\nHave a nice day!"+ Colors.END)
        print(Colors.GREEN + "Exiting program.." + Colors.END)

    def allCustomersHeaderPrint(self):
        print(Colors.GREEN +
        "---------------------------------- ALL CUSTOMERS ----------------------------------\n"
         + Colors.END)

    def allDeletedCustomerHeaderPrint(self):
        print(Colors.RED +
        "------------------------------ All Deleted Customers ------------------------------\n"
         + Colors.END)

    def allAvailableCars(self):
        print(Colors.GREEN +
        "---------------------------------------------- ALL Available Cars ----------------------------------------------\n"
         + Colors.END)

    def allUnAvilableCars(self):
        print(Colors.RED +
        "--------------------------------------------- ALL Unavailable Cars ---------------------------------------------\n"
         + Colors.END)

    def creatingCustomerPrintHeader(self):
        print(Colors.GREEN + 
        "-----------Creating Customer Account-----------"
        + Colors.END)

    def invalidAction(self,action):
        print(Colors.RED+"\nAction "+Colors.WHITE+f"'{action}'"+Colors.RED+" is not a valid action!"+Colors.END)
        # else:
        # self.invalidAction(action)
        # self.pressEnterToContinue()
        # self.showCarsByTypeMenu(typeAction,dateAvailable)

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
                self.pressEnterToContinue()
                self.findCustomerMenu()
    
# If the customer is found it prints found message.
            else:
                self.spaces()
                print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/\n"+Colors.END)
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print(Colors.WHITE+(str(customer)+Colors.END))
                self.afterCustomerIsFoundMenu(customer)
#show all customers
        elif action == '2':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/All_Customers/\n"+Colors.END)
            self.allCustomersHeaderPrint()
            customers = self.__customerService.getAllCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressEnterToContinue()
            self.findCustomerMenu()

# Shows all deleted customers.
        elif action == '3':
            self.spaces()
            print(Colors.WHITE+"Path: Menu/Find_Customer/All_Deleted_Customers/\n"+Colors.END)
            self.allDeletedCustomerHeaderPrint()
            customers = self.__customerService.getAllDeletedCustomers()
            self.displayAllCustomersPrint(customers)
            action = self.pressEnterToContinue()
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
                self.pressEnterToContinue()
                self.findCustomerMenu()
            
# If the customer is found it prints found message.
            else:
                self.spaces()
                self.customerFound()
                self.displayCustomerHeaderPrint()
                print(Colors.WHITE+(str(customer)+Colors.END))
                self.afterDeletedCustomerIsFoundMenu(customer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.findCustomerMenu()

# After the customer is found the user can go back or reinstate the customer.
    def afterDeletedCustomerIsFoundMenu(self,customer):
        self.afterDeletedCustomerIsFoundPrint()
        action = self.chooseAction()
        if action == '0':
            self.findCustomerMenu()
        elif action == '1':
            self.reinstatingWarningMessageMenu(customer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.afterDeletedCustomerIsFoundMenu(customer)

    def reinstatingWarningMessageMenu(self,customer):
        self.spaces()
        self.reinstatingWarningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.restoringCustomer(customerNumber)
                self.spaces()
                print(Colors.GREEN+"Customer "+Colors.WHITE+f"'{customer.getName()}'"+Colors.GREEN+" has been reinstated."+Colors.END)  # Customer reinstated
                self.pressEnterToContinue()
                self.spaces()
                self.findCustomerMenu()
            elif action == '2':
                self.spaces()
                self.afterDeletedCustomerIsFoundMenu(customer)
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.reinstatingWarningMessageMenu(customer)

    def reinstatingWarningMessagePrint(self,customer):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Reinstate_Selected_Customer/"+Colors.END)
        print(Colors.GREEN + "\nSelected customer: " + Colors.END)
        self.displayCustomerHeaderPrint()
        print(Colors.WHITE+str(customer)+Colors.END)
        print(Colors.RED + "\nWarning: " + Colors.BLUE + "Are you sure you want to reinstate this customer?" + Colors.END)
        print(Colors.WHITE+"1. Yes, reinstate this customer")
        print("2. No, do not reinstate this customer"+Colors.END)
        
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
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.afterCustomerIsFoundMenu(customer)
    
            
# The menu for editing the customer information, Number stays the same
    def editCustomerInfo(self,customer):
        self.spaces()
        self.editCustomerInfoPrint()
        cs = CustomerService()
        action = self.chooseAction()
        self.spaces()
        name = customer.getName()
        age = customer.getAge()
        ssn = customer.getSsn()
        address = customer.getAddress()
        number = customer.getNumber()
        if action =='0':
            self.afterCustomerIsFoundMenu(customer)
# Edit customer name
        elif action =='1':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Name/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers name:"+Colors.END)
            name = cs.inputNameCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print(Colors.GREEN+"\nCustomer name has been changed from "\
            +Colors.WHITE+f"'{customer.getName()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{name}'"+Colors.END)
            self.pressEnterToContinue()
            self.editCustomerInfo(customer)
#Edit customer ssn
        elif action =='2':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Ssn/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers ssn:"+Colors.END)
            ssn,age = cs.inputSsnCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getSsn()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{ssn}'"+Colors.END)
            self.pressEnterToContinue()
            self.editCustomerInfo(customer)
#Edit customer address
        elif action =='3':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/Address/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers address:"+Colors.END)
            address = cs.inputAddressCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getAddress()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{address}'"+Colors.END)
            self.pressEnterToContinue()
            self.editCustomerInfo(customer)

#Edit all customer information
        elif action == '4':
            print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/All_Customer_Info/\n"+Colors.END)
            print(Colors.BLUE+"Editing customers name, ssn and address:"+Colors.END)
            cs = CustomerService()
            name = cs.inputNameCheck()
            ssn,age = cs.inputSsnCheck()
            address = cs.inputAddressCheck()
            newCustomer = Customer(name,age,ssn,address,number)
            cs.customerEdit(newCustomer)
# Name changed
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getName()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{name}'"+Colors.END)
# Ssn changed
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getSsn()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{ssn}'"+Colors.END)
# Address changed
            print(Colors.GREEN+"\nCustomer address has been changed from "\
            +Colors.WHITE+f"'{customer.getAddress()}'"+Colors.END+Colors.GREEN+" to "+Colors.WHITE+f"'{address}'"+Colors.END)
            self.pressEnterToContinue()
            self.editCustomerInfo(customer)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.editCustomerInfo(customer)

# Safety function that asks the user if he is certain that he wants to delete the selected customer.
    def warningMessageMenu(self,customer):
        self.spaces()
        self.warningMessagePrint(customer)
        action = self.chooseAction()
        while action:
            if action == '1':
                customerNumber = customer.getNumber()
                self.__customerService.deletingCustomer(customerNumber)
                self.spaces()
                print(Colors.RED+"Customer "+Colors.WHITE+f"'{customer.getName()}'"+Colors.RED+" has been deleted."+Colors.END) # Customer Deleted
                self.pressEnterToContinue()
                self.spaces()
                self.findCustomerMenu()
            elif action == '2':
                self.spaces()
                self.afterCustomerIsFoundMenu(customer)
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.warningMessageMenu(customer)

        
# Creates a customer, calls a function in the service class to validate the input.
    def createCustomer(self):
        self.spaces()
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
        print(Colors.BLUE+"{:24} {:15} {:15} {:20} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("-----------------------",\
        "---------------","---------------", "--------------------", "---------------"+Colors.END))
# Comes after the displayCustomerHeaderPrint, prints out all the customers.
    def displayAllCustomersPrint(self,customers):
        self.displayCustomerHeaderPrint()
        for customer in customers:
            print(Colors.WHITE+(str(customer))+Colors.END)
    
# Header which is printed when user is searching for a customer.
    def searchCustomerHeaderPrint(self):
        print(Colors.YELLOW + 
        "-------------------------------------------- Search for customer -------------------------------------------"
        + Colors.END)

# Prints the option to go back or reinstate the customer back into the main customer dir file.   VANTAR PATH
    def afterDeletedCustomerIsFoundPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Reinstate selected customer"+Colors.END)

# 
    def afterCustomerIsFoundPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Edit customer info")
        print("2. Delete customer"+Colors.END)

# Print function that displays users action choice.
    def editCustomerInfoPrint(self):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Edit_Customer/"+Colors.END)
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Edit customer name")
        print("2. Edit customer SSN")
        print("3. Edit customer address")
        print("4. Edit All customer information"+Colors.END)

# Prints when user chooses to delete a user.
    def warningMessagePrint(self,customer):
        print(Colors.WHITE+"Path: Menu/Find_Customer/Selected_Customer/Deleted_Selected_Customer/"+Colors.END)
        print(Colors.GREEN + "\nSelected customer: " + Colors.END)
        self.displayCustomerHeaderPrint()
        print(Colors.WHITE+(str(customer))+Colors.END)
        print(Colors.RED + "\nWarning: " + Colors.BLUE + "Are you sure you want to delete this customer?" + Colors.END)
        print(Colors.WHITE+"1. Yes, delete this customer")
        print("2. No, do not deleted this customer"+Colors.END)
    
    
    
    ''' -------------------- CAR FUNCTIONS -------------------- '''

    def editCarMenuPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Car Type")
        print("2. Make")
        print("3. Color")
        print("4. Passenger")
        print("5. Transmission"+Colors.END)

    def editCar(self):
        print(Colors.WHITE + "\nPath: Menu/Edit_Car" + Colors.END)
        print("-------------------------------------------------- Edit a Car --------------------------------------------------")
        licensePlate = self.__carService.checkLicenseplate(False)
        searchedCar = self.__carService.licensePlateCheck(licensePlate)
        self.printCarHeader()
        print(searchedCar)
        carType = searchedCar.getType()
        make = searchedCar.getMake()
        color = searchedCar.getColor()
        passengers = searchedCar.getPassengers()
        transmission = searchedCar.getTransmission()
        rentCost = searchedCar.getRentcost()
        status = searchedCar.getStatus()
        rentOutCar = searchedCar.getRentOutCar()
        self.editCarMenuPrint()
        action = self.chooseAction()
        if action == '0':
            self.spaces()
            self.editCar()
        elif action == '1':
            self.spaces()
            carTypeInput = self.__carService.checkCarType()
            rentCost, carType = self.getCarTypeVariables(carTypeInput)
        elif action == '2':
            self.spaces()
            make = input(Colors.WHITE+'Make (f.x. Toyota Yaris): '+Colors.END).capitalize()
        elif action == '3':
            self.spaces()
            color = input(Colors.WHITE+'Color: '+Colors.END).capitalize()
        elif action == '4':
            self.spaces()
            passengers = self.__carService.checkPassengers()
        elif action == '5':
            self.spaces()
            transmissionInput = self.__carService.checkTransmission()
            transmission = self.getTransmission(transmissionInput)
        rentOutCar, unusedValue = self.getTimeOfOrder()
        returnCar = rentOutCar
        editedCar = self.__carService.editCar(carType,make,licensePlate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        self.spaces()
        print(Colors.GREEN+"\nCar successfull edited!"+Colors.END)
        self.printCarHeader()
        print(Colors.WHITE+str(editedCar)+Colors.END)
        self.pressEnterToContinue()

    def showCarsByTypeMenu(self, typeAction,dateAvailable):
        while True:
            self.findCarTypeMenuPrint()
            action = self.chooseAction()
            if action == '0':
                self.mainMenu()
            elif action == '1':
                self.spaces()
                if typeAction == '1':
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/Compact/" + Colors.END)
                    self.allAvailableCars()
                elif typeAction == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/Compact/" + Colors.END)
                    self.allUnAvilableCars()
                action = 'compact'
            elif action == '2':
                self.spaces()
                if typeAction == '1':
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/Comfort/" + Colors.END)
                    self.allAvailableCars()
                elif typeAction == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/Comfort/" + Colors.END)
                    self.allUnAvilableCars()
                action = 'comfort'
            elif action == '3':
                self.spaces()
                if typeAction == '1':
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/CUV/" + Colors.END)
                    self.allAvailableCars()
                elif typeAction == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/CUV/" + Colors.END)
                    self.allUnAvilableCars()
                action = 'CUV'
            elif action == '4':
                self.spaces()
                if typeAction == '1':
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/Highland/" + Colors.END)
                    self.allAvailableCars()
                elif typeAction == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/Highland/" + Colors.END)
                    self.allUnAvilableCars()
                action = 'highland'
            elif action == '5':
                self.spaces()
                if typeAction == '1':
                    print(Colors.WHITE + "\nPath: Menu/Available_Cars/Luxury/" + Colors.END)
                    self.allAvailableCars()
                elif typeAction == '2':
                    print(Colors.WHITE + "\nPath: Menu/UnAvailable_Cars/Luxury/" + Colors.END)
                    self.allUnAvilableCars()
                action = 'luxury'
            elif action == '6':
                self.rentOutACar()
                return False
            else:
                self.invalidAction(action)
                self.pressEnterToContinue()
                self.showCarsByTypeMenu(typeAction,dateAvailable)
            cars = self.__carService.getCars(typeAction, action,dateAvailable)
            self.displayAllCarsPrint(cars)

    def createCar(self):
        self.spaces()
        self.createCarPrint()
        #car type
        carTypeInput = self.__carService.checkCarType()
        make = input(Colors.WHITE+"Make (f.x. Toyota Yaris): "+Colors.END).capitalize()
        color = input(Colors.WHITE+"Color: "+Colors.END).capitalize()
        passengers = self.__carService.checkPassengers()
        transmissionInput = self.__carService.checkTransmission()
        liecensePlate = self.__carService.checkLicenseplate()

        transmission = self.getTransmission(transmissionInput)
        rentCost, carType = self.getCarTypeVariables(carTypeInput)
        status = 'available'
        rentOutCar, unusedValue = self.getTimeOfOrder()
        returnCar = rentOutCar
        newCar = Car(carType,make,liecensePlate,color,passengers,transmission,rentCost,status,rentOutCar,returnCar)
        print(Colors.GREEN+"\nCar successfully created!"+Colors.END)
        self.printCarHeader()
        print(Colors.WHITE+(str(newCar)+Colors.END))
        return newCar


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
            print(Colors.WHITE+(str(car))+Colors.END)

    def findCarTypeMenuPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")
        print("6. Rent out a car"+Colors.END)

    def createCarPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"\n1. Select Compact")
        print("\n2. Select Comfort")
        print("\n3. Select CUV")
        print("\n4. Select Highland")
        print("\n5. Select Luxury"+Colors.END)
    
    def printCarHeader(self):
            LINE = '-'
            print(Colors.BLUE+"\n{:15} {:15} {:15} {:15} {:<15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
            'Color', 'Passengers','Transmission','Rent Cost'))
            print("{:-<15} {:-<15} {:-<15} {:-<15} {:-<15} {:-<15} {:-<15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE)+Colors.END)


    '''----------------------------------ORDER FUNCTIONS-----------------------------------------------'''
    def customerNotFoundMenu(self):
        self.customerNotFoundPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            self.createOrder()
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.customerNotFound()

    def rentOutToCustomerMenu(self):
        self.rentOutToCustomerPrintMenu()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            return
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.rentOutToCustomerMenu()

    def selectCarType(self):
        self.selectCarTypePrintMenu()
        action = self.__orderService.checkCarTypeSelection()
        rentCost, carType = self.getCarTypeVariables(action)
        return rentCost, carType

    def getCostOfOrder(self, rentOutCarTime, returnCarTime, rentCost):
        self.spaces()
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
            totalDaysRented = daysRentedCount.days
        else:
            totalDaysRented = daysRented.days        
        totalCost = int(totalDaysRented) * rentCost
        print(Colors.WHITE+"Price for {} days rental is {} ISK without VAT".format(totalDaysRented,totalCost)+Colors.END)
        return totalCost, totalDaysRented

    def addInsurance(self, cost):
        self.addInsurancePrint()
        action = self.chooseAction()
        self.spaces()
        insurance = 0
        if action == '1':
            totalCost = cost * 1.05
            insurance = cost * 0.05
        elif action == '2':
            totalCost = cost
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.addInsurance()
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
        self.spaces()
        self.areYouSurePrint()
        action = self.chooseAction()
        if action == '1':
            return True
        elif action == '2':
            return False
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.areYouSure()

    def finalStepOrder(self, order):
        self.finalStepOrderPrint()
        action = self.chooseAction()
        if action == '1':
            status = self.areYouSure()
            if status == True:
                self.__orderService.addOrder(order)
                self.spaces()
                print(Colors.GREEN+"Order complete!"+Colors.END)
            else:
                self.finalStepOrder(order)
        elif action == '2':
            status = self.areYouSure()
            if status == True:
                self.mainMenu()
            else:
                self.finalStepOrder(order)
        else:
            self.invalidAction(action)
            self.pressEnterToContinue()
            self.finalStepOrder(order)

    def createOrder(self):###WORKING ON THIS#####
        #Order Number
        self.searchCustomerForCarRentalHeaderPrint()
        searchTerm = self.searchTermInput()
        try:
            # find customer
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            ssn = customer.getSsn()
            print(Colors.WHITE + "\nPath: Menu/Creating_Car_Order/Select_Customer/\n" + Colors.END)
            self.customerFound()
            self.displayCustomerHeaderPrint()
            print(Colors.WHITE+(str(customer))+Colors.END)
            self.rentOutToCustomerMenu()
        except:
            print(Colors.WHITE + "\nPath: Menu/Creating_Car_Order/Customer_Not_Found/" + Colors.END)
            self.customerNotFound()
            self.customerNotFoundMenu()
        unusedValue, orderNumber = self.__orderService.getAllOrders()
        # Time for rental
        print(Colors.WHITE + "\nPath: Menu/Creating_Car_Order/Select_Customer/Input_Time_Of_Rental/\n" + Colors.END)
        try:
            #FAILS####
            rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
            self.pressEnterToContinue()
        except:
            self.mainMenu()
        # Choose car type
        print(Colors.WHITE + "\nPath: Menu/Creating_Car_Order/Select_Car_Type/" + Colors.END)
        rentCost, carType = self.selectCarType()
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        print(Colors.WHITE + "\nPath: Menu/Creating_Car_Order/Select_Car_Type/Add_Insurance/" + Colors.END)
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
        # Print out order
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, ssn)
        print(Colors.WHITE + "\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/" + Colors.END)
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        # Credit card for insurance
        creditCard = self.creditCardInfo()
        print(Colors.WHITE + "\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/Final_Step/" + Colors.END)
        self.finalStepOrder(order)
        #Choose payment
        print(Colors.WHITE + "\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/Final_Step/Payment/" + Colors.END)
        self.choosePayment(carCost, creditCard)
        # Print receipt
        print(Colors.WHITE + "\nPath: Menu/Create_Car_Order/Select_Car_Type/Order_Info/Final_Step/Payment/Receipt/" + Colors.END)
        self.showReceipt(order,insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)

    def displayAllOrders(self, orders):
        print("-------------------------------------------- List of All Orders --------------------------------------------")
        print(Colors.WHITE + "/Menu/Show_List_Of_All_Orders/"+ Colors.END)
        self.displayAllOrdersHeaderPrint()
        for order in orders:
            print(Colors.WHITE+str(order)+Colors.END)
            #menu? 

    def returnCarPrint(self):
        print(Colors.GREEN+"Car has successfully been returned"+Colors.END)

    def returnCarAdditionalPricePrint(self,price):
        print(Colors.WHITE+"\nAdditional price to be paid for late delivery: {} ISK\n".format(price)+Colors.END)
    
    def returnCarAdditionalPrice(self, returnTimeDifference, searchedCar):
        hourPrice = int(searchedCar.getRentcost())/24*1.25
        hours = returnTimeDifference.seconds / 60 / 60
        price = hours * hourPrice
        self.returnCarAdditionalPricePrint(int(price))
    
    def returnCar(self):
        licenseplate = self.__carService.checkLicenseplate(False)
        car = self.__carService.licensePlateCheck(licenseplate)
        self.printCarHeader()
        print(car)
        self.printReturnMenu()
        action = self.chooseAction()
        if action == '0':
            self.returnCar()
        elif action == '1':
            timeOfReturn = self.__orderService.checkValidDate()
            timeOfreturnInputTimeFormat = self.__orderService.createDate(timeOfReturn)
            searchedCar = self.__carService.returnCar(licenseplate, timeOfReturn)
            returnTimeDifference = timeOfreturnInputTimeFormat - searchedCar.getReturnCar()

            if returnTimeDifference.seconds > 0:
                self.returnCarAdditionalPrice(returnTimeDifference, searchedCar)
            self.returnCarPrint()
            self.pressEnterToContinue()

    def rentOutACar(self):
        print(Colors.WHITE + "\nPath: Menu/Rent_Out_Car" + Colors.END)
        print("-------------------------------------------------- Rent Out a Car --------------------------------------------------")
        licensePlate = self.__carService.checkLicenseplate(False)
        searchedCar = self.__carService.licensePlateCheck(licensePlate)
        # Info about the car to be rented
        carType = searchedCar.getType()
        make = searchedCar.getMake()
        color = searchedCar.getColor()
        passengers = searchedCar.getPassengers()
        transmission = searchedCar.getTransmission()
        rentCost = searchedCar.getRentcost()
        rentCost = int(rentCost)
        status = searchedCar.getStatus()
        rentOutCar = searchedCar.getRentOutCar() # string format
        returnCar = searchedCar.getReturnCar() # string format
        status = 'unavailable'
        # Prin out the car to be rented
        self.printCarHeader()
        print(Colors.WHITE+str(searchedCar)+Colors.END)
        self.pressEnterToContinue()
        self.spaces()
        #Search for customer for the rental
        self.searchCustomerForCarRentalHeaderPrint()
        searchTerm = self.searchTermInput()
        try:
            customer = self.__customerService.findCustomer(searchTerm)
            name = customer.getName()
            ssn = customer.getSsn()
            self.customerFound()
            self.displayCustomerHeaderPrint()
            print(Colors.WHITE+str(customer)+Colors.END)
            self.rentOutToCustomerMenu()
        except:
            self.customerNotFound()
            self.customerNotFoundMenu()
        # Get order number
        nothing, orderNumber = self.__orderService.getAllOrders()
        #Input rent out time and return
        self.spaces()
        rentOutCar, returnCar, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
        #calculate direct costs
        carCost, totalDaysRented = self.getCostOfOrder(rentOutCarTime, returnCarTime, rentCost)
        #Add insurance
        totalCost, insurance = self.addInsurance(carCost)
        #Time of order
        stringTimeOforder, timeOfOrder = self.getTimeOfOrder()
       # Print out order
        order = Order(orderNumber, name, carType, stringTimeOforder, rentOutCar, returnCar, totalCost, ssn)
        self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)  
        # Credit card for insurane
        creditCard = self.creditCardInfo()
        self.spaces()
        self.finalStepOrder(order)
        #Choose payment
        self.choosePayment(carCost, creditCard)
        # Print receipt
        self.showReceipt(order,insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)

    def choosePaymentPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"1. Credit card")
        print("2. Cash"+Colors.END)

    def choosePayment(self, carCost, creditCard):
        self.choosePaymentPrint()
        action = self.chooseAction()
        self.spaces()
        if action == '1':
            print(Colors.WHITE+"Payment will be charged on the following credit card {} for {} ISK".format(creditCard, carCost)+Colors.END)
            self.pressEnterToContinue()
            self.spaces()
        if action == '2':
            print(Colors.WHITE+"Payment to be paid: {} ISK".format(carCost)+Colors.END)
            self.pressEnterToContinue()
            self.spaces()
        


    def creditCardInfo(self):
        creditCard = self.__orderService.creditCardInfo()
        return creditCard

    def showReceiptPrint(self):
        print(Colors.BLUE+"Do you want to get a receipt ?")
        print(Colors.WHITE+"1. Yes")
        print("2. No"+Colors.END)

    def showReceipt(self, order,insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
        self.actionsPrint()
        self.showReceiptPrint()
        action = self.chooseAction()
        self.spaces()
        if action == '1':
            self.displayOrderInfo(order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder)
            self.pressEnterToContinue()
        elif action == '2':
            self.pressEnterToContinue()

    def editOrderInfoMenu(self):
        self.actionsPrint()
        self.lookUpOrderMenuPrint()
        action = self.chooseAction()
        if action == '0':
            self.mainMenu()
        elif action == '1':
            #get order info
            try:
                orderNumber, orderInfo = self.__orderService.checkOrderNumber()#check for illegitimacy##might be stuck in loop
                #prints order info
                #variables for rent cost
                originalRentOutCarTime = self.__orderService.createDate(orderInfo.getStartDate())
                originalReturnCarTime = self.__orderService.createDate(orderInfo.getEndDate())
                originalDaysRented = self.daysRented(originalRentOutCarTime, originalReturnCarTime)
                #NOT THE ORIGINAL PRICE AND 0.0
                originalPrice = orderInfo.getRentCost()
                ##NEEDS FIXING FOR CORRECT INFO IN DISPLAYORDERINFO###
                self.displayOrderInfo(orderInfo, 0, originalDaysRented, originalPrice, originalRentOutCarTime, originalReturnCarTime, orderInfo.getTimeOfOrder())#####
                self.editOrderMenuPrint()
            except:
                self.mainMenu()
                
            action = self.chooseAction()

            if action == '0':
                self.editOrderInfoMenu()
            
            elif action == '1':
                #gets beginning of rental time and 
                #edit rental time
                #MISSING RENTOUTTIME OG RENTOUTDATE
                rentOutDate, returnDate, rentOutCarTime, returnCarTime = self.__orderService.checkValidDate(True)
                #get type
                newDaysRented = self.daysRented(rentOutCarTime, returnCarTime)
                #get price
                newCostOfRental = int((int(originalPrice) / originalDaysRented) * newDaysRented)
                #new order
                newOrder = self.__orderService.editTimeOfRental(rentOutDate, returnDate, newCostOfRental, orderNumber)
                print(Colors.GREEN+"\nRental time updated"+Colors.END)
                self.displayAllOrdersHeaderPrint()
                print(Colors.GREEN+str(newOrder)+Colors.END)

            elif action == '2':
                #Change car type
                rentCost, carType = self.selectCarType()
                newCostOfRental = originalDaysRented * rentCost
                totalCost, insurance = self.addInsurance(newCostOfRental)
                newOrder = self.__orderService.editCarType(totalCost, carType, orderNumber)
                print(Colors.GREEN+"Car Type updated"+Colors.END)
                self.displayAllOrdersHeaderPrint()
                print(Colors.WHITE+str(newOrder)+Colors.END)
            
            elif action == '3':
                #Cancel order
                #flawed... prints out old car type
                confirmingCancellation = self.areYouSure()
                if confirmingCancellation == True:
                    deletedOrder = self.__orderService.cancelOrder(orderNumber)
                    print(Colors.RED+"\nOrder number: {} deleted".format(orderNumber)+Colors.END)
                    print(Colors.RED+"\nOrder number: "+Colors.WHITE,orderNumber,Colors.RED+"has been deleted"+Colors.END)
                    self.displayAllOrdersHeaderPrint()
                    print(Colors.WHITE+str(deletedOrder)+Colors.END)
                    self.pressEnterToContinue()

                else:
                    self.editOrderInfoMenu()

    def daysRented(self, rentOutCarTime, returnCarTime):
        daysRented = returnCarTime - rentOutCarTime
        if daysRented.seconds > 00:
            daysRentedCount = daysRented + timedelta(days = 1)
            totalDaysRented = daysRentedCount.days
        else:
            totalDaysRented = daysRented.days

        return int(totalDaysRented)


    def editOrderMenuPrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print(Colors.WHITE+"1. Edit rental time")
        print(Colors.WHITE+"2. Change car type")
        print(Colors.WHITE+"3. Cancel order")

    
    def lookUpOrderMenuPrint(self):
        print("--------------------------------------------Look Up an Order--------------------------------------------")
        print(Colors.WHITE+"0. Go back")
        print("1. Search for order"+Colors.END)


    

    '''--------------------------ORDER PRINT FUNCTIONS--------------------------'''
    def rentOutToCustomerPrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back to main menu")
        print("1. Select customer"+Colors.END)

    def customerNotFoundPrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back to main menu")
        print("1. Search again"+Colors.END)

    def selectCarTypePrintMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. <-- Go back")
        print("1. Compact")
        print("2. Comfort")
        print("3. CUV")
        print("4. Highland")
        print("5. Luxury"+Colors.END)

    def addInsurancePrint(self):
        self.actionsPrint()
        print(Colors.WHITE+"1. Add SCDW(Includes):\n\t{0}\n\t{1}\n\t{2}\n\t{3}".format("-Front window","-Sandstorm","-Chassis", "-Theft insurance"))
        print("2. No additional insurance"+Colors.END)

    def areYouSurePrint(self):
        print(Colors.BLUE+"\nAre you sure?")
        print(Colors.WHITE+"1. Yes")
        print("2. No, go back"+Colors.END)

    def finalStepOrderPrint(self):
        self.actionsPrint()
        print(Colors.GREEN+"1. Save and complete order")
        print(Colors.RED+"2. Cancel order"+Colors.END)

    def displayAllOrdersHeaderPrint(self):
        LINE = '---------------'
        print(Colors.BLUE+"\n{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:6}".format('Order number', 'Customer', 'ssn', 'Car Type',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:15} {:15} {:15} {:15} {:17} {:17} {:17} {:6}".format(LINE,LINE, LINE, LINE, LINE, LINE, LINE, LINE)+Colors.END)

    def displayOrderInfo(self,order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
# THIS LOOKS HORRIBLE, FIX LATER
        print(Colors.WHITE+"\n-------------------------------------------------- Order Info --------------------------------------------------\n")
        # print("Order Number: {}\n".format(order.getOrderNumber())+Colors.END)
        print(Colors.BLUE+"Order number: "+Colors.WHITE,str(order.getOrderNumber())+Colors.END)
        print(Colors.BLUE+"\n{:20} {:20}".format('Name','Ssn'))
        print("---------------------------------------------------"+Colors.END)
        print(Colors.WHITE+"{:20} {:20}".format(order.getCustomer(), order.getSsn())+Colors.END)
        print(Colors.BLUE+"\n{:20} {:20} {:20} {:20}".format('Car type','From','To','Date rented'))
        print("{:20} {:20} {:20} {:20}".format('-------------------','-------------------','-------------------','-------------------')+Colors.END)
        print(Colors.WHITE+"{:20} {:20} {:20} {:20}".format(order.getCarType(),str(rentOutCarTime),str(returnCarTime), str(timeOfOrder))+Colors.END)
        print(Colors.BLUE+"\nCost of"+Colors.WHITE,str(totalDaysRented),Colors.BLUE+"days without VAT: "+Colors.WHITE,str(carCost),"ISK"+Colors.END)
        if insurance != 0:
            print(Colors.BLUE+"Extra insurance: "+Colors.WHITE,str(insurance),"ISK"+Colors.END)
            # print("\nTotal cost of {} days without VAT: {} ISK".format(totalDaysRented, order.getRentCost()))
            print(Colors.BLUE+"\nTotal cost of"+Colors.WHITE,str(totalDaysRented),Colors.BLUE+"days without VAT: "+Colors.WHITE,str(order.getRentCost())," ISK")
    
    def displayAllOrdersHeaderPrint(self):
        LINE = '-'
        print(Colors.BLUE+"\n{:13} {:20} {:12} {:10} {:18} {:18} {:18} {:10}".format('Order number', 'Customer', 'SSN', 'Car Type',\
        'Time of order', 'Start of order','End of order','Rent cost'))
        print("{:-<13} {:-<20} {:-<12} {:-<10} {:-<18} {:-<18} {:-<18} {:-<12}".format(LINE,LINE, LINE, LINE, LINE, LINE, LINE, LINE)+Colors.END)

    def displayOrderInfo(self,order, insurance, totalDaysRented, carCost, rentOutCarTime, returnCarTime, timeOfOrder):
# THIS LOOKS HORRIBLE, FIX LATER
        LINE = '-'
        print(Colors.WHITE+"\n-------------------------------------------------- Order Info --------------------------------------------------\n")
        # print("Order Number: {}\n".format(order.getOrderNumber())+Colors.END)
        print(Colors.BLUE+"Order number: "+Colors.WHITE,str(order.getOrderNumber())+Colors.END)
        print(Colors.BLUE+"\n{:20} {:20}".format('Name','SSN'))
        print("{:-<32}".format(LINE)+Colors.END)
        print(Colors.WHITE+"{:20} {:20}".format(order.getCustomer(), order.getSsn())+Colors.END)
        print(Colors.BLUE+"\n{:10} {:20} {:20} {:20}".format('Car type','From','To','Date rented'))
        print("{:-<10} {:-<20} {:-<20} {:-<20}".format(LINE,LINE,LINE,LINE)+Colors.END)
        print(Colors.WHITE+"{:10} {:20} {:20} {:20}".format(order.getCarType(),str(rentOutCarTime),str(returnCarTime), str(timeOfOrder))+Colors.END)
        print(Colors.BLUE+"\nCost of"+Colors.WHITE,str(totalDaysRented),Colors.BLUE+"days without VAT: "+Colors.WHITE,str(carCost),"ISK"+Colors.END)
        if insurance != 0:
            print(Colors.BLUE+"Extra insurance: "+Colors.WHITE,str(insurance),"ISK"+Colors.END)
            # print("\nTotal cost of {} days without VAT: {} ISK".format(totalDaysRented, order.getRentCost()))
            print(Colors.BLUE+"\nTotal cost of"+Colors.WHITE,str(totalDaysRented),Colors.BLUE+"days without VAT: "+Colors.WHITE,str(order.getRentCost())," ISK")

    def searchCustomerForCarRentalHeaderPrint(self):
        print(Colors.BLUE+"--------------------- Find Customer for Car Rental ---------------------"+Colors.END)

    def printReturnMenu(self):
        print("-------------------------------------------------- Return a Car --------------------------------------------------")
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Return selected car"+Colors.END)
    ##NOT IN USE###
    def listofOrdersMenu(self):
        self.actionsPrint()
        print(Colors.WHITE+"0. Go back")
        print("1. Search for an order by order number"+Colors.END)