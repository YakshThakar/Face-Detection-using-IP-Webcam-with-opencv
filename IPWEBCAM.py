import cv2
import numpy as np
import urllib.request

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
url=""
scaling_factor =0.75
        while True:
                imglink=urllib.request.urlopen(url).read()
                imgNp=np.array(bytearray(imglink.read(),dtype=np.uint8))
                img = cv2.imdecode(imgNp,-1)
                frame = cv2.resize(frame, None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
                face_rects = face_cascade.detectMultiScale(frame, 1.3, 2)
                for (x,y,w,h) in face_rects:
                        cv2.rectangle(frame, (x,y), (x+w,y+h), (3400,1234,2500), 5)
                        cv2.imshow('Face Detector', frame)
                        c = cv2.waitKey(1)
               
        cap.release()
        cv2.destroyAllWindows()
