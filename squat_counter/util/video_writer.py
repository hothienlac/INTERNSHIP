import cv2



class VideoWriter:
    
    def __init__(self, path, fps=30, dimention=(1920,1080)):
        print(dimention)
        print(fps)
        self.video = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'XVID'), fps, dimention, True)

    def add_frame(self, frame):
        self.video.write(frame)
    
    def save(self):
        self.video.release()