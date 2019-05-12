import imgScript


if __name__ == '__main__':
	raw_imgs = imgScript.imgFromFile("C:/Users/Martin/git/AVRS/data")

	proc_imgs = imgScript.imgProcess(raw_imgs)

	proc_imgs[0].show()