import cv2
import numpy as np

cap = cv2.VideoCapture('video/DJI_0636.MP4')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fgbg = cv2.createBackgroundSubtractorMOG2()
out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 进行前景-背景分离处理
    fgmask = fgbg.apply(frame)
    
    # 对前景区域进行膨胀操作，以填补目标物体周围的空洞
    kernel = np.ones((5,5), np.uint8)
    fgmask = cv2.dilate(fgmask, kernel, iterations=1)
    
    # 将前景区域覆盖为黑色，以实现移除目标物体的效果
    frame[fgmask==255] = 0
    
    # 将处理后的帧写出到输出视频中
    out.write(frame)

# 释放资源
cap.release()
out.release()
