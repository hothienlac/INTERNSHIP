import os

from util.video_util import  read_video, get_dimention,get_frame_rate
from util.video_writer import VideoWriter
from util.draw_skeleton import draw_skeleton
from posenet.client import get_pose
from multi_threading.process_video import process_video



dirname = os.path.dirname(__file__)
input = os.path.join(dirname, 'data/x.mp4')
output = os.path.join(dirname, 'data/x-with-skeleton.mp4')



def process_frame(frame):
    pose = get_pose(frame)
    draw_skeleton(frame, pose)


def main():
    video = read_video(input)
    fps = get_frame_rate(input)
    dimention = get_dimention(input)
    video_writer = VideoWriter(output, fps, dimention)
    
    process_video(process_frame, video, video_writer)

    video_writer.save()
    print('DONE')


if __name__ == '__main__':
    main()