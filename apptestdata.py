from mnist import MNIST
import numpy as np

mndata = MNIST('MNIST dataset')
testingimages,testinglabels = mndata.load_testing()
index = 0

def diff ():
    diff = 0

testimages0 = diff(testingimages[index],avg0)
testimages1 = diff(testingimages[index],avg1)
# print(testimages0)
# print(testimages1)

correct_match=0
incorrect_match=0

for i in range(len(testingimages)):
    if diff(testingimages[i],avg0)<=acrt_0:
        if testinglabels[i]==0:
            correct_match+=1
        else:
            incorrect_match+=1

    elif diff(testingimages[i],avg1)<=acrt_1:
        if testinglabels[i]==1:
            correct_match+=1
        else:
            incorrect_match+=1
    else:
        incorrect_match+=1

print(correct_match)
print(incorrect_match)