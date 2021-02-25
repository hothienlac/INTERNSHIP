import cv2



class VideoUtil:

    @staticmethod
    def read_video(path):
        vidcap = cv2.VideoCapture(path)
        
        while(vidcap.isOpened()):
            ret, frame = vidcap.read()
            if ret == False:
                break
            yield frame

        vidcap.release()


    @staticmethod
    def get_frame_rate(path):
        video = cv2.VideoCapture(path)
        fps = video.get(cv2.CAP_PROP_FPS)
        video.release()

        return fps


    @staticmethod
    def get_dimention(path):
        video = cv2.VideoCapture(path)
        width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        video.release()

        return (int(width), int(height))


    @staticmethod
    def get_number_of_frame(path):
        video = cv2.VideoCapture(path)
        number_of_frame = video.get(cv2.CAP_PROP_FRAME_COUNT)

        return number_of_frame


    @staticmethod
    def draw_text(image, text, line):
        height, width, channels = image.shape
        root = (width//20, width//10*line)
        cv2.putText(image, text, root, cv2.FONT_HERSHEY_SIMPLEX, height//200, (255, 0, 0), height//200, cv2.LINE_AA)


    @staticmethod
    def draw_nose_velocity(image, velocity):
        height, width, channels = image.shape
        root = (width*4//5, height//2)
        cv2.arrowedLine(image, root, (root[0], root[1] + int(velocity*height*4)), (0, 0, 255), height//100)


    @staticmethod
    def draw_skeleton(image, pose):
        json_to_tuple = lambda a: (
            int(a['x']),
            int(a['y']),
        )

        draw_line = lambda a, b: cv2.line(
            image,
            json_to_tuple(a),
            json_to_tuple(b),
            (255, 0, 0),
            thickness=3
        )

        draw_line(pose.left_shoulder, pose.right_shoulder)
        draw_line(pose.left_shoulder, pose.left_hip)
        draw_line(pose.right_shoulder, pose.right_hip)
        draw_line(pose.left_hip, pose.right_hip)
        draw_line(pose.left_hip, pose.left_knee)
        draw_line(pose.right_hip, pose.right_knee)
        draw_line(pose.left_knee, pose.left_ankle)
        draw_line(pose.right_knee, pose.right_ankle)
        
        draw_dot = lambda a: cv2.circle(
            image,
            json_to_tuple(a),
            6, (00,255,0), -6,
        )

        draw_dot(pose.left_shoulder)
        draw_dot(pose.right_shoulder)
        draw_dot(pose.left_hip)
        draw_dot(pose.right_hip)
        draw_dot(pose.left_knee)
        draw_dot(pose.right_knee)
        draw_dot(pose.left_ankle)
        draw_dot(pose.right_ankle)


    class VideoWriter:
        def __init__(self, path, fps=30, dimention=(1920,1080)):
            self.video = cv2.VideoWriter(path,cv2.VideoWriter_fourcc(*'XVID'), fps, dimention, True)

        def add_frame(self, frame):
            self.video.write(frame)
        
        def save(self):
            self.video.release()

