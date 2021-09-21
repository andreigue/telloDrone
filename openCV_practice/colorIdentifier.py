import cv2

cap = cv2.VideoCapture(0) #capture stream from main camera on laptop
cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
