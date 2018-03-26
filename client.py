# client.py

import socket                   

import cv2
import numpy as np

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
host = '192.168.1.116'   
port = 5000                   
 
s.connect((host, port))
print('connect')

f = open( "1.png",'wb')
while True:
	data = s.recv(1024)
	if not data:
		break
	# write data to a file
	f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')


print('read img done')
img = cv2.imread('1.png')
Threshold=150

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

height = img.shape[0]
width = img.shape[1]


newImg = gray.copy()


gx=[[-1,0,1],[-2,0,2],[-1,0,1]]
gy=[[-1,-2,-1],[0,0,0],[1,2,1]]


print('start sobel')


for h in range(0,height):
    for w in range(0,width):
            
        sobelx=0
        sobely=0
		
        for j in range(0,3):
            for i in range(0,3):
                sobelx=sobelx+gray[h+j-2][w+i-2]*gx[j][i]
                sobely=sobely+gray[h+j-2][w+i-2]*gy[j][i]
                
         
        sobel= (sobelx**2+sobely**2)**0.5
           
		
		
        if sobel>Threshold:
            newImg.itemset((h, w), 255)
        else:
            newImg.itemset((h, w), 0)
        
          
cv2.imwrite('1_sobel.png',newImg)   
        
print('sobel done')
        



