from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []
        self.__setCustomers = set()
        self.__ssnList = []

    def addCustomer(self,customer):
        with open('./data/customers.csv','a',) as customerFile:
            name = customer.getName()
            age = customer.getAge()
            ssn = customer.getSsn()
            address = customer.getAddress()
            number = customer.getNumber()
            customerFile.write(f'{name},{age},{ssn},{address},{number}\n')

    def getAllCustomers(self):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__customers = []
            for line in csvReader:
                    name = line['name']
                    age = line['age']
                    ssn = line['ssn']
                    address = line['address']
                    number = line['number']
                    newCustomer = Customer(name, age, ssn, address, number)
                    self.__customers.append(newCustomer)

                    # if ssn not in self.__ssnCustomers:
                    #     newCustomer = name +'   '+ age+'    ' + ssn
                    #     self.__ssnCustomers.add(newCustomer)   
        return self.__customers

    def findCustomer(self, searchTerm):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__customers = []
            for line in csvReader:
                    name = line['name']
                    age = line['age']
                    ssn = line['ssn']
                    address = line['address']
                    number = line['number']
                    newCustomer = Customer(name, age, ssn, address, number)
                    if searchTerm == number:
                        print(newCustomer)
                    elif searchTerm == ssn:
                        print(newCustomer)
                    else:
                        print("Nothing found")

    def countingCustomers(self):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__ssnList = []
            for line in csvReader:
                ssn = line['ssn']
                self.__ssnList.append(ssn)
            return self.__ssnList



