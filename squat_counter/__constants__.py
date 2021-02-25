COLUMN_NAMES = [
    'posture',

    'left_shoulder_left_hip_left_knee_angle',
    'left_hip_left_knee_left_ankle_angle',

    'right_shoulder_right_hip_right_knee_angle',
    'right_hip_right_knee_right_ankle_angle',

    'left_knee_left_hip_right_hip_angle',
    'left_knee_left_ankle_right_ankle_angle',

    'right_knee_right_hip_left_hip_angle',
    'right_knee_right_ankle_left_ankle_angle',


    'left_shoulder_left_hip_distance',
    'left_hip_left_knee_distance',
    'left_knee_left_ankle_distance',
    'left_shoulder_left_knee_distance',
    'left_shoulder_left_ankle_distancee',
    'left_hip_left_ankle_distance',

    'right_shoulder_right_hip_distance',
    'right_hip_right_knee_distance',
    'right_knee_right_ankle_distance',
    'right_shoulder_right_knee_distance',
    'right_shoulder_right_ankl_distancee',
    'right_hip_right_ankle_distance',

    'left_knee_right_knee_distance',
    'left_ankle_right_ankle_distancee',
]

NUMBER_OF_WORKERS = 24
QUEUE_SIZE = 24

POSENET_SERVER = 'localhost:5001'
