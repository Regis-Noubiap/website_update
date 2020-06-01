#!/usr/bin/env python3

#Script uses the emails and reports module to analyze data, generate a report
#and email it as an attachement 
from datetime import date 
import os 
import reports 

from datetime import date 
import emails 
sender = 'automation@example.com'
user = os.environ.get('USER')
#description_path = '/home/'+user+'/supplier-data/descriptions/'

receiver = user+'@example.com' 
subject = 'Upload Completed - Online Fruit Store' 
body = 'All fruits are uploaded to our website successfully. \nA detailed list is a$
attachment = '/tmp/processed.pdf'



today = date.today()
date = today.strftime('%B %d, %Y')

attachment = '/tmp/processed.pdf' 
title = 'Processed Update on {}'.format(date)
user = os.environ.get('USER')
description_path = '/home/'+user+'/website_update/supplier-data/descriptions/'

#Generate the list of dictionaries 
paragraph = []
for file in os.listdir(description_path):
  fruit = {} 
  with open(description_path+file,"r") as f: 
    fruit["name"] = f.readline().rstrip("\n")
    fruit["weight"] = int(f.readline().rstrip(" lbs\n"))
  paragraph.append(fruit)
#Uncomment below to see paragraph 
#print(paragraph)

#Generate and email report
reports.generate_report(attachment,title,paragraph)
message = emails.generate_email(sender, receiver,subject, body,attachment)
emails.send_email(message) 


