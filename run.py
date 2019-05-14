import imgProc
import audProc


if __name__ == '__main__':
	vid = cv2.VideoWriter("demo.avi", cv2.VideoWriter_fourcc(*'DIVX'), 10, (1280, 720))

for _ in range(100):
	vid.write(np.array(im))

vid.release()