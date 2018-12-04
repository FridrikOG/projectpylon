from models.Customer import Customer
import csv

class CustomerRepository:
    def __init__(self):
        self.__customers = []

    def addCustomer(self,customer):
        with open('./data/customers.csv','a',) as customerFile:
            writer = csv.writer(customerFile)
            name = customer.getName()
            age = customer.getAge()
            ssn = customer.getSsn()
            customerFile.write(f'{name},{age},{ssn}\n')