import cv2
detect = cv2.CascadeClassifier("haarcascase_frontalface_default.xml")
imp_img = cv2.VideoCapture("rayan.jpg")

res , img = imp_img.read()
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

faces = detect.detectMultiScale(gray , 1.3 , 5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+w),(255,255,0),2)
cv2.imshow("rayan Image" , img)

cv2.waitKey(2000)

cv2.destroyAllWindow()
