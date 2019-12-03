import cv2
import numpy
import time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H%M%S")
capture =cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
time.sleep(1)
ret,framepre=capture.read() #base frame
#framepre=cv2.cvtColor(framepre,cv2.COLOR_BGR2GRAY)
a=1
minframegap=500
vname=""
#vname=vname+
#vname=str(now.strftime("%H%M%S"))+".avi"
vname="output.avi"
print(vname)
height=int(capture.get(3))
width=int(capture.get(4))
out  =cv2.VideoWriter(vname,fourcc,120.0,(height,width))
cv2.imshow("detect",framepre)
d=0
p=0
while capture.isOpened():
    d+=1
    ret,framenew=capture.read()
    #framenew=cv2.cvtColor(framenew,cv2.COLOR_BGR2GRAY)
    #out  =cv2.VideoWriter('outvid.avi',fourcc,30.0,(640,480))
    framediff=cv2.absdiff(framepre,framenew)
    diffgray=cv2.cvtColor(framediff,cv2.COLOR_BGR2GRAY)
    #diffgray=framediff
    blurframe=cv2.GaussianBlur(diffgray,(5,5) ,0)
    _,framethresh=cv2.threshold(blurframe,10,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(framethresh, None, iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(framepre,contours,-1,(0,255,0),2)
    for contour in contours:
        print(cv2.contourArea(contour))
        if cv2.contourArea(contour)>7500:
	    
            #ret,frame=capture.read() #ret will have true/false frame will have actual frame
	    
            cv2.imshow('clip',framenew)
            p+=1
            out.write(framenew)
        #if minframegap == 0:
            #out.release()
            #a=a+1


    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()
#print(p,d)
out.release()
capture.release()


