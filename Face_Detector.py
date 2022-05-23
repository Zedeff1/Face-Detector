import cv2
from random import randrange

#Load some pre-trained data
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0)
#address = 'http://192.168.1.4:8080/video'			#From ip webcam
#webcam.open(address)

#Choose an image to detect faces in
#img = cv2.imread('C:/Users/umbal/OneDrive/Desktop/CS_Projekt/Clever Programer/Face Detection/face_1.jpg')

# Iterate forever in our frames
while True:

	#read the current frames
	successful_frame_read, frame = webcam.read()

	#Must convert to grey scale
	greyscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	face_coordinates = trained_face_data.detectMultiScale(greyscale_img)
	# [[240 43 176 176]]
	#    x   y  w   h

	for (x, y, w, h) in face_coordinates:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

	cv2.imshow('Tess Face Detector', frame)
	key = cv2.waitKey(1)

	#stop if Q is pressed
	if key == 81 or key == 113:
		break

#release webcam object
webcam.release()



#create greyscale of img cuz its easier to detect b&w pixels than rgb




#Draw rectangles around the faces


#Shows face
"""
cv2.imshow('Tess Face Detector', img)

cv2.waitKey()	#pauses the code execution until a key is pressed
 
"""
print("Code completed")
