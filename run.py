import imgProc


if __name__ == '__main__':
	raw_imgs = imgProc.imgFromFile("C:/Users/Martin/git/AVRS/data")

	proc_imgs = imgProc.imgProcess(raw_imgs)

	proc_imgs[0].show()