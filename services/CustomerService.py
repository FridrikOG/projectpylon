from repositories.CustomerRepository import CustomerRepository
from models.Colors import Colors
import string
from datetime import datetime, timedelta


class CustomerService:
    def __init__(self):
        self.__customerRepo = CustomerRepository()
        self.__CUSTFILE = './data/customers.csv'
        self.__CUSTDELFILE = './data/customersDeleted.csv'
        self.__ADDINGONECUSTOMER = 1


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
        
        sumOfAllCustomers = len(self.countingDeletedCustomers()) + len(self.countingCustomers()) + self.__ADDINGONECUSTOMER
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
            fullName = input(Colors.WHITE+"Step 1/3 - Enter name: "+Colors.END).strip().title().split()
            for name in fullName:
                if name not in string.punctuation and name.isalpha():
                    newName += name + ' '
                    check = True
                else:
                    check = False
        newName = newName.strip()
        return newName


# Input check for the age of the customer
    def inputAgeCheck(self,ssn):
        year = datetime.now().year
        ssn = str(ssn)
        ssn = ssn[4:6]
        ssn = int(ssn)
        year = str(year)
        year = year[2:4]
        year = int(year)
        if ssn >= year:
            year += 100
            ageOfCustomer = year - ssn
        else:
            ageOfCustomer = year - ssn
        return ageOfCustomer
                
    
# Input check for the ssn of the customer
# 

    def inputSsnCheck(self):
        ssn = ''
        booleanCheck = False
        while len(str(ssn)) != 10 or not booleanCheck:
            try:
                ssn = input("Step 2/3 - Enter an SSN of 10 numbers: ")
                age = self.inputAgeCheck(ssn)
                if age < 21:
                    print("Customer has to be above the age of 21")
                else:  
                    booleanCheck = self.__customerRepo.duplicateSsnCheck(str(ssn))
                    if booleanCheck == False:
                        print("SSN already exists!")
            except ValueError:
                print("Please enter only 10 integers")
        return str(ssn),str(age)


# Input check for the address of the customer

    def inputAddressCheck(self):
        address = input(Colors.WHITE+"Step 3/3 - Enter address: "+Colors.END).strip().capitalize()
        return address