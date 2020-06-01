#!/usr/bin/env python3
import requests, os
# The Python Requests module

#this module uploads supplier image files to the web server 

user = os.environ.get('USER')

path = '/home/'+user+'/website_update/supplier-data/images/'

def upload(path): 
  for pic in os.listdir(path): 
    if pic.endswith('.jpeg'): 
      url = "http://localhost/upload/"
      with open(path+pic, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
  return 


if __name__ == '__main__': 
  upload(path)


