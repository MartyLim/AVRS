from PIL import Image
import cv2, random, os
import numpy as np
import math


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
		if image != None:
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
	orient = []
	titleim = []
	for filename in os.listdir(path):
		if filename[-4:] == ".JPG" or filename[-4:] == ".jpg":
			if len(filename) < 9 or filename[-9:-4] != "title":
				orient.append(filename)
			else:
				img_path = os.path.join(path, filename)
				img = Image.open(img_path)
				titleim.append(img)
	orient.sort()
	insert = []
	for i in range(len(orient)-1):
		if orient[i][0] != orient[i+1][0]:
			insert.append(i+1)
	inc = 0
	for i in insert:
		orient.insert(i+inc, None)
		inc += 1
	for filename in orient:
		if filename != None:
			img_path = os.path.join(path, filename)
			img = Image.open(img_path)
			ret.append(img)
		else:
			ret.append(filename)
	ret.insert(0, titleim[0]) 

	#return array of image objects with None for transitions 
	#Turn to array before feeding into VideoWriter
	return ret

#take in processed image obj, audio length in seconds, and save path
def createBase(img, audLength, path):
	vidPath = path + "/temp.mp4"
	vid = cv2.VideoWriter(vidPath, cv2.VideoWriter_fourcc(*'mp4v'), 29.97, (1280, 720))
	numFrames = 30 * math.ceil(audLength)
	for _ in range(numFrames):
		vid.write(np.array(img))
	vid.release()

	return vidPath

		



	
		
