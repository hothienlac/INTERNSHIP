from tqdm import tqdm

### Receive multi worker result, and run handler function in right order


## compare_function(a, b) return True if a<b if ascending. Assuming that already sorted
def insert_to_right_position(queue, element, compare_function):
    if len(queue) == 0:
        queue.append(element)
        return
    for i in range(len(queue)):
        if compare_function(element, queue[i]):
            queue.insert(i, element)
            return
    queue.append(element)
    return



class MultiWorkerHandler:
    def __init__(self, handler):
        self.handler = handler
        self.queue = []
        ## call handler if new received result equal next index
        self.next_index = 0
        self.progress_bar = tqdm()
    

    # Result is in format (index, result)
    def add_to_queue(self, result):
        compare_function = lambda x,y: x[0] < y[0]
        insert_to_right_position(self.queue, result, compare_function)
        self.check_queue()


    def check_queue(self):
        while len(self.queue) > 0:
            if self.next_index != self.queue[0][0]:
                return
            self.run_handler()
    

    def run_handler(self):
        self.handler(self.queue.pop(0)[1])
        self.progress_bar.update()
        self.next_index += 1


    def done(self):
        self.progress_bar.close()
