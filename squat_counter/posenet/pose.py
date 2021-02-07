import numpy as np



def dict_to_np_array(x):
    return np.array([x.get('x'), x.get('y')])



def calculate_angle(a, b, c):
    A, B, C = list(map(dict_to_np_array, [a,b,c]))

    BA = A - B
    BC = C - B

    cosine_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
    angle = np.arccos(cosine_angle)

    return angle



class Pose:
    def __init__(self, pose):
        if pose == None:
            return

        self.pose = pose

        self.leftShoulder   =   pose[5].get('position')
        self.rightShoulder  =   pose[6].get('position')
        self.leftHip        =   pose[11].get('position')
        self.rightHip       =   pose[12].get('position')
        self.leftKnee       =   pose[13].get('position')
        self.rightKnee      =   pose[14].get('position')
        self.leftAnkle      =   pose[15].get('position')
        self.rightAnkle     =   pose[16].get('position')
    
    
    # Return list, features are sorted
    def get_features(self):
        list_of_points = [
            self.leftShoulder,
            self.rightShoulder,
            self.leftHip,
            self.rightHip,
            self.leftKnee,
            self.rightKnee,
            self.leftAnkle,
            self.rightAnkle,
        ]

        x = list(map(lambda point: point.get('x'), list_of_points))
        y = list(map(lambda point: point.get('y'), list_of_points))

        min_x = min(x)
        min_y = min(y)
        x = list(map(lambda a: a - min_x, x))
        y = list(map(lambda a: a - min_y, y))

        center_x = max(x) / 2
        center_y = max(y) / 2
        x = list(map(lambda a: a - center_x, x))
        y = list(map(lambda a: a - center_y, y))

        scale = max(center_x, center_y)
        x = list(map(lambda a: a/scale, x))
        y = list(map(lambda a: a/scale, y))

        leftHipAngle = calculate_angle(self.leftShoulder, self.leftHip, self.leftKnee)
        rightHipAngle = calculate_angle(self.rightShoulder, self.rightHip, self.rightKnee)
        leftKneeAngle = calculate_angle(self.leftHip, self.leftKnee, self.leftAnkle)
        rightKneeAngle = calculate_angle(self.rightHip, self.rightKnee, self.rightAnkle)

        angles = [leftHipAngle, rightHipAngle, leftKneeAngle, rightKneeAngle]

        return x + y + angles