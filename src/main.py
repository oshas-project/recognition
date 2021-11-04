import face_recognition
import pickle
import numpy as np
import os
from picamera import PiCamera
from time import sleep

import requests

CURRENT_SAMPLE_PATH = '/home/pi/oshas/recognition/currentsample.jpg'
FACES_PATH = '/home/pi/oshas/recognition/faces/'

# PROD IP: 192.168.0.4
API_PATH = 'https://192.168.0.2:5000'

LOGGING = False

def main():
	if LOGGING: 
		print('STARTED loading camera')
	camera = PiCamera()
	if LOGGING: 
		print('ENDED loading camera')
		print('STARTED changing resolution')
	camera.resolution = (540, 405)
	if LOGGING: 
		print('ENDED changing resolution')
	camera.rotation = 90

	known_face_encodings = load_faces()

	'''
	print('\n-- FINN ENCODING DUMPED --')
	finn_encoding_bytes = pickle.dumps(finn_encoding)
	print(type(finn_encoding_bytes))
	print(finn_encoding_bytes)
	print(pickle.loads(finn_encoding_bytes))
	print('\n-- FINN ENCODING DUMPED --')
	'''

	print('\nSTARTED while loop')
	while True:
		if LOGGING: 
			print('\n-- NEW LOOP ENTRY --')
		
		# CAPTURING OF SAMPLE
		if LOGGING: 
			print('STARTED capturing current sample')
		camera.capture(CURRENT_SAMPLE_PATH)
		if LOGGING: 
			print('ENDED capturing current sample')
		
		# LOADING OF SAMPLE
		if LOGGING: 
			print('STARTED loading current sample')
		sample_image = face_recognition.load_image_file(CURRENT_SAMPLE_PATH)
		if LOGGING: 
			print('ENDED loading current sample')
		# todo: handle multiple faces here?

		# ENCODING OF IMAGE
		if LOGGING: 
			print('STARTED encoding sample')
		sample_encodings = face_recognition.face_encodings(sample_image)
		if LOGGING: 
			print('ENDED encoding sample')

		# RESULTS
		if (len(sample_encodings) > 0):
			unknown_face = True
			target_sample_encoding = sample_encodings[0]
			for known_face_encoding in known_face_encodings:
				results = face_recognition.compare_faces([known_face_encoding[1]], target_sample_encoding)
				if results[0] == True:
					username = known_face_encoding[0]
					print('[FACE] ' + username + ' DETECTED')
					unknown_face = False

					send_api_event('face_detected', username)
			if unknown_face == True:
				print('[FACE] UNKNOWN FACE DETECTED')

				send_api_event('face_detected', 'unknown') 
		
		if LOGGING: 
			print('-- ENDED LOOP ENTRY --\n')

def load_faces():
	faces = []
	for filename in os.listdir(FACES_PATH):
		if (filename.endswith('.jpg')):
			subject_name = filename.replace('.jpg', '')
			print(subject_name + ' found in directory')
			print('STARTED LOADING IMAGE OF ' + subject_name)
			subject_image = face_recognition.load_image_file(FACES_PATH + subject_name + '.jpg')
			print('LOADED IMAGE')
			print('ENCODING ' + subject_name)
			subject_encoding = face_recognition.face_encodings(subject_image)[0]
			print('ENCODED')
			faces.append([subject_name, subject_encoding])
	return faces

def send_api_event(event_id, username):
	URL = API_PATH + '/event'
	PARAMS = {
		'event_id':event_id,
		'username':username
		}
	r = requests.get(url = URL, params = PARAMS)

	data = r.json()
	print(data)

if __name__ == "__main__":
    main()