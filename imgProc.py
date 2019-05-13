from PIL import Image
import cv2, random, os
import numpy as np

bg = Image.open("C:/Users/Martin/Pictures/backgrounds/darkgreen.jpg")

im = bg.copy()
im.paste(img, (0, 0))



h, w, l = np.array(img).shape


vid = cv2.VideoWriter("demo.avi", cv2.VideoWriter_fourcc(*'DIVX'), 10, (1280, 720))

for _ in range(100):
	vid.write(np.array(im))

vid.release()



def imgProcess(rawImages):
	#load in backgrounds
	backs = []
	path = "C:/Users/Martin/Pictures/backgrounds"
	for filename in os.listdir(path):
		back_path = os.path.join(path, filename)
		back = Image.open(back_path)
		backs.append(back)
	
	#process pics and add background
	ret = []
	for image in rawImages:
		h, w, l = np.array(image).shape

		if w >= 1100:
			ratio = h/w 
			w = 1000
			h = int(1000 * ratio)
			image.resize((1000, h))

		xcord = (1280 - w) // 2
		ycord = (720 - h) // 2

		rando = random.randint(0, len(backs) - 1)
		bcopy = backs[rando].copy()
		bcopy.paste(image, (xcord, ycord))
		ret.append(bcopy)
	#return array of final images on random backgrounds
	return ret

def imgFromFile(path):
	ret = []
	for filename in os.listdir(path):
		if filename[-4:] == ".jpg":
			img_path = os.path.join(path, filename)
			img = Image.open(img_path)
			ret.append(img)
	return ret
		


		
