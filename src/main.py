import face_recognition
from picamera import PiCamera
from time import sleep

def main():
	print('STARTED loading camera')
	camera = PiCamera()
	print('ENDED loading camera')
	print('STARTED changing resolution')
	camera.resolution = (540, 405)
	print('ENDED changing resolution')
	camera.rotation = 90

	print('STARTED loading finn image')
	finn_image = face_recognition.load_image_file('/home/pi/finn.jpg')
	print('ENDED loading finn image')
	print('STARTED loading finn encoding')
	finn_encoding = face_recognition.face_encodings(finn_image)[0]
	print('ENDED loading finn encoding')

	print('\nSTARTED while loop')
	while True:
		print('\n-- NEW LOOP ENTRY --')
		
		# CAPTURING OF SAMPLE
		print('STARTED capturing current sample')
		camera.capture('/home/pi/oshas/recognition/images/currentsample.jpg')
		print('ENDED capturing current sample')
		
		# LOADING OF SAMPLE
		print('STARTED loading current sample')
		sample_image = face_recognition.load_image_file('/home/pi/oshas/recognition/images/currentsample.jpg')
		print('ENDED loading current sample')
		# todo: handle multiple faces here?

		# ENCODING OF IMAGE
		print('STARTED encoding sample')
		sample_encodings = face_recognition.face_encodings(sample_image)
		print('ENDED encoding sample')

		# RESULTS
		if (len(sample_encodings) > 0):
			target_sample_encoding = sample_encodings[0]
			results = face_recognition.compare_faces([finn_encoding], target_sample_encoding)
			print(results)
		else:
			print('no face detected')
		print('-- ENDED LOOP ENTRY --\n')
		

if __name__ == "__main__":
    main()