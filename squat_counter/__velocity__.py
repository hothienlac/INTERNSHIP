



class Velocity:

    def __init__(self):
        self.ALPHA              = 0.05
        self.BETA               = 1 - self.ALPHA
        self.smooth_velocity    = 0
        self.previous_nose      = None


    def update(self, nose, back_length):
        if not self.previous_nose:
            self.previous_nose = nose
            return

        velocity                = (nose - self.previous_nose) / back_length
        self.smooth_velocity    = self.smooth_velocity * self.BETA  +  velocity * self.ALPHA
        self.previous_nose      = nose

