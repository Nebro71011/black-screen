import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
image = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

frame=cv2.resize(frame,(640,480))
image=cv2.resize(image,(640,480))

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        break
    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    mask=cv2.inRange(frame,u_black,l_black) 
    res=cv2.bitwise_and(frame,frame,mask=mask)

    f=frame-res
    f=np.where(f==0,image,f)

    final_output = cv2.addWeighted(res, 1, res, 1, 0)
    image.write(final_output)
    #Displaying the output to the user
    cv2.imshow("magic", final_output)
    cv2.waitKey(1)
    
