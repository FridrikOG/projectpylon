from services.CarService import CarService
from models.Car import Car
from services.CustomerService import CustomerService
from models.Customer import Customer


class SalesmanUi:

    def __init__(self):
        self.__carService = CarService()
        self.__customerService = CustomerService()

    def mainMenu(self):

        action = True
        while action:
            mainMenuPrint()

            action = input('Choose an option: ').lower()
            print()
            
            if action == '1' or action == '2':
                LINE = '---------------'
                cars = self.__carService.getCars(action)
                print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format('Type', 'Make', 'License Plate',\
                'Color', 'Passengers','Transmission','Rent Cost'))
                print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format(LINE, LINE, LINE, LINE, LINE, LINE, LINE))
                for x in cars:
                    print(x)
            
            elif action == '3':
                name,age,ssn = createCustomer()
                newCustomer = Customer(name,age,ssn)
                self.__customerService.addCustomer(newCustomer)





def createCustomer():
    name = input('Enter name: ')
    age = input('Enter age: ')
    ssn = input('Enter Social-security-nr: ')
    return name,age,ssn
        

def mainMenuPrint():
    print("\nYou can do the following: ")
    print("1. List all available cars")
    print("2. List all unavailable cars")
    print("3. Register customer.")
    print("4. Create car reservation.")
    print("5. Find a customer.")
    print("6. Look up an order.")
    print("7. Show list of orders.")
    print("8. Return a car.")
    print("9. Edit order.")
    print("press q to quit\n")
            