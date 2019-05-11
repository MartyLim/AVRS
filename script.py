from PIL import Image
import cv2, numpy

img = cv2.imread("C:/Users/Martin/git/AVRS/data/test.jpg")

h, w, l = numpy.array(img).shape

vid = cv2.VideoWriter("demo.avi", cv2.VideoWriter_fourcc(*'DIVX'), 10, (w, h))

vid.write(img)

