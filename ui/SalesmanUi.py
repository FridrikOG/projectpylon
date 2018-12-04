from services.CarService import CarService
from models.Car import Car

class SalesmanUi:

    def __init__(self):
        self.__car_service = CarService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("\nYou can do the following: ")
            print("1. Add a video")
            print("2. List all available cars")
            print("3. List all unavailable cars")
            print("press q to quit\n")

            action = input("Choose an option: ").lower()
            print("\n")

            if action == "1":
                title = input("Movie title: ")
                genre = input("Genre: ")
                length = input("Length in minutes: ")
                new_video = Video(title, genre, length)
                self.__video_service.add_video(new_video)

            elif action == "2" or action == "3":
                cars = self.__car_service.get_cars(action)
                print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format("Type", "Make", "License Plate",\
                "Color", "Passengers","Transmission","Rent Cost"))
                print("{:15} {:15} {:15} {:15} {:15} {:15} {:15}".format('---------------',\
                '---------------','---------------','---------------','---------------',\
                '---------------','---------------',))
                for x in cars:
                    print(x)
                    