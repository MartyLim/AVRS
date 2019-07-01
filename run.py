import img, aud, cv2
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips


if __name__ == '__main__':
	#define relevant paths 
	path = "C:/Users/Martin/reddit/1"
	productPath = path + "/product.mp4"
	transPath = "C:/Users/Martin/reddit/data/tvtransition.mp4"

	#read in dialogue from txt file and process images 
	read = aud.procTxt(path)
	rawImgs = img.imgFromFile(path)
	imgs = img.imgProcess(rawImgs)

	vidTitles = []
	vidDia = []
	for k,v in read.items():
		vidTitles.append(k)
		vidDia.append(v)

	i = 0
	clips = []
	transition = VideoFileClip(transPath)
	for im in imgs:
		if im == None:
			clips.append(transition)
		else: 
			#create audio file and get length in seconds
			audPath = aud.tts(vidDia[i], path)
			length = aud.getLength(audPath)

			#write frames accoring to corresponding audio length 
			vidPath = img.createBase(im, length, path)

			#add audio and add final clip to list "clips"
			outPath = aud.addAud(vidPath, audPath, path + "/" + vidTitles[i] + ".mp4")
			clip = VideoFileClip(outPath)
			clips.append(clip)

	#concatenate clips to get final video
	fin = concatenate_videoclips(clips, method='compose')
	fin.write_videofile(path + "/final.mp4")


