"""
This code takes a picture file (ex: jpg, png) and returns face coordinates.

Libraries used:
OpenCV
Numpy

Original sample OpenCV code:
https://realpython.com/face-recognition-with-python/

Edited by John Wu, 9/5/2018

"""

import cv2
import sys
import os
import numpy as np

def face_tracking(path):
	# Get user supplied values
	abs_path = os.path.dirname(os.path.abspath(__file__))
	image_file = os.path.join(abs_path, 'abba.png')
	#imagePath = "D:/image.jpg"
	imagePath = path

	#LabVIEW doesn't seem to like relative paths, hence the explicit path.
	model_file = os.path.join(abs_path, 'haarcascade_frontalface_default.xml')
	cascPath = model_file

	# Create the haar cascade
	faceCascade = cv2.CascadeClassifier(cascPath)

	# Read the image
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		# flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))
	print(type(faces))
	
	#define an empty list, in cases there are no elements in 'faces'
	pp = [0,0,0,0]

	if (len(faces) == 0):
		print(pp)
		return("pp")
	else:
		pp = faces.tolist()
		print (pp)
		print(type(pp))

		
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

		'''Disable the python image interface'''
		# cv2.imshow("Faces found", image)
		# cv2.waitKey(0)
		
		return(pp);