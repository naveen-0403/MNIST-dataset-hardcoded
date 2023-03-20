from mnist import MNIST
import numpy as np

mndata = MNIST('MNIST dataset')
images,labels = mndata.load_training()

# index = 0

arr1=[]

# for i in range(len(images)):
#     for j in range(len(images[i])):
#         if images[i][j]==0:
#             images[i][j]=" "
#         elif images[i][j] >0 and images[i][j]< 256:
#             images[i][j]="x"

# def print_image(index):
#     image = images[index]
#     for i in range(len(image)):
#         if image[i]==0:
#             image[i]=" "
#         else:
#             image[i]="W"

#     for i in range(0,28):
#         print(image[i*28:(i+1)*28])    
#     print(labels[index])
# print_image(23)

avglist0 = []
avglist1 = []
for i in range(len(images)):
    if labels[i] == 0:
        avglist0.append(images[i])
    elif labels[i] == 1:
        avglist1.append(images[i])

# print(len(avglist0),len(avglist1))

N = 100
newlist = []
for index in range(0, N):
    newlist.append(avglist0[index])
# print(len(newlist))

# print(avglist0)
# print(newlist)

# print (newlist[23])

avg0 = [0]*784
for i in range(len(avglist0)):
    for j in range(0,784):
        avg0[j] += avglist0[i][j]

for j in range(0,784):
    avg0[j]=avg0[j]/len(avglist0)
# print(avg0)

avg1 = [0]*784
for i in range(len(avglist1)):
    for j in range(0,784):
        avg1[j] += avglist1[i][j]

for j in range(0,784):
    avg1[j]=avg1[j]/len(avglist1)
# print(avg1)

for i in range(len(avg0)):
    if avg0[i]==0:
        avg0[i]=" "
    elif avg0[i]>0 and avg0[i]< 256:
        avg0[i]="W"
for i in range(0,28):
    print(avg0[i*28:(i+1)*28])

# for i in range(len(avg1)):
#     if avg1[i]==0:
#         avg1[i]=" "
#     elif avg1[i] >0 and avg1[i]< 256:
#         avg1[i]="W"
# for i in range(0,28):
#     print(avg1[i*28:(i+1)*28]) 

# for j in range(0,28):
#     print(images[index][j*28:(j+1)*28])    
# print(labels[index])