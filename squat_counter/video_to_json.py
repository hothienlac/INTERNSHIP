import argparse
import json
import os

from tqdm import tqdm
import __constants__    as constants
from __video_util__ import VideoUtil

from posenet.posenet_client import PosenetClient


def main(args):
    posenet_client = PosenetClient(constants.POSENET_SERVER)

    dirname = os.path.dirname(__file__)
    
    video_input = args.video
    if not video_input:
        video_input = './data/a.mp4'
    video_input = os.path.join(dirname, video_input)
    video = VideoUtil.read_video(video_input)

    output = args.output
    if not output:
        output = './Squat_Video_.json'
    output = os.path.join(dirname, output)

    progress_bar = tqdm()

    data = []
    for frame in video:
        data.append([posenet_client.get_json(frame)])
        progress_bar.update()
    
    progress_bar.close()
    
    with open(output, 'w') as file:
        json.dump(
            {
                'data': data
            },
            file,
        )



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--video',
        type=str,
        help='Path to video.',
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        help='Path to OutPut.',
    )
    args = parser.parse_args()
    main(args)
