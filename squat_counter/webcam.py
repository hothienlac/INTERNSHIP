# import the opencv library 
import cv2 
from tqdm import tqdm

x = tqdm()
  
class ScreenOutput:
    def __init__(self) -> None:
        pass

    def add_frame(self, frame):
        x.update()
        cv2.imshow('frame', frame)


s = ScreenOutput()
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True):       
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    s.add_frame(frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 