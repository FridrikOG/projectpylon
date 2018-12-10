from repositories.CustomerRepository import CustomerRepository
import string


class CustomerService:
    def __init__(self):
        self.__customerRepo = CustomerRepository()

    def addCustomer(self, customer):
        if self.isValidCustomer(customer):
            self.__customerRepo.addCustomer(customer)
    
    def isValidCustomer(self, customer):
        #here should be some code to 
        #validate the video
        return True
#This function returns a list of all customers
    def getAllCustomers(self):
        dataPosition = './data/customers.csv'
        return self.__customerRepo.getAllCustomers(dataPosition)
#This function returns a list of all deleted customers
    def getAllDeletedCustomers(self):
        dataPosition = './data/customersDeleted.csv'
        return self.__customerRepo.getAllCustomers(dataPosition)

    def findCustomer(self, searchTerm):
        dataPosition = './data/customers.csv'
        theFoundCustomer = self.__customerRepo.findCustomer(searchTerm,dataPosition)
        if theFoundCustomer == None:
            return None
        else:
            return theFoundCustomer
    def findDeletedCustomer(self, searchTerm):
        dataPosition = './data/customersDeleted.csv'
        theFoundCustomer = self.__customerRepo.findCustomer(searchTerm, dataPosition)
        if theFoundCustomer == None:
            return None
        else:
            return theFoundCustomer        
#Counts all the customers
    def countingCustomers(self):
        dataPosition = './data/customers.csv'
        return self.__customerRepo.countingCustomers(dataPosition)
#Counts all the deleted customers
    def countingDeletedCustomers(self):
        dataPosition = './data/customersDeleted.csv'
        return self.__customerRepo.countingCustomers(dataPosition)
#This function takes the sum of both deleted and current registered customers and returns a total to keep count.
    def getSumOfAllCustomers(self):
        ADDINGONECUSTOMER = 1
        sumOfAllCustomers = len(self.countingDeletedCustomers()) + len(self.countingCustomers()) + ADDINGONECUSTOMER
        return sumOfAllCustomers
    
    def deletingCustomer(self,customerNumber):
        dataAdd = './data/customersDeleted.csv'
        dataRemove = './data/customers.csv'
        return self.__customerRepo.removingCustomer(customerNumber,dataAdd,dataRemove)
    def restoringCustomer(self,customerNumber):
        dataAdd = './data/customers.csv'
        dataRemove = './data/customersDeleted.csv'
        return self.__customerRepo.removingCustomer(customerNumber,dataAdd,dataRemove)

    def customerEdit(self,newCustomer):
        self.__customerRepo.customerEdit(newCustomer)
    
# Input check for the name of the customer
    def inputNameCheck(self):
        check = False
        newName = ''
        while not check:
            fullName = input(' - Enter name: ')
            fullName = fullName.strip().title().split()
            for name in fullName:
                if name not in string.punctuation and name.isalpha():
                    newName += name + ' '
                else:
                    print("Invalid name")
                    self.inputNameCheck()
            check = True
        newName = newName.strip()
        return newName

# Input check for the age of the customer
    def inputAgeCheck(self):
        age = -1
        while age < 18 or age > 80:
            try:
                age = int(input("Step 2/4 - Enter the age of the customer: "))
            except:
                print("Age has to be a number between 18 and 80 ")
        return str(age)
    
# Input check for the ssn of the customer
    def inputSsnCheck(self):
        ssn = ''
        booleanCheck = False
        while len(str(ssn)) != 10 or not booleanCheck:
            try:
                ssn = int(input("Step 3/4 - Enter an SSN of 10 numbers: "))
                booleanCheck = self.__customerRepo.duplicateSsnCheck(str(ssn))
            except ValueError:
                print("Please enter only 10 integers")
        return str(ssn)

# Input check for the address of the customer
    def inputAddressCheck(self):
        address = input("Step 4/4 - Enter address: ").capitalize()
        return address
