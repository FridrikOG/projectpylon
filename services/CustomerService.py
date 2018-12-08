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

    def getAllCustomers(self):
        return self.__customerRepo.getAllCustomers()

    def findCustomer(self, searchTerm):
        theFoundCustomer = self.__customerRepo.findCustomer(searchTerm)
        if theFoundCustomer == None:
            return None
        else:
            return theFoundCustomer
        
    def countingCustomers(self):
        return self.__customerRepo.countingCustomers()
    
    def countingDeletedCustomers(self):
        return self.__customerRepo.countingDeletedCustomers()
    

    def getSumOfAllCustomers(self):
        ADDINGONECUSTOMER = 1
        sumOfAllCustomers = len(self.countingDeletedCustomers()) + len(self.countingCustomers()) + ADDINGONECUSTOMER
        return sumOfAllCustomers

    
    def deletingCustomer(self,customerNumber):
        return self.__customerRepo.deletingCustomer(customerNumber)

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
                    self.inputNameCheck(messageDisplayed)
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
        while len(str(ssn)) != 10:
            try:
                ssn = int(input("Step 3/4 - Enter an SSN of 10 numbers: "))
            except ValueError:
                print("Please enter only 10 integers")
        return str(ssn)

# Input check for the address of the customer
    def inputAddressCheck(self):
        address = input("Step 4/4 - Enter address: ").capitalize()
        return address
