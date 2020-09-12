from cv2 import cv2

#cv2.namedWindow("output", cv2.WINDOW_NORMAL)

#load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#choose an image to detect faces
#img = cv2.imread('20190428_225553.jpg')

#To video capture from webcam
webcam = cv2.VideoCapture(0)
key=cv2.waitKey()

#iterate forever frames
while True:

    #read the current frame (boolean saying if the reading was successful or not, frame)
    successful_frame_read, frame = webcam.read()
    #must convert to grayscale (convert color BGR TO GRAY)
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #detect faces irrespective of the size of faces (coordinates are [x,y,width,height])
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Draw rectangles around the faces (image,first coordinate,last coordinate,color,thickness of line)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('Face Detection',frame)
    #hits a key every 1ms
    key=cv2.waitKey(1)

    #stop if q is pressed
    if key==81 or key==113:
        break

"""
#must convert to grayscale (convert color BGR TO GRAY)
grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect faces irrespective of the size of faces (coordinates are [x,y,width,height])
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
#(x,y,w,h)=face_coordinates

#print(face_coordinates)

#Draw rectangles around the faces (image,first coordinate,last coordinate,color,thickness of line)
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

#display image with faces
imSmall=cv2.resize(img,(900,900))
cv2.imshow('Face Detection',imSmall)
cv2.waitKey()
"""

print("Code Completed")