import subprocess
from gtts import gTTS

def procTxt(textPath):
	obj = open(textPath, "r")
	txt = obj.read()

	return txt

path = "C:/Users/Martin/reddit/1/dialogue.txt"
t = procTxt(path)
t = t.strip()
arr = t.split("\n")
print(t)

w = gTTS(t)
w.save("test.mp3")





