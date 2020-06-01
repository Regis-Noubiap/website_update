#!/usr/bin/env python3 
import os , sys 

from PIL import Image

#Path to images to be converted to JPEG 
user = os.environ.get('USER')
path = "/home/"+user+"/website_update/supplier-data/images/" 

#Uncomment the code below if you want to pass the pass as an argument
#path = sys.argv[1: ] 

def jpeg_conv(path):
  """This function converts files in path from 3000x2000 to 600x400 returns them as
  JPEG files""" 
  for pic in os.listdir(path): 
    if pic.endswith('.tiff'): 
      f,e = os.path.splitext(pic)
      new_file = f+'.jpeg'
      im = Image.open(path+pic)
      im_conv = im.convert("RGB")
      im_conv_r= im_conv.resize((600,400))
      im_conv_r.save(path+new_file)
  return 

if __name__ == '__main__': 
  jpeg_conv(path)

