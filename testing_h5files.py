import numpy as np  
import matplotlib.pyplot as plt  
import h5py

train_h5 = h5py.File('dataset/mnist/train.h5', 'r')
print(list(train_h5.keys()))

images = train_h5['images']
labels = train_h5['labels']
print(images.shape)
print(labels.shape)

print(labels[0:12]) #shows labels

plt.subplots(3,4,figsize = (20,20))

for i in range(12):
    img_np = images[i]
    plt.subplot(3,4,1+i)
    plt.imshow(img_np)
plt.show() #shows correspoding images