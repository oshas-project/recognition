import face_recognition
from picamera import PiCamera
from time import sleep

def main():
	camera = PiCamera()
	camera.resolution = (1296, 972)
	# camera.rotation = 0

	finn_image = face_recognition.load_image_file('/home/pi/finn.jpg')
	finn_encoding = face_recognition.face_encodings(sample_image)[0]

	while True:
		camera.capture('/home/pi/oshas/recognition/images/currentsample.jpg')
		sample_image = face_recognition.load_image_file('/home/pi/oshas/recognition/images/currentsample.jpg')
		# handle multiple faces here?
		sample_encoding = face_recognition.face_encodings(sample_image)[0]
		results = face_recognition(compare_faces([finn_encoding], sample_encoding))
		print(results)

if __name__ == "__main__":
    main()