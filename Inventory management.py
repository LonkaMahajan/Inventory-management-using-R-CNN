!pip install progressbar2
!pip install cvlib
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
# from numpy.lib.polynomial import poly
image = cv2.imread("/content/appletree3.jpg")
input1 = input("Object name")
box,label,count = cv.detect_common_objects(image)
output = draw_bbox(image,box,label,count)
plt.imshow(output)
print(input1," are : " , end = " ")
label.count(input1)
