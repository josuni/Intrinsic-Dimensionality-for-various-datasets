#https://stackoverflow.com/a/66641176
import sys
import glob
import h5py
import cv2

IMG_WIDTH = 300
IMG_HEIGHT = 300

h5file = 'example_train.h5'

#count number of files
nfiles = len(glob.glob('dataset/cats-vs-rabbits/train-cat-rabbit/cat/*.jpg'))
print(nfiles)

# resize all images and load into a single dataset
with h5py.File(h5file,'w') as  h5f:
    img_ds = h5f.create_dataset('images',shape=(nfiles, IMG_WIDTH, IMG_HEIGHT,3), dtype=int)
    for cnt, ifile in enumerate(glob.iglob('./*.ppm')) :
        img = cv2.imread(ifile, cv2.IMREAD_COLOR)
        # or use cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED
        img_resize = cv2.resize( img, (IMG_WIDTH, IMG_HEIGHT) )
        img_ds[cnt:cnt+1:,:,:] = img_resize
