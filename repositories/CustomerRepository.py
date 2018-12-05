from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []

    def addCustomer(self,customer):
        with open('./data/customers.csv','a',) as customerFile:
            name = customer.getName()
            age = customer.getAge()
            ssn = customer.getSsn()
            customerFile.write(f'{name},{age},{ssn}\n')

    def getAllCustomers(self):
        with open('./data/customers.csv', 'r') as customerFile:
            csv_reader = csv.DictReader(customerFile)
            for line in csv_reader:
                name = line['name']
                age = line['age']
                ssn = line['ssn']
                newCustomer = Customer(name,age,ssn)
                self.__customers.append(newCustomer)     
        return self.__customers