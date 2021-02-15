import os
import cv2
import numpy as np

from util.video_util import  read_video, get_dimention,get_frame_rate
from util.video_writer import VideoWriter
from util.squat_counter import SquatCounter
from posenet.client import get_pose
from multi_threading.process_video import process_video
from posture_estimator.posture_estimator_random_forest import PostureEstimator
from util.draw_skeleton import draw_skeleton

dirname = os.path.dirname(__file__)
input = os.path.join(dirname, 'data/4.webm')
output = os.path.join(dirname, 'data/4-count-squat.mp4')

SIT = 'SIT'
MIDDLE = 'MIDDLE'
STAND = 'STAND'


model = PostureEstimator()


squat_counter = SquatCounter()



def decode(code):
    dictionary = [SIT, MIDDLE, STAND]
    
    return dictionary[int(code)]



class EMA:
    def __init__(self):
        self.EMA = 0
        self.ALPHA = 0.05
        self.PREVIOUS_NOSE = -1
    
    def update(self, nose, back_length):
        if self.PREVIOUS_NOSE == -1:
            self.PREVIOUS_NOSE = nose
        
        velocity = (nose - self.PREVIOUS_NOSE) / back_length
        self.EMA = self.EMA*(1-self.ALPHA) + velocity*self.ALPHA
        
        self.PREVIOUS_NOSE = nose



def process_frame(frame, ema):
    pose = get_pose(frame)


    features = pose.get_features()

    posture = model.predict([features])
    posture = decode(posture[0])

    back_length = pose.get_back_length()
    ema.update(pose.nose.get('y'), back_length)

    squat_counter.update(posture, ema.EMA)

    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(frame, str(posture), (100,200), font, 5, (255, 0, 0), 5, cv2.LINE_AA)
    cv2.putText(frame, str(int(ema.EMA*1000)), (100,400), font, 5, (0, 255, 0), 5, cv2.LINE_AA)
    cv2.putText(frame, str(squat_counter.count), (100,600), font, 5, (0, 255, 0), 5, cv2.LINE_AA)

    frame = cv2.line(frame, (1000, 360+int(ema.EMA*2000)), (1000, 360), (0, 0, 255), 20)

    draw_skeleton(frame, pose)


def process_frame_factory(ema):
    return lambda frame: process_frame(frame, ema)


def main():
    video = read_video(input)
    fps = get_frame_rate(input)
    if fps > 60:
        fps = 30
    dimention = get_dimention(input)
    video_writer = VideoWriter(output, fps, dimention)
    
    ema = EMA()
    process_video(process_frame_factory(ema), video, video_writer, in_order=True)

    video_writer.save()
    print('DONE')



if __name__ == '__main__':
    main()
