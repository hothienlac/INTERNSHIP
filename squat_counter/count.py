# from model.deep_neural_network          import DeepNeuralNetwork
from model.gaussian_naive_bayes         import GaussianNaiveBayes
from model.random_forest                import RandomForest

from multi_threading.parallel_runner    import ParallelRunner
from multi_threading.tasks_manager      import TasksManager

from posenet.posenet_client             import PosenetClient

from tqdm               import tqdm
import os

from   __video_util__   import VideoUtil
from   __velocity__     import Velocity
from   __counter__      import Counter
import __constants__    as constants



class Count:
    def __init__(self, args):
        dirname = os.path.dirname(__file__)

        self.model_path = args.model_path
        if not self.model_path:
            self.model_path = f'./model/{args.model}.model'
        self.model_path = os.path.join(dirname, self.model_path)

        video_input = args.video
        if not video_input:
            video_input = './data/a.mp4'
        video_input = os.path.join(dirname, video_input)

        video_output = args.video_output
        if not video_output:
            video_output = video_input[:-4] + '_count_squat.mp4'
        video_output = os.path.join(dirname, video_output)
        
        fps = VideoUtil.get_frame_rate(video_input)
        if fps > 60:
            fps = 30

        dimention               = VideoUtil.get_dimention(video_input)
        number_of_frame         = VideoUtil.get_number_of_frame(video_input)
        self.model              = Count.load_model(args.model, self.model_path)
        self.video              = VideoUtil.read_video(video_input)
        self.video_writer       = VideoUtil.VideoWriter(video_output, fps, dimention)
        self.velocity           = Velocity()
        self.counter            = Counter()
        self.progress_bar       = tqdm(total=number_of_frame)
        self.posenet_client     = PosenetClient(constants.POSENET_SERVER)


    def run(self):
        tasks_manager = TasksManager(
            lambda frame: (frame, self.posenet_client.get_pose(frame)),
            self.video,
            self.process_frame,
        )

        tasks_list = tasks_manager.callback_in_order_tasks_list()

        parallel_runner = ParallelRunner(constants.NUMBER_OF_WORKERS, constants.QUEUE_SIZE)
        parallel_runner.run(tasks_list)

        self.progress_bar.close()
        self.video_writer.save()
        print('Video saved')


    def process_frame(self, result):
        frame, pose = result
        features    = pose.get_features()
        posture     = int(self.model.predict([features]))
        back_length = pose.get_back_length()

        self.velocity.update(pose.nose['y'], back_length)
        self.counter.update(posture, self.velocity.smooth_velocity)

        VideoUtil.draw_skeleton(frame, pose)
        VideoUtil.draw_nose_velocity(frame, self.velocity.smooth_velocity)

        VideoUtil.draw_text(frame, ['SIT', 'MIDDLE', 'STAND'][posture], 1)
        VideoUtil.draw_text(frame, str(self.counter.count), 2)

        self.video_writer.add_frame(frame)
        self.progress_bar.update()


    @staticmethod
    def load_model(model, model_path):
        model_dictionary = {
            # 'deep_neural_network': DeepNeuralNetwork,
            'gaussian_naive_bayes': GaussianNaiveBayes,
            'random_forest': RandomForest,
        }

        return model_dictionary[model].load(model_path)
