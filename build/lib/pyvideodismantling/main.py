import cv2


def split_action(videoPath,picturePath,step=5):
    '''
    视频拆分
    :param videoPath:视频地址
    :param picturePath: 图片地址
    :param stop: 调节时间
    :return:
    '''

    vc=cv2.VideoCapture(videoPath)      #原始视频路径按实际调整

    c=1

    if vc.isOpened():

        rval,frame=vc.read()

    else:

        rval=False


    while rval:
        rval, frame = vc.read()
        if c % step == 0:

            path = str(picturePath) + "/" + str(c) + ".jpg"
            cv2.imwrite(path, frame)  # 视频帧图片另存路径按实际调整
            print(c)
        c = c + 1
        cv2.waitKey(1)
    vc.release()

    return "视频拆分完成"
