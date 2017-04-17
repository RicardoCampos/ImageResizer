#!/usr/bin/python

from PIL import Image
import sys
import os

def createThumbnailDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def resizeImage( infile, out_directory, sizeFactor ):
    print("Resizing "+infile)
    filename = os.path.splitext(os.path.basename(infile))[0] + "_thumb.jpeg"
    outfile = os.path.join(out_directory,filename)
    if infile != outfile:
        try:
            img = Image.open(infile)
            xsize, ysize = img.size
            if ( (xsize < 1) or (ysize < 1) ):
                return
            xsize = xsize * sizeFactor
            ysize = ysize * sizeFactor
            new_size = xsize, ysize
            #print(new_size)
            img.thumbnail(new_size)
            img.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for", infile)

def resizeImagesInDirectory( in_directory, out_directory, sizeFactor ):
    for file in os.listdir(in_directory):
        if (file.endswith(".jpg") or file.endswith(".jpeg")):
            resizeImage(os.path.join(in_directory,file), out_directory, sizeFactor)

print("Resizing images.")
resize_directory = "web_resized"
my_directory  = os.getcwd()
output_directory = os.path.join(my_directory, resize_directory)

createThumbnailDirectory(output_directory)
resizeImagesInDirectory ( my_directory,output_directory,0.5 )
print("Finished resizing images.")
