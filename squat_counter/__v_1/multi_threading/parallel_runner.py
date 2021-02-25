from multi_threading.worker import Worker
import queue



class ParallelRunner:
    
    def __init__(self, workers, queue_size):
        self.q = queue.Queue(queue_size)
        self.workers = []
        for _ in range(workers):
            worker = Worker(self.q)
            self.workers.append(worker)


    def start(self, jobs):
        for worker in self.workers:
            worker.start()

        for job in jobs:
            self.q.put(job, block=True, timeout=60)

        for worker in self.workers:
            worker.join()
