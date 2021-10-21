from picamera import PiCamera
from time import sleep

def main():
	camera = PiCamera()
	camera.capture('/home/pi/testing.jpg')

if __name__ == "__main__":
    main()