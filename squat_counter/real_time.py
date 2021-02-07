import os
import cv2
import numpy as np

from util.video_util import  read_video, get_dimention,get_frame_rate
from util.video_writer import VideoPlayer
from util.squat_counter import SquatCounter
from posenet.client import get_pose
from multi_threading.process_video import process_video
from posture_estimator.posture_estimator import PostureEstimator


squat_counter = SquatCounter()

dirname = os.path.dirname(__file__)
input = 0
output = os.path.join(dirname, 'data/xx-count-squat.mp4')

SIT = 'SIT'
MIDDLE = 'MIDDLE'
STAND = 'STAND'

model = PostureEstimator()




def decode(code):
    max_value_index = np.argmax(code)
    dictionary = [SIT, MIDDLE, STAND]
    
    return dictionary[max_value_index]



def process_frame(frame):
    pose = get_pose(frame)
    features = pose.get_features()

    posture = model.predict([features])
    posture = decode(posture[0])

    squat_counter.update(posture)

    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(frame, str(posture), (100,200), font, 5, (255, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(frame, str(squat_counter.count), (100,400), font, 5, (0, 255, 0), 5, cv2.LINE_AA)



def main():
    video = read_video(input)
    fps = get_frame_rate(input)
    if fps > 60:
        fps = 30
    dimention = get_dimention(input)
    video_player = VideoPlayer()
    
    process_video(process_frame, video, video_player)

    video_player.close()
    print('DONE')



if __name__ == '__main__':
    main()