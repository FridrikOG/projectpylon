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
                cars = self.__carService.getCars(action)
                self.displayAllCarsPrint(cars)

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
                searchTerm = input("Input SSN or name to find: ")
                customer = self.__customerService.findCustomer(searchTerm)
                self.searchCustomerPrintHeader(customer)
                
            elif findCustomerAction == '2':
                customers = self.__customerService.getAllCustomers()
                self.displayAllCustomersPrint(customers)

    def createCustomer(self):
        print("-----------Creating customer account-----------")
        name = input('Step 1/3 - Enter name: ').strip()
        age = input('Step 2/3 - Enter age: ').strip()
        ssn = self.errorCheckingSsn()
        address = input('Step 3/3 Enter address: ').strip()
        number = self.countingCustomers()
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

    def displayAllCustomersPrint(self,customers):
        print("{:15} {:15} {:15} {:15} {:15}".format("Name", "Age", "SSN", "Address", "Number"))
        print("{:15} {:15} {:15} {:15} {:15}".format("---------------",\
        "---------------","---------------", "---------------", "---------------"))
        for customer in customers:
            print(customer)
    
    def searchCustomerPrintHeader(self,customer):
        print("--------------------------------------------Search for customer-------------------------------------------")
        print(customer)



    ''' -------------------- Car Functions -------------------- '''




    def createCar(self):
        print("\nSelect from Car Types:\n1. Compact\n2. Comfort\n3. CUV\
                \n4. Highland\n5. Luxury\n")
        while True:
            try:
                carTypeInput = int(input('Choose car type number:  '))
                if 0 < carTypeInput < 6:
                    break
                else:
                    print('Please choose from available types\n')
            except:
                print("Please only insert integer values\n")
        make = input('Make (f.x. Toyota Yaris): ').capitalize()
        color = input('Color: ').capitalize()
        while True:
            try:
                passengers = int(input('Passengers: '))
                break
            except:
                print("\nPlease only insert integer values\n")
        print("Transmission:\n1. Auto\n2. Manual\n")
        while True:
            try:
                transmissionInput = int(input('Choose: '))
                if 0 < transmissionInput < 3:
                    break
                else:
                    print('Please choose from available transmissions\n')
            except:
                print("Please only insert integer values\n")
        transmission = self.getTransmission(transmissionInput)
        while True:
            licenseplate = input('License plate (F.x. LL-L00): ').upper()
            if len(list(licenseplate)) == 6:
                break
            else:
                print("Not a valid license plate")

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

    def findRentCost(self,carTypeInput):
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
        print("\n{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
        'Color', 'Passengers','Transmission','Rent Cost'))
        print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))
