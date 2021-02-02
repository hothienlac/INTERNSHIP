import threading
import queue



class Worker(threading.Thread):
    
    def __init__(self, jobs, *args, **kwargs):
        self.jobs = jobs
        super().__init__(*args, **kwargs)


    def run(self):
        while True:
            try:
                work = self.jobs.get(timeout=3)
            except queue.Empty:
                return
            work[0](*(work[1:]))
