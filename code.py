Run the below code to read and display image using OpenCV in google collab,
import cv2
import numpy as np
from google.colab.patches import cv2_imshow

img=cv2.imread("TajMahal.JPG")

cv2_imshow(img)

