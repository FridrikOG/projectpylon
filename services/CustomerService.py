from repositories.CustomerRepository import CustomerRepository
import string


class CustomerService:
    def __init__(self):
        self.__customerRepo = CustomerRepository()
        self.__CUSTFILE = './data/customers.csv'
        self.__CUSTDELFILE = './data/customersDeleted.csv'

    def addCustomer(self, customer):
        self.__customerRepo.addCustomer(customer,self.__CUSTFILE)
    
#This function returns a list of all customers
    def getAllCustomers(self):
        return self.__customerRepo.getAllCustomers(self.__CUSTFILE)
#This function returns a list of all deleted customers
    def getAllDeletedCustomers(self):
        return self.__customerRepo.getAllCustomers(self.__CUSTDELFILE)

    def findCustomer(self, searchTerm):
        theFoundCustomer = self.__customerRepo.findCustomer(searchTerm,self.__CUSTFILE)
        if theFoundCustomer == None:
            return None
        else:
            return theFoundCustomer
    def findDeletedCustomer(self, searchTerm):
        theFoundCustomer = self.__customerRepo.findCustomer(searchTerm, self.__CUSTDELFILE)
        if theFoundCustomer == None:
            return None
        else:
            return theFoundCustomer        
#Counts all the customers
    def countingCustomers(self):
        return self.__customerRepo.countingCustomers(self.__CUSTFILE)
#Counts all the deleted customers
    def countingDeletedCustomers(self):
        return self.__customerRepo.countingCustomers(self.__CUSTDELFILE)
#This function takes the sum of both deleted and current registered customers and returns a total to keep count.
    def getSumOfAllCustomers(self):
        ADDINGONECUSTOMER = 1
        sumOfAllCustomers = len(self.countingDeletedCustomers()) + len(self.countingCustomers()) + ADDINGONECUSTOMER
        return sumOfAllCustomers
    
    def deletingCustomer(self,customerNumber):
        return self.__customerRepo.removingCustomer(customerNumber,self.__CUSTDELFILE,self.__CUSTFILE)
    def restoringCustomer(self,customerNumber):
        return self.__customerRepo.removingCustomer(customerNumber,self.__CUSTFILE,self.__CUSTDELFILE)

    def customerEdit(self,newCustomer):
        self.__customerRepo.customerEdit(newCustomer,self.__CUSTFILE)
    
# Input check for the name of the customer
    def inputNameCheck(self):
        check = False
        newName = ''
        while not check:
            fullName = input('Step 1/4 - Enter name: ').strip().title().split()
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
                if booleanCheck == False:
                    print("SSN already exists!")
            except ValueError:
                print("Please enter only 10 integers")
        return str(ssn)

# Input check for the address of the customer
    def inputAddressCheck(self):
        address = input("Step 4/4 - Enter address: ").capitalize()
        return address
