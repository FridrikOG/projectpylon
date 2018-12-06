from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer


class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()

    def mainMenu(self):
        action = ''
        while action != 'q':
            self.mainMenuPrint()
            action = input('Action: ')

            if action == '1' or action == '2':
                typeAction = ''
                cars = self.__carService.getCars(action, typeAction)
                self.displayAllCarsPrint(cars)
                self.showCarsByTypeMenu(action)


            elif action == '3':
                name,age,ssn,address,number = self.createCustomer()
                newCustomer = Customer(name,age,ssn,address,number)
                self.__customerService.addCustomer(newCustomer)

            elif action == '5':
                self.findCustomerMenuPrint()
                self.findCustomerMenu()

            elif action == '10':
                carType,make,licenseplate,color,passengers,transmission,rentCost,status = self.createCar()
                newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status)
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




    ''' -------------------- Customer Functions -------------------- '''

    def findCustomerMenu(self):
            findCustomerAction = input('Choose action: ')
            if findCustomerAction == '0':
                self.mainMenu()
            elif findCustomerAction == '1':
                self.searchCustomerPrintHeader()
                searchTerm = input("Input SSN or name to find: ")
                customer = self.__customerService.findCustomer(searchTerm)
                self.displayCustomerHeaderPrint()
                
            elif findCustomerAction == '2':
                customers = self.__customerService.getAllCustomers()
                self.displayAllCustomersPrint(customers)

    def createCustomer(self):
        print("-----------Creating customer account-----------")
        cs = CustomerService()
        name = cs.inputNameCheck()
        age = cs.inputAgeCheck()
        ssn = cs.inputSsnCheck()
        address = cs.inputAddressCheck()
        number = cs.countingCustomers()
        number += 1
        return name,age,ssn, address, number

    def errorCheckingSsn(self):
        ssn = ''
        while len(str(ssn)) != 10:
            try:
                ssn = int(input("Step 3/5 - Enter an SSN of 10 numbers: "))
            except ValueError:
                print("Please enter only 10 integers")
        return ssn

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
    
    
    def searchCustomerPrintHeader(self):
        print("--------------------------------------------Search for customer-------------------------------------------")


    
    
    
    ''' -------------------- Car Functions -------------------- '''

    def findCarTypeMenuPrint(self):
        print("0. <-- Go back")
        print("1. Show only Compact")
        print("2. Show only Comfort")
        print("3. Show only CUV")
        print("4. Show only Highland")
        print("5. Show only Luxury")

    def showCarsByTypeMenu(self, action):
        while True:
            self.findCarTypeMenuPrint()
            typeAction = input('Choose action: ')
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
            cars = self.__carService.getCars(action, typeAction)
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
        newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status)
        print("\nCar successfully created!")
        self.printCarHeader()
        print(newCar)
        return carType,make,licenseplate,color,passengers,transmission,rentCost,status

    def getTransmission(self, transmissionInput):
        if transmissionInput == 1:
            transmission = 'Auto'
        else:
            transmission = 'Manual'
        return transmission

        rentCost, carType = self.findRentCost(carTypeInput)
        status = 'available'
        newCar = Car(carType,make,licenseplate,color,passengers,transmission,rentCost,status)
        print("\nCar successfully created!")
        self.printCarHeader()
        print(newCar)
        return carType,make,licenseplate,color,passengers,transmission,rentCost,status

    def getTransmission(self, transmissionInput):
        if transmissionInput == 1:
            transmission = 'Auto'
        else:
            transmission = 'Manual'
        return transmission

    def getCarTypeVariables(self,carTypeInput):
        if carTypeInput == 1:
            carType = 'Compact'
            rentCost = 14000
        if carTypeInput == 2:
            carType = 'Comfort'
            rentCost = 20000
        if carTypeInput == 3:
            carType = 'CUV'
            rentCost = 25000
        if carTypeInput == 4:
            carType = 'Highland'
            rentCost = 30000
        if carTypeInput == 5:
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
