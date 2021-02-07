# Return a Generator

import cv2


def read_video(path):
    vidcap = cv2.VideoCapture(path)
    count = 0
    
    while(vidcap.isOpened()):
        ret, frame = vidcap.read()
        if ret == False:
            break
        count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        
        yield frame

    vidcap.release()


def get_frame_rate(path):
    video = cv2.VideoCapture(path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()

    return fps


def get_dimention(path):
    video = cv2.VideoCapture(path)
    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    video.release()

    return (int(width), int(height))