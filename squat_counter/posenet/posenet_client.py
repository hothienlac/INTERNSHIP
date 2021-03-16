import grpc
import json
import cv2
import base64

from .grpc import picture_pb2
from .grpc import picture_pb2_grpc
from .pose import Pose



class PosenetClient:

    def __init__(self, server):
        channel = grpc.insecure_channel(server)
        self.stub = picture_pb2_grpc.GetPoseStub(channel)


    def get_pose(self, image):
        pose = self.get_json(image)

        return Pose(pose)
    

    def get_json(self, image):
        base64_encoded_image = self.image_to_base64(image)

        grpc_payload = picture_pb2.Picture(picture=base64_encoded_image)
        grpc_result = self.stub.getPose(grpc_payload)

        return json.loads(grpc_result.pose)


    @staticmethod
    def image_to_base64(image):
        retval, buffer = cv2.imencode('.jpg', image)
        encoded = base64.b64encode(buffer)

        return 'data:image/jpeg;base64,'.encode() + encoded
