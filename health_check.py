#!/usr/bin/env python3

#Script monitors CPU usage, disk space, available memory and name resolution. 
#Emails in case of any problems 

import shutil 
import psutil 
import socket 
import os 
import emails
def health_check():   
  """Checks for the CPU usage, disk space, available memory, and name resolution. 
  Emails in case of abnomalities""" 

  cpu_percent = psutil.cpu_percent(interval = 1) 
  disk_usage = psutil.disk_usage('/').percent
  mem = psutil.virtual_memory().free 
  mem_MB = mem/(1024*1024)
  looback = socket.gethostbyname('localhost')
  user = os.environ.get('USER')

  sender = 'automation@example.com' 
  receiver = user+'@example.com'
  body = 'Please check your system and resolve the issue as soon as possible'
#Report an error if CPU usage is over 80%
  if cpu_percent > 80: 
    subject = 'Error - CPU usage is over 80%'
    print(subject) 
    message = emails.generate_error_report( sender, receiver, subject, body)
    emails.send_email(message)
#Report an error if available disk space is lower than 20%
  elif disk_usage < 20: 
    subject ='Error - Available disk space is less than 20%'
    message = emails.generate_error_report( sender, receiver, subject, body)
    emails.send_email(message)
#Report an error if available memory is less than 500MB
  elif mem_MB < 500: 
    subject = 'Error - Available memory is less than 500MB'
    message = emails.generate_error_report( sender, receiver, subject, body)
    emails.send_email(message)
#Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
  elif loopback != '127.0.0.1': 
    subject = 'Error - localhost cannot be resolved to 127.0.0.1'
    message = emails.generate_error_report( sender, receiver, subject, body)
    emails.send_email(message) 
  return  


if __name__ == "__main__": 
  health_check()




