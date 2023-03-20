from mnist import MNIST
import numpy as np
mndata = MNIST('MNIST dataset')
images,labels = mndata.load_training()
test_image,test_labels = mndata.load_testing()

def diff(img1,img2):
    diff=0
    for i in range(0,784):
        diff+=abs(img1[i]-img2[i])
    return diff/784

accptcrt = [0]*10
average_images = [[0]*784]*10
count = [0]*10

for i in range(len(images)):
    for j in range(784):
        average_images[labels[i]][j]+=images[i][j]
        count[labels[i]]+=1
for i in range(len(average_images)):
    for index in range(784):
        average_images[i][index]=average_images[i][index]/count[i]
# print(average_images)

for i in range(len(images)):
    distance=0
    for average_image in average_images:
        distance+=diff(average_image,images[i])
    distance /=10
    accptcrt[labels[i]]+=distance
for i in range(len(accptcrt)):
    accptcrt[i]/=count[i]
print(accptcrt)