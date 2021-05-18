import cv2
import numpy as np
import utlis

def getLaneCurve(img):

    imgThres = utlis.thresholding(img)
    cv2.imshow("ThresHold",imgThres)

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        img = cv2.resize(img, (480, 240))

        getLaneCurve(img)
        cv2.imshow('Vid',img)
        cv2.waitKey(1)