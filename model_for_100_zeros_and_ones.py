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

newlist0 = []
for index in range(0, N):
    newlist0.append(avglist0[index])

newlist1 = []
for index in range(0, N):
    newlist1.append(avglist1[index])
# print(len(newlist))

# print(avglist0)
# print(newlist)

# print (newlist[23])

avg0 = [0]*784
for i in range(len(newlist0)):
    for j in range(0,784):
        avg0[j] += newlist0[i][j]

for j in range(0,784):
    avg0[j]=avg0[j]/len(newlist0)
# print(avg0)

avg1 = [0]*784
for i in range(len(newlist1)):
    for j in range(0,784):
        avg1[j] += newlist1[i][j]

for j in range(0,784):
    avg1[j]=avg1[j]/len(newlist1)
# print(avg1)

# for i in range(len(avg0)):
#     if avg0[i]==0:
#         avg0[i]=" "
#     elif avg0[i]>0 and avg0[i]< 256:
#         avg0[i]="W"
# for i in range(0,28):
    # print(avg0[i*28:(i+1)*28])  
  
# print ("\n")

# for i in range(len(avg1)):
#     if avg1[i]==0:
#         avg1[i]=" "
#     elif avg1[i] >0 and avg1[i]< 256:
#         avg1[i]="W"
# for i in range(0,28):
    # print(avg1[i*28:(i+1)*28])

def diff (img1,img2):
    diff = 0
    for i in range(0,784):
        diff += abs(img1[i] - img2[i])
    return diff/784
# print(diff(newlist0[0],avg0))
# print(diff(newlist0[0],avg1))


        #on bench {for i in range(len(newlist0)):
        #     newarr0 += diff(newlist0[i],avg0)
        # criteria0 = (newarr0/len(newlist0))
        # print(criteria0)}

newarr0=0
for i in range(len(newlist0)):
    newarr0 += (diff(newlist0[i],avg0))
crt0_0 = newarr0/len(newlist0)
# print("crt newlist0(0)",crt0_0)

newarr1=0
for i in range(len(newlist0)):
    newarr1 += (diff(newlist0[i],avg0))
crt0_1 = newarr1/len(newlist0)
# print("crt newlist0(1)",crt0_1)

acrt_0 = (crt0_1 + crt0_0)/2
# print("acceptance criteria for 0 is = ",acrt_0,"\n")

arr_1=0
for i in range(len(newlist1)):
    arr_1 += (diff(newlist1[i],avg1))
crt_1 = arr_1/len(newlist1)
# print("crt newlist1(1)",crt_1)

arr_2=0
for i in range(len(newlist1)):
    arr_2 += (diff(newlist1[i],avg0))
crt_2 = arr_2/len(newlist1)
# print("crt newlist1(0)",crt_2)

acrt_1 = (crt_1+crt_2)/2
# print("acceptance criteria for 1 is = ",acrt_1)


mndata = MNIST('MNIST dataset')
testingimages,testinglabels = mndata.load_testing()
index = 0

testimages0 = diff(testingimages[index],avg0)
testimages1 = diff(testingimages[index],avg1)
# print(testimages0)
# print(testimages1)

correctmatch=0
incorrectmatch=0

for i in range(len(testingimages)):
    if diff(testingimages[i],avg0)<=acrt_0:
        if testinglabels[i]==0:
            correctmatch+=1
        else:
            incorrectmatch+=1

    elif diff(testingimages[i],avg1)<=acrt_1:
        if testinglabels[i]==1:
            correctmatch+=1
        else:
            incorrectmatch+=1
    else:
        incorrectmatch+=1

print(correctmatch)
print(incorrectmatch)

