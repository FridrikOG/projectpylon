from repositories.CarRepository import CarRepository

class CarService:
    def __init__(self):
        self.__car_repo = CarRepository()

    def add_video(self, video):
        if self.is_valid_video(video):
            self.__video_repo.add_video(video)
    
    def is_valid_video(self, video):
        #here should be some code to 
        #validate the video
        return True

    def get_cars(self, action):
        return self.__car_repo.get_cars(action)

    def get_videos_by_genre(self, genre):
        pass