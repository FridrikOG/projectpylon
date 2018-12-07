from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []
        self.__setCustomers = set()
        self.__ssnList = []
        self.__deletedCustomers = []

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
        return self.__customers

    def findCustomer(self, searchTerm):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    name = line['name']
                    age = line['age']
                    ssn = line['ssn']
                    address = line['address']
                    number = line['number']
                    newCustomer = Customer(name, age, ssn, address, number)
                    if searchTerm == number or searchTerm == ssn:
                        return newCustomer, name, ssn

    def countingCustomers(self):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__ssnList = []
            for line in csvReader:
                ssn = line['ssn']
                self.__ssnList.append(ssn)
            return self.__ssnList

    def countingDeletedCustomers(self):
        with open('./data/customerDeleted.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__ssnList = []
            for line in csvReader:
                ssn = line['ssn']
                self.__ssnList.append(ssn)
            return self.__ssnList    
    
    def deletingCustomer(self,customerNumber):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__customers = []
            self.__deletedCustomers = []
            for line in csvReader:
                name = line['name']
                age = line['age']
                ssn = line['ssn']
                address = line['address']
                number = line['number']
                if number != customerNumber:
                    self.__customers.append(name+','+age+','+ssn+','+address+','+number)
                else:
                    self.__deletedCustomers.append(name+','+age+','+ssn+','+address+','+number)

            self.emptyingFile()
            self.addingCustomers(self.__customers)
            self.addingDeletedCustomers(self.__deletedCustomers)

    def emptyingFile(self):
        with open('./data/customers.csv', 'w') as customerFile:
            customerFile.write('name,age,ssn,address,number\n')
    def addingCustomers(self,listOfCustomers):
        with open('./data/customers.csv', 'a') as customerFile:
            for customer in listOfCustomers:
                customerFile.write(f'{customer}\n')
    def addingDeletedCustomers(self,listOfCustomers):
        with open('./data/customerDeleted.csv', 'a') as customerFile:
            for customer in listOfCustomers:
                customerFile.write(f'{customer}\n')
