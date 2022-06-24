import numpy as np
import matplotlib.pyplot as plt
import h5py
import imageio

train_h5 = h5py.File('example_train.h5', 'r')
print(list(train_h5.keys()))

images = train_h5['images']
labels = train_h5['labels']
print(images.shape)
print(labels.shape)

print(labels[0:6]) #shows labels

for i in range(6):
    imdata = np.array(images[i][:,:,:])
    imfile = 'test' + str(i) + '.jpg'
    imageio.imwrite(imfile, imdata)
# https://stackoverflow.com/a/52691552
