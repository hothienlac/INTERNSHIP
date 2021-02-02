import cv2
from tqdm import tqdm

from util.video_util import read_video

def main():
    file_prefix = 'full'
    video_path = 'C:\\Users\\hothi\\Documents\\CODE\\INTERNSHIP\\squat_counter\\data\\full.mp4'
    out_path = 'C:\\Users\\hothi\\Documents\\CODE\\INTERNSHIP\\squat_counter\\data\\khoi\\full\\'
    video = read_video(video_path)
    count = 0

    for frame in tqdm(video):
        cv2.imwrite(f'{out_path}{file_prefix}_{count}.jpg', frame)
        count += 1


if __name__ == "__main__":
    main()