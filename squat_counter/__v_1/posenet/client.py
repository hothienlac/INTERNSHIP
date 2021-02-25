import grpc
import json
import cv2
import base64

from .pose import Pose
from .proto import picture_pb2
from .proto import picture_pb2_grpc


channel = grpc.insecure_channel('localhost:5001')
stub = picture_pb2_grpc.GetPoseStub(channel)


def to_base64(image):
    retval, buffer = cv2.imencode('.jpg', image)
    encoded = base64.b64encode(buffer)

    return 'data:image/jpeg;base64,'.encode() + encoded


def get_pose(image):
    encoded_image = to_base64(image)

    picture = picture_pb2.Picture(picture=encoded_image)
    pose = stub.getPose(picture).pose

    pose = json.loads(pose)
    pose = Pose(pose.get('keypoints'))

    return pose