import numpy as np



class Pose:

    def __init__(self, pose):
        self.nose           =   pose[0].get('position')
        self.left_shoulder   =   pose[5].get('position')
        self.left_hip        =   pose[11].get('position')
        self.left_knee       =   pose[13].get('position')
        self.left_ankle      =   pose[15].get('position')
        self.right_shoulder  =   pose[6].get('position')
        self.right_hip       =   pose[12].get('position')
        self.right_knee      =   pose[14].get('position')
        self.right_ankle     =   pose[16].get('position')
    

    def get_features(self):
        back_length = self.get_back_length()

        left_shoulder_left_hip_left_knee_angle        =   Pose.calculate_angle(self.left_shoulder     , self.left_hip     , self.left_knee)
        left_hip_left_knee_left_ankle_angle           =   Pose.calculate_angle(self.left_hip          , self.left_knee    , self.left_ankle)
        right_shoulder_right_hip_right_knee_angle     =   Pose.calculate_angle(self.right_shoulder    , self.right_hip    , self.right_knee)
        right_hip_right_knee_right_ankle_angle        =   Pose.calculate_angle(self.right_hip         , self.right_knee   , self.right_ankle)

        left_knee_left_hip_right_hip_angle            =   Pose.calculate_angle(self.left_knee         , self.left_hip     , self.right_hip)
        left_knee_left_ankle_right_ankle_angle        =   Pose.calculate_angle(self.left_knee         , self.left_ankle   , self.right_ankle)
        right_knee_right_hip_left_hip_angle           =   Pose.calculate_angle(self.right_knee        , self.right_hip    , self.left_hip)
        right_knee_right_ankle_left_ankle_angle       =   Pose.calculate_angle(self.right_knee        , self.right_ankle  , self.left_ankle)


        left_shoulder_left_hip_distance               =   Pose.calculate_distance(self.left_shoulder    , self.left_hip)    / back_length
        left_hip_left_knee_distance                   =   Pose.calculate_distance(self.left_hip         , self.left_knee)   / back_length
        left_knee_left_ankle_distance                 =   Pose.calculate_distance(self.left_knee        , self.left_ankle)  / back_length
        left_shoulder_left_knee_distance               =   Pose.calculate_distance(self.left_shoulder    , self.left_knee)   / back_length
        left_shoulder_left_ankle_distancee             =   Pose.calculate_distance(self.left_shoulder    , self.left_ankle)  / back_length
        left_hip_left_ankle_distance                  =   Pose.calculate_distance(self.left_hip         , self.left_ankle)  / back_length

        right_shoulder_right_hip_distance             =   Pose.calculate_distance(self.right_shoulder   , self.right_hip)   / back_length
        right_hip_right_knee_distance                 =   Pose.calculate_distance(self.right_hip        , self.right_knee)  / back_length
        right_knee_right_ankle_distance               =   Pose.calculate_distance(self.right_knee       , self.right_ankle) / back_length
        right_shoulder_right_knee_distance             =   Pose.calculate_distance(self.right_shoulder   , self.right_knee)  / back_length
        right_shoulder_right_ankl_distancee            =   Pose.calculate_distance(self.right_shoulder   , self.right_ankle) / back_length
        right_hip_right_ankle_distance                =   Pose.calculate_distance(self.right_hip        , self.right_ankle) / back_length

        left_knee_right_knee_distance                 =   Pose.calculate_distance(self.left_knee        , self.right_knee)  / back_length
        left_ankle_right_ankle_distancee              =   Pose.calculate_distance(self.left_ankle       , self.right_ankle) / back_length

        return [
            left_shoulder_left_hip_left_knee_angle,
            left_hip_left_knee_left_ankle_angle,
            right_shoulder_right_hip_right_knee_angle,
            right_hip_right_knee_right_ankle_angle,

            left_knee_left_hip_right_hip_angle,
            left_knee_left_ankle_right_ankle_angle,
            right_knee_right_hip_left_hip_angle,
            right_knee_right_ankle_left_ankle_angle,


            left_shoulder_left_hip_distance,
            left_hip_left_knee_distance,
            left_knee_left_ankle_distance,
            left_shoulder_left_knee_distance,
            left_shoulder_left_ankle_distancee,
            left_hip_left_ankle_distance,

            right_shoulder_right_hip_distance,
            right_hip_right_knee_distance,
            right_knee_right_ankle_distance,
            right_shoulder_right_knee_distance,
            right_shoulder_right_ankl_distancee,
            right_hip_right_ankle_distance,

            left_knee_right_knee_distance,
            left_ankle_right_ankle_distancee,
        ]


    def get_back_length(self):
        left_shoulder_left_hip_distance     =   Pose.calculate_distance(self.left_shoulder    , self.left_hip)
        right_hip_right_knee_distance       =   Pose.calculate_distance(self.right_shoulder    , self.right_hip)
        
        backlength = (left_shoulder_left_hip_distance + right_hip_right_knee_distance) / 2

        return backlength


    @staticmethod
    def dict_to_np_array(a):
        x = a['x']
        y = a['y']

        return np.array([x, y])
    

    @staticmethod
    def calculate_distance(a, b):
        A = Pose.dict_to_np_array(a)
        B = Pose.dict_to_np_array(b)
        distance = np.linalg.norm(A - B)
        
        return distance


    @staticmethod
    def calculate_angle(a, b, c):
        A = Pose.dict_to_np_array(a)
        B = Pose.dict_to_np_array(b)
        C = Pose.dict_to_np_array(c)

        BA = A - B
        BC = C - B

        cosine_angle = np.dot(BA, BC) / (np.linalg.norm(BA) * np.linalg.norm(BC))
        angle = np.arccos(cosine_angle)

        # Calculate Sign of determinant, to distinguish between (ABC) and (CBA)
        det = np.linalg.det([BA, BC])
        sign = np.sign(det)

        return angle * sign

