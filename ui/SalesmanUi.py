from services.CarService import CarService
from models.Car import Car

class SalesmanUi:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("\nYou can do the following: ")
            print("1. List all available cars")
            print("2. List all unavailable cars")
            print("3. Register customer.")
            print("4. Create car reservation.")
            print("5. Find a customer.")
            print("6. Look up an order.")
            print("7. Show list of orders.")
            print("8. Return a car.")
            print("9. Edit order.")
            print("press q to quit\n")

            action = input("Choose an option: ").lower()
            print("\n")

            if action == "1" or action == "2":
                cars = self.__car_service.get_cars(action)
                print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format("Type", "Make", "License Plate",\
                "Color", "Passengers","Transmission","Rent Cost"))
                print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format('---------------',\
                '---------------','---------------','---------------','---------------',\
                '---------------','---------------',))
                for x in cars:
                    print(x)
                    