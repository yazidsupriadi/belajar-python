import cv2
import numpy as np

#Get Image
# img = cv2.imread('img/dog.jpg')
img = cv2.imread('img/dog.jpcg', cv2.IMREAD_GRAYSCALE)

#Show Image
cv2.imshow('sample image',img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

#Convert Image To Matrix
img_matrix = np.asarray(img)
print img_matrix

#Save Matrix to File

#Negative
img_matrix_neg = 255-img_matrix
print img_matrix_neg
cv2.imshow("Negative Image",img_matrix_neg)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

#Contrast Stretching
min = np.min(img_matrix)
max = np.max(img_matrix)
a = min
b = 255 / (max-min)
img_matrix_cs = (img_matrix - a) * b
cv2.imshow("Contrast Streched Image",img_matrix_cs)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

#Histogram Equilization
equ_img = cv2.equalizeHist(img)
equ_img_matrix = np.asarray(equ_img)
cv2.imshow("Histeq Image",equ_img_matrix)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

#Normalized Image
norm_img_matrix = img_matrix.astype(float)/255
print norm_img_matrix

#Convolution
# kernel = np.array([[1.0,0.0,-1.0],
#                     [2.0,0.0,-2.0],
#                     [1.0,0.0,-1.0]])
# kernel = np.array([[1.0,1.0,1.0],
#                     [1.0,1.0,1.0],
#                     [1.0,1.0,1.0]])
# kernel = kernel / 9
kernel = np.ones((7,7), dtype=float)
kernel = kernel / 49

m, n = kernel.shape
y, x = norm_img_matrix.shape
y = y - m + 1
x = x - m + 1
res_img = np.zeros((y,x))
for i in range(y):
    for j in range(x):
        res_img[i][j] = np.sum(norm_img_matrix[i:i+m, j:j+m]*kernel)

cv2.imshow("Convolved Image",res_img)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image