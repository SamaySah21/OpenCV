# opencv-python is the main library
#opencv-contrib-python = opencv-python (packages) + contributor packages

# !pip install opencv-contrib-python

# Caer is a GPU-accelerated Computer Vision library in Python that's designed to help speed up your Computer Vision workflow.

# !pip install caer

import cv2 as cv

                  # READ IMAGE
def readImage():
    img = cv.imread("gr_dog.jpg")
    cv.imshow("dog", img)
    cv.waitKey(0)   # 0 means show the image infintely untill any key is pressed

# readImage()
                 # READ VIDEO
# capture = cv2.VideoCapture(video_path)

# capture = cv2.VideoCapture(0) # 0 for webcam

#capture = cv2.VideoCapture(1) # 1 for first camera connected to computer

#capture = cv2.VideoCapture(2) # 2 for second camera connected to computer

# reading the video present in local

def readVideo():
    capture_video = cv.VideoCapture("cars.avi")

    # video we can read frame by frame

    while True:
        isTrue, frame = capture_video.read()  # isTrue : whether frame is read or not

        cv.imshow("carvideo", frame)

        #  video will stop when any key is pressed and video rans for 20 ms
        if cv.waitKey(20) and 0xFF == ord("d"):
            break

    capture_video.release()  # releasing the pointer
    cv.destroyAllWindows()  # close all the windows


readVideo()
