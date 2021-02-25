from util.image_processing import draw_function_factory, dot_function_factory



def draw_skeleton(image, pose):

    draw = draw_function_factory(image)

    draw(pose.leftShoulder, pose.rightShoulder)
    draw(pose.leftShoulder, pose.leftHip)
    draw(pose.rightShoulder, pose.rightHip)
    draw(pose.leftHip, pose.rightHip)
    draw(pose.leftHip, pose.leftKnee)
    draw(pose.rightHip, pose.rightKnee)
    draw(pose.leftKnee, pose.leftAnkle)
    draw(pose.rightKnee, pose.rightAnkle)

    dot = dot_function_factory(image)

    dot(pose.leftShoulder)
    dot(pose.rightShoulder)
    dot(pose.leftHip)
    dot(pose.rightHip)
    dot(pose.leftKnee)
    dot(pose.rightKnee)
    dot(pose.leftAnkle)
    dot(pose.rightAnkle)