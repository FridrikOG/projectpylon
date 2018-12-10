from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []
        self.__setCustomers = set()
        self.__ssnList = []
        self.__deletedCustomers = []

    def addCustomer(self,customer,customerData):
        with open(customerData,'a',) as customerFile:
            name = customer.getName()
            age = customer.getAge()
            ssn = customer.getSsn()
            address = customer.getAddress()
            number = customer.getNumber()
            customerFile.write(f'{name},{age},{ssn},{address},{number}\n')

    def getAllCustomers(self, customerData):
        with open(customerData, 'r') as customerFile:
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

    def findCustomer(self, searchTerm,customerData):
        with open(customerData, 'r') as customerFile:
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

    def countingCustomers(self, customerData):
        with open(customerData, 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            self.__ssnList = []
            for line in csvReader:
                ssn = line['ssn']
                self.__ssnList.append(ssn)
            return self.__ssnList
    
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

   # ''' -------------------- Customer editing functions -------------------- '''

    def customerEdit(self,newCustomer,customerData):
        with open(customerData, 'r') as customerFile:
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
            self.emptyingFile(customerData)
            self.addingCustomers(self.__customers,customerData)


   # ''' -------------------- Checking data input -------------------- '''
    def duplicateSsnCheck(self,newSsn):
        with open('./data/customers.csv', 'r') as customerFile:
            csvReader = csv.DictReader(customerFile)
            for line in csvReader:
                    ssn = line['ssn']
                    if newSsn == ssn:
                        return False
            return True




        



        






