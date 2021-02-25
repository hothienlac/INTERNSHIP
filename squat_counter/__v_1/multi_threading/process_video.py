from multi_threading.parallel_runner import ParallelRunner
from multi_threading.multi_worker_handler import MultiWorkerHandler
from multi_threading.jobs_generator import job_generator


NUMBER_OF_FEATURES = 16
NUMBER_OF_WORKERS = 12
QUEUE_SIZE = 24


def video_generator_with_frame_index(video):
    for i, frame in enumerate(video):
        yield (i, frame)


def add_frame_to_video_writer_factory(video_writer):
    return lambda frame: video_writer.add_frame(frame)


def process_frame(function_to_work, handler, args):
    count, frame = args
    function_to_work(frame)
    handler.add_to_queue((count, frame))


def process_frame_factory(function_to_work, handler):
    return lambda args: process_frame(function_to_work, handler, args)


def process_video(function_to_work, video, video_writer, in_order=True):
    video_generator = video_generator_with_frame_index(video)

    handler = MultiWorkerHandler(add_frame_to_video_writer_factory(video_writer), in_order)
    function_to_work_2 = process_frame_factory(function_to_work, handler)

    jobs = job_generator(function_to_work_2, video_generator)
    parallel_runner = ParallelRunner(NUMBER_OF_WORKERS, QUEUE_SIZE)
    parallel_runner.start(jobs)
