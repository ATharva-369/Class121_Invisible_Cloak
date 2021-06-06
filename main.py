'''
Algorithm : 1]Capture and store background frame
            2]Detect red colored bottle using color detection and segmentation algorithm
            3]Segment out red-colored object by generating a mask
            4]Generate final augumented output
'''
import cv2
import numpy 
import time
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
cam = cv2.VideoCapture(0)
time.sleep(2)
bg = 0
for i in range(60):
    ret,bg = cam.read()
bg = numpy.flip(bg,axis=1)
while (cam.isOpened()):
    ret,img = cam.read()
    if not ret :
        break   
    img = numpy.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red= numpy.array([0,120,50])
    upper_red  = numpy.array([10,255,255])
    mask1 = cv2.inRange(hsv,lower_red,upper_red)
    lower_red= numpy.array([170,120,70])
    upper_red  = numpy.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)   
    mask1 = mask2 + mask1
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,numpy.ones((3,3),numpy.uint8)) 
    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_DILATE,numpy.ones((3,3),numpy.uint8))  
    mask2 = cv2.bitwise_not(mask1) #selecting the part that doesn't that mask1 and saving in mask2
    res_1 = cv2.bitwise_and(img,img,mask=mask2)
    res_2 = cv2.bitwise_and(img,img,mask=mask1)
    final_output = cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)
    cv2.imshow("Invisible Cloak",final_output)
    cv2.waitKey(1)

cam.release()
out.release()
cv2.destroyAllWindows()

