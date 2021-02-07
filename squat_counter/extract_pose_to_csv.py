import os
from tqdm import tqdm
import pandas as pd

from util.read_all_images_in_folder import read_all_images_in_folder
from posenet.client import get_pose

from multi_threading.parallel_runner import ParallelRunner
from multi_threading.jobs_generator import job_generator

dirname = os.path.dirname(__file__)
sit = os.path.join(dirname, 'data/combined/sit')
middle = os.path.join(dirname, 'data/combined/middle')
stand =  os.path.join(dirname, 'data/combined/stand')
output = os.path.join(dirname, 'data/combined/data.csv')


progress_bar = tqdm()


COLUMN_NAMES = [
    'position',
    'leftShoulder_x',
    'rightShoulder_x',
    'leftHip_x',
    'rightHip_x',
    'leftKnee_x',
    'rightKnee_x',
    'leftAnkle_x',
    'rightAnkle_x',
    'leftShoulder_y',
    'rightShoulder_y',
    'leftHip_y',
    'rightHip_y',
    'leftKnee_y',
    'rightKnee_y',
    'leftAnkle_y',
    'rightAnkle_y',
    'leftHipAngle',
    'rightHipAngle',
    'leftKneeAngle',
    'rightKneeAngle',
]


SIT = 0
MIDDLE = 1
STAND = 2
NUMBER_OF_FEATURES = 20
NUMBER_OF_WORKERS = 12
QUEUE_SIZE = 24


def add_one_row(data_frame, image, position):
    pose = get_pose(image)
    features = pose.get_features()
    features.insert(0, position)
    
    data_frame.loc[len(data_frame)] = features

    progress_bar.update()


def process_image(data_frame, position):
    return lambda images: add_one_row(data_frame, images, position)


def add_data(data_frame, images, position):
    jobs = job_generator(process_image(data_frame, position), images)
    parallel_runner = ParallelRunner(NUMBER_OF_WORKERS, QUEUE_SIZE)
    parallel_runner.start(jobs)
    
    return data_frame



def main():
    data_frame = pd.DataFrame(columns = COLUMN_NAMES)

    sit_images = read_all_images_in_folder(sit)
    middle_images = read_all_images_in_folder(middle)
    stand_images = read_all_images_in_folder(stand)

    add_data(data_frame, sit_images, SIT)
    add_data(data_frame, middle_images, MIDDLE)
    add_data(data_frame, stand_images, STAND)

    data_frame.to_csv(output, index=False, encoding='utf-8')

    progress_bar.close()


if __name__ == '__main__':
    main()
