from mnist import MNIST

mndata = MNIST('MNIST dataset')
images,labels = mndata.load_training()

average_list_0 = []
average_list_1 = []

for i in range(len(images)):
    if labels[i] == 0:
        average_list_0.append(images[i])
    elif labels[i] == 1:
        average_list_1.append(images[i])