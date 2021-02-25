import cv2



def json_to_tuple(a):
    return (int(a.get('x')), int(a.get('y')))


def draw_line(image, a, b):
    line_thickness = 3
    cv2.line(image, a, b, (255, 0, 0), thickness=line_thickness)


def draw_function_factory(image):
    return lambda a, b: draw_line(image, json_to_tuple(a), json_to_tuple(b))


def draw_dot(image, a):
    cv2.circle(image, a, 6, (00,255,0), -6)


def dot_function_factory(image):
    return lambda a: draw_dot(image, json_to_tuple(a))
