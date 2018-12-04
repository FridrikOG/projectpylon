from repositories.CustomerRepository import CustomerRepository

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

    def getCustomers(self):
        return self.__customerRepo.getCustomers()

    def get_videos_by_genre(self, genre):
        pass