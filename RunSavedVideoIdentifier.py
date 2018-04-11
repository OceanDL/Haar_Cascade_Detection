import numpy as np
import cv2
import sys

# Cascade file to use, change name to whatever you called it.
cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(sys.argv[1])


while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grenade = cascade.detectMultiScale(gray)

    for (x, y, w, h) in grenade:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()