import face_recognition
import pickle
import numpy as np
import os
from picamera import PiCamera
from time import sleep

IMAGE_PATH = '/home/pi/oshas/recognition/faces/'

def main():
	print('STARTED loading camera')
	camera = PiCamera()
	print('ENDED loading camera')
	print('STARTED changing resolution')
	camera.resolution = (540, 405)
	print('ENDED changing resolution')
	camera.rotation = 90
	
	print('\nPlease type the name of this user:')
	name = input('')
	
	print('\n-- CHECK ORIENTATION! --')
	print('-- MAKE SURE YOUR FACE IS VISIBLE\n ')
	print('-- YOU SHOULD BE THE ONLY PERSON IN SHOT')

	sleep(4)

	print('CAPTURING IN 3...')
	sleep(1)
	print('CAPTURING IN 2..')
	sleep(1)
	print('CAPTURING IN 1.')
	sleep(1)

	print('\nSTARTED capturing current sample')
	camera.capture(IMAGE_PATH + name.lower() + '.jpg')
	print('ENDED capturing current sample')

if __name__ == "__main__":
    main()