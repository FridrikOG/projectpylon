from repositories.VideoRepository import VideoRepository

class VideoService:
    def __init__(self):
        self.__video_repo = VideoRepository()

    def add_video(self, video):
        if self.is_valid_video(video):
            self.__video_repo.add_video(video)
    
    def is_valid_video(self, video):
        #here should be some code to 
        #validate the video
        return True

    def get_videos(self):
        return self.__video_repo.get_videos()

    def get_videos_by_genre(self, genre):
        pass