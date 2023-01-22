import cv2
import numpy as np

matriz = np.array([[7,6,5,5,6,7],[6,4,3,3,4,6],[5,3,2,2,3,5],[5,3,2,2,3,5],[6,4,3,3,4,6],[7,6,5,5,6,7]])
alfa = 0
kernel = np.array([[-alfa,alfa-1,-alfa],[alfa-1, alfa+5, alfa-1],[-alfa, alfa-1, -alfa]]) * (1/(alfa+1))
m, n = matriz.shape

flip = np.array([['a','b','c'],['d','e','f'],['g','h','i']])
print(flip)
flip = np.flip(flip)
print(flip)
matriz2 = np.zeros([m+2,n+2])
img_new = np.zeros([m, n])
kernerl_size = 3
k = int(kernerl_size/2)
temp = np.zeros([kernerl_size, kernerl_size])
for i in range(0, m):
    for j in range(0, n):
        matriz2[i+1,j+1] = matriz[i,j]
print(matriz2)
for i in range(k, m-k):
    for j in range(k, n-k):
        for l in range (0,kernerl_size):
            for c in range(0,kernerl_size):
                temp[l,c] = matriz[i-k+l, j-k+c]*kernel[l,c]
        soma=np.sum(temp)
        img_new[i, j]= soma
print(img_new)
# k = 5
# for a in range(-k,k):
#     print(a)
    
# s = 3/2
# print(int(s))
# matriz = np.array([[1,2,3],[4,5,6]])
# print(np.sum(matriz))
# temp = np.zeros([3, 3])  
# for l in range (0,3):
#     for c in range(0,3):
#         temp[l][c] = c
    
    
# print(np.mean(np.sort(temp, axis =None)))