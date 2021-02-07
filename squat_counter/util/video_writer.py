import cv2



class VideoWriter:
    
    def __init__(self, path, fps=30, dimention=(1920,1080)):
        print(dimention)
        print(fps)
        self.video = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'x264'), fps, dimention, True)

    def add_frame(self, frame):
        self.video.write(frame)
    
    def save(self):
        self.video.release()



class VideoPlayer:

    def __init__(self):
        pass


    def add_frame(self, frame):
        cv2.imshow('Video', frame)
        cv2.waitKey(1)


    def close(self):
        cv2.destroyAllWindows()