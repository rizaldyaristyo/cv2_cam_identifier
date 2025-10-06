import os
os.environ["OPENCV_LOG_LEVEL"]="SILENT" # I just found this instead, either cv2 docs is confusing or it's just me can't read it properly
import cv2
# import ctypes
# # cv2 prints errors on c-level stderr dammit
# ctypes.CDLL(None).dup2(os.open(os.devnull, os.O_WRONLY), 2)  # redirect C stderr (fd=2) to devnull
def returnCameraIndexes():
    index = 0
    arr = []
    i = 10
    while i > 0:
        cap = cv2.VideoCapture(index)
        if cap.read()[0]:
            arr.append(index)
            cap.release()
        index += 1
        i -= 1
    return arr
print(returnCameraIndexes())