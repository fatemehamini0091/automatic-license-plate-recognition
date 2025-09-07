import json

import cv2
import time

with open("configs/config.json") as f:
    config = json.load(f)


cpt = 0
maxFrames = 300

count=0
cap=cv2.VideoCapture(config["VIDEO_PATH_TRAINING"])
while cpt < maxFrames:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1080,500))
    cv2.imshow("test window", frame) # show image in a window
    cv2.imwrite(config["IMAGE_TRAINING_PATH"]+"/numberplate_%d.jpg" %cpt, frame)
    time.sleep(0.01)
    cpt += 1
    if cv2.waitKey(5)&0xFF==27:
        break
cap.release()   
cv2.destroyAllWindows()