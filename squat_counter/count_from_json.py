from tqdm               import tqdm
import joblib
import os

from   __velocity__     import Velocity
from   __counter__      import Counter
from  posenet.pose      import Pose

class CountFromJSON:

    # Use Pretrained Random Forest as Default
    def __init__(self, json_input, model_path='./model/random_forest.model'):
        dirname             = os.path.dirname(__file__)
        self.model_path     = os.path.join(dirname, model_path)
        self.model          = joblib.load(self.model_path)
        self.json_input     = JSONInput(json_input)
        self.velocity       = Velocity()
        self.counter        = Counter()
        self.progress_bar   = tqdm(total=self.json_input.number_of_frame)

# self.counter.count

    def count(self):
        for frame in self.json_input.json_input:
            self.process_frame(frame)
            self.progress_bar.update()
        self.progress_bar.close()
        return self.counter.count


    def process_frame(self, result):
        pose = result
        features    = pose.get_features()[1:]
        posture     = int(self.model.predict([features]))
        back_length = pose.get_back_length()

        self.velocity.update(pose.nose['y'], back_length)
        self.counter.update(posture, self.velocity.smooth_velocity)



class JSONInput:

    def __init__(self, json_input):
        self.json_input         = list(map(lambda x: Pose(x[0]), json_input['data']))
        self.number_of_frame    = len(self.json_input)
