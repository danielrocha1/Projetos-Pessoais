import cv2 as cv
import numpy as np


cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
