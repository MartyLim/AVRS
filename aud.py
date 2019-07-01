import subprocess
from gtts import gTTS
from mutagen.mp3 import MP3

def procTxt(path):
	obj = open(path + "/dialogue.txt", "r")
	txt = obj.read()
	txt = txt.strip()
	arr = txt.split("\n")
	
	ret = {}
	for i in arr:
		point = i.index(":")
		ret[i[:point]] = i[point + 2:].strip()

	#dictionary of text to read, no indications for transitions.
	return ret 

def tts(text, path):
	speech = gTTS(text)
	tempPath = path + "/temp.mp3"
	speech.save(tempPath)

	#return path of mp3 file (overwritten to save memory)
	return tempPath 

def getLength(audPath):
	audio = MP3(audPath)
	return audio.info.length

def addAud(vidPath, audPath, outPath):
	command = "ffmpeg -y -i {video} -i {audio} -c copy -map 0:v:0 -map 1:a:0 {out}".format(video=vidPath, audio=audPath, out=outPath)
	subprocess.call(command, shell=True)
	return vidPath

