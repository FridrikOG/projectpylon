from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []
        self.__ssnList = []
        self.__deletedCustomers = []

# fileDir = Filedirectory
 # Takes in fileDir and writes into the file information about the customer
    def addCustomer(self,customer,fileDir):
        with open(fileDir,'a',) as customerFile:
            name = customer.getName()
            age = customer.getAge()
            ssn = customer.getSsn()
            address = customer.getAddress()
            number = customer.getNumber()
            customerFile.write(f'{name},{age},{ssn},{address},{number}\n')

# Appends all the customers from 'fileDir' to a list then sends it back where it is printed out
    def getAllCustomers(self, fileDir):
        with open(fileDir, 'r') as customerFile:
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


# Search engine that can search in whatever directory required.
# Finds a customer in a dir when customerNumber or ssn is inputted
    def findCustomer(self, searchTerm,fileDir):
        with open(fileDir, 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    name = line['name']
                    age = line['age']
                    ssn = line['ssn']
                    address = line['address']
                    number = line['number']
                    newCustomer = Customer(name, age, ssn, address, number)
                    if searchTerm == number or searchTerm == ssn:
                        return newCustomer

# Counts how many ssn in fileDir.
    # such that a customer recieves his own customerNumber in the system.
    def countingCustomers(self, fileDir):
        with open(fileDir, 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__ssnList = []
            for line in csvReader:
                ssn = line['ssn']
                self.__ssnList.append(ssn)
            return self.__ssnList
    
# Iterates through the file and appends the unwanted customerNumber or ssn
    # to customersDeleted.csv
    def removingCustomer(self,customerNumber,dataAdd, dataRemove):
        with open(dataRemove, 'r') as customerFile:
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

            self.emptyingFile(dataRemove)
            self.addingCustomers(self.__customers,dataRemove)
            self.addingDeletedCustomers(self.__deletedCustomers,dataAdd)

# Clears the file and adds the headers name,age,ssn,address,number and a new line.
    def emptyingFile(self,dataRemove):
        with open(dataRemove, 'w') as customerFile:
            customerFile.write('name,age,ssn,address,number\n')
    def addingCustomers(self,listOfCustomers,dataRemove):
        with open(dataRemove, 'a') as customerFile:
            for customer in listOfCustomers:
                customerFile.write(f'{customer}\n')
    def addingDeletedCustomers(self,listOfCustomers,dataAdd):
        with open(dataAdd, 'a') as customerFile:
            for customer in listOfCustomers:
                customerFile.write(f'{customer}\n')

# Edits the customers information, with help from the previous functions.
    def customerEdit(self,newCustomer,fileDir):
        with open(fileDir, 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            customerNumber = newCustomer.getNumber()
            self.__customers = []
            for line in csvReader:
                name = line['name']
                age = line['age']
                ssn = line['ssn']
                address = line['address']
                number = line['number']
                if number != customerNumber and number < customerNumber:
                    self.__customers.append(name+','+age+','+ssn+','+address+','+number)
                elif number == customerNumber:
                    newName = newCustomer.getName()
                    newage = newCustomer.getAge()
                    newSsn = newCustomer.getSsn()
                    newAddress = newCustomer.getAddress()
                    self.__customers.append(newName+','+newage+','+newSsn+','+newAddress+','+customerNumber)
                else:
                    self.__customers.append(name+','+age+','+ssn+','+address+','+number)
            self.emptyingFile(fileDir)
            self.addingCustomers(self.__customers,fileDir)


# Checks if the ssn already exists in the system when creating a new customer or
    # when editing a customer.
    def duplicateSsnCheck(self,newSsn):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    ssn = line['ssn']
                    if newSsn == ssn:
                        return False
            return True