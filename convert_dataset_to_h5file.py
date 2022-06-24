#https://stackoverflow.com/a/66641176

import sys
import glob
import h5py
import cv2

IMG_WIDTH = 32
IMG_HEIGHT = 32

folder = sys.argv[1]
category1 = sys.argv[2]
category2 = sys.argv[3]

h5file = sys.argv[4]

#count number of files
nfiles = len(glob.glob(folder + '/*.jpg'))
print(nfiles)

# resize all images and load into a single dataset
with h5py.File(h5file,'w') as  h5f:
    img_ds = h5f.create_dataset('images',shape=(nfiles, IMG_WIDTH, IMG_HEIGHT,3), dtype=int)
    label_ds = h5f.create_dataset('labels', shape=nfiles, dtype=int)
    for cnt, filename in enumerate(glob.iglob(folder + '/*.jpg')) :
        img = cv2.imread(filename, cv2.IMREAD_COLOR)
        # or use cv2.IMREAD_GRAYSCALE, cv2.IMREAD_UNCHANGED
        img_resize = cv2.resize( img, (IMG_WIDTH, IMG_HEIGHT) )
        img_ds[cnt:cnt+1:,:,:] = img_resize
        filename = filename.removeprefix(folder)
        if category1 in filename:
            label_ds[cnt:] = 0
        if category2 in filename:
            label_ds[cnt:] = 1