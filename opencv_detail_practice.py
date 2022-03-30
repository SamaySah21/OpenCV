# opencv-python is the main library
#opencv-contrib-python = opencv-python (packages) + contributor packages

# !pip install opencv-contrib-python

# Caer is a GPU-accelerated Computer Vision library in Python that's designed to help speed up your Computer Vision workflow.

# !pip install caer

import cv2 as cv

                  # READ IMAGE
img = cv.imread("gr_dog.jpg")
cv.imshow("dog", img)
cv.waitKey(0)   # 0 means show the image infintely untill any key is pressed

                 # READ VIDEO
# capture = cv2.VideoCapture(video_path)

# capture = cv2.VideoCapture(0) # 0 for webcam

#capture = cv2.VideoCapture(1) # 1 for first camera connected to computer

#capture = cv2.VideoCapture(2) # 2 for second camera connected to computer



