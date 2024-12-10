import cv2
import numpy as np

video = cv2.VideoCapture(r'46026-447087782_small.mp4')

def video_brightness_contrast(frame,contrast,brightness):
    return cv2.convertScaleAbs(frame, alpha = 1 + contrast / 127, beta=brightness)

noise_kernel = (5,5)
enhanced_kernel = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1]
])
while True:
    res,frame = video.read()
    if not res:
        break
    adjusted_frame = video_brightness_contrast(frame,contrast = 10, brightness = 5)
    noise_frame = cv2.GaussianBlur(frame,noise_kernel,0)
    enhanced_frame = cv2.filter2D(frame, -1, enhanced_kernel)

    cv2.imshow('Adjusted Frame',adjusted_frame)
    cv2.imshow('Noise Reduction',noise_frame)
    cv2.imshow('Edge-Enhanced Frame', enhanced_frame)
    cv2.waitKey(1)