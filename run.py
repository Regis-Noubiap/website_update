#!/usr/bin/env python3

import requests, os, json

user = os.environ.get('USER')

path = "/home/"+user+"/website_update/supplier-data/descriptions/"
fruit = {}
data = []
def json_gen(path):
  """Produces a .json file containing fruit information"""
  for file in os.listdir(path): 
    print("opening {}".format(file))
    with open(path+file,"r") as f: 
      fruit["name"] = f.readline().rstrip("\n")
      fruit["weight"] = int(f.readline().rstrip(" lbs\n"))
      fruit["description"] = f.read().rstrip("\n")
    fruit["image_name"] = file.rstrip(".txt")+".jpeg" 
    url = "http://35.225.209.227/fruits/"
    r = requests.post(url,data=fruit)
    print(r)
    print(r.status_code)
    data.append(fruit)
  print(data)
  return data 


if __name__ == "__main__" : 
  json_gen(path)

