import cv2
import numpy

capture =cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
ret,framepre=capture.read() #base frame
a=1
minframegap=5
vname=""
#vname=vname+
vname="clip"+str(a)+".avi"
out  =cv2.VideoWriter(vname,fourcc,30.0,(640,480))
while True:
    
    ret,framenew=capture.read()
    #out  =cv2.VideoWriter('outvid.avi',fourcc,30.0,(640,480))
    framediff=cv2.absdiff(framepre,framenew)
    diffgray=cv2.cvtColor(framediff,cv2.COLOR_BGR2GRAY)

    blurframe=cv2.GaussianBlur(diffgray,(5,5) ,0)
    _,framethresh=cv2.threshold(blurframe,20,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(framethresh, None, iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #cv2.drawContours(framepre,contours,-1,(0,255,0),2)
    for contour in contours:
        if cv2.contourArea(contour)<1000:
            if minframegap is 500:
                vname="clip"+str(a)+".avi"
                out  =cv2.VideoWriter(vname,fourcc,30.0,(640,480))
            minframegap=minframegap-1
            if minframegap <0:
                minframegap=0
        elif minframegap != 0: 
            ret,frame=capture.read() #ret will have true/false frame will have actual frame
            cv2.imshow('clip',frame)
            out.write(frame)
        if minframegap == 0:
            out.release()
            a=a+1


    cv2.imshow("detect",framepre)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cv2.destroyAllWindows()
out.release()
capture.release()


