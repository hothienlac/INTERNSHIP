import os
import cv2
import pandas as pd
import __constants__ as constants

from tqdm                               import tqdm
from multi_threading.tasks_manager      import TasksManager
from multi_threading.parallel_runner    import ParallelRunner
from posenet.posenet_client             import PosenetClient



class ProcessData:

    def __init__(self, args):
        dirname             = os.path.dirname(__file__)
        self.sit_path       = os.path.join(dirname, f'{args.data_input}/sit')
        self.middle_path    = os.path.join(dirname, f'{args.data_input}/middle')
        self.stand_path     = os.path.join(dirname, f'{args.data_input}/stand')
        self.output_path    = os.path.join(dirname, args.data_output)


    def run(self):
        data_frame = pd.DataFrame(columns = constants.COLUMN_NAMES)

        count_sit, sit_images           = self.read_all_images_folder(self.sit_path)
        count_middle, middle_images     = self.read_all_images_folder(self.middle_path)
        count_stand, stand_images       = self.read_all_images_folder(self.stand_path)

        total_number_of_image = sum([count_sit, count_middle, count_stand])
        print(f'Total {total_number_of_image} images.')
        print(f'{count_sit} sit images.')
        print(f'{count_middle} middle images.')
        print(f'{count_stand} stand images.')

        progress_bar = tqdm(total=total_number_of_image)

        self.add_data_to_data_frame(data_frame  , sit_images      , 0   , progress_bar)
        self.add_data_to_data_frame(data_frame  , middle_images   , 1   , progress_bar)
        self.add_data_to_data_frame(data_frame  , stand_images    , 2   , progress_bar)

        data_frame.to_csv(self.output_path, index=False, encoding='utf-8')
        progress_bar.close()


    @staticmethod
    def add_data_to_data_frame(data_frame, images, posture, progress_bar):
        posenet_client = PosenetClient(constants.POSENET_SERVER)

        tasks_manager = TasksManager(
                lambda image: posenet_client.get_pose(image).get_features(),
                images,
                lambda features: ProcessData.add_one_row_to_data_frame(data_frame, features, posture, progress_bar)
        )

        tasks_list = tasks_manager.callback_not_in_order_tasks_list()

        parallel_runner = ParallelRunner(constants.NUMBER_OF_WORKERS, constants.QUEUE_SIZE)
        parallel_runner.run(tasks_list)


    @staticmethod
    def add_one_row_to_data_frame(data_frame, features, posture, progress_bar):
        features.insert(0, posture)
        data_frame.loc[len(data_frame)] = features
        progress_bar.update()


    @staticmethod
    def read_all_images_folder(folder):
        files_list = os.listdir(folder)
        files_list = list(map(lambda file: os.path.join(folder, file), files_list))

        number_of_files = len(files_list)
        images = ProcessData.read_all_images_generator(files_list)

        return number_of_files, images


    @staticmethod
    def read_all_images_generator(files_list):
        for file in files_list:
            image = cv2.imread(file)
            if image:
                yield image
