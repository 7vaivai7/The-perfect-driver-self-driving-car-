import cv2
import numpy as np
import utlis

def getLaneCurve(img):

    imgThres = utlis.thresholding(img)
    cv2.imshow("THRES",imgThres)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while True:
        success,img =cap.read()
        img = cv2.resize(img,(480,240))
        cv2.imshow('VID',img)
        cv2.waitKey(1)
        getLaneCurve()