import cv2
import numpy as np

window_name = "Checking Box"

def boxDrawing(img,start_point,end_point):
	color = (0,0,255) # BGR
	thickness = 3 #px
	new_img = cv2.rectangle(img,start_point,end_point,color,thickness)
	
	return new_img

def resizing(img,width,height):
	new_size = (width,height)
	new_img = cv2.resize(img,new_size,interpolation = cv2.INTER_AREA)

	return new_img

def cropping(img,topLeft_x,topLeft_y,width,height):
	crop_img = img[topLeft_y:topLeft_y+height,topLeft_x:topLeft_x+width]
	
	return crop_img
	
def main():
	img = cv2.imread("./images/IMAGE5.png",1)
	height,width,channels = img.shape
	dimensions = (height,width,channels)

	#Box Drawing for visual inspection
	start_point = (75,75) #Top Left Corner
	end_point = (75+269,75+267) #Bottom Right Corner
	#new_img = boxDrawing(img,start_point,end_point)

	#Cropping Image
	new_img = cropping(img,100,340,width-190,int(height/2)-200)
		
	#Resizing Image
	new_width = 269
	new_height = 267
	new_img2 = resizing(new_img,new_width,new_height)

	#Displaying Image
	cv2.imshow(window_name,new_img)
	cv2.waitKey(0)

	#Writing the new image
	cv2.imwrite("./images/gauge-5.jpg",new_img)
	

if __name__=='__main__':
    main()

