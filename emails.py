
#!/usr/bin/env python3

from email.message import EmailMessage
import mimetypes 
import os.path
import smtplib
def generate_email(sender, receiver,subject, body,attachment): 
  """Generates a message with an attachement"""
  message = EmailMessage() 
  message['From'] = sender 
  message['To'] = receiver 
  message['Subject'] = subject 
  message.set_content(body)
  
  file = os.path.basename(attachment)
  mime_types,_ = mimetypes.guess_type(file) 
  mime_type,mime_subtype = mime_types.split('/',1)

  with open(attachment,'rb') as att: 
    message.add_attachment(att.read(),maintype = mime_type, subtype =mime_subtype,
    filename = file)
  return message 

def generate_error_report(sender, receiver,subject, body):
  """Generates a message without any attachement"""  
  message = EmailMessage() 
  message['From'] = sender 
  message['To'] = receiver 
  message['Subject'] = subject 
  message.set_content(body)
  return message


def send_email(message):
  """Sends the email"""
  mailserver = smtplib.SMTP('localhost')
  mailserver.send_message(message)
  mailserver.set_debuglevel(1)
  mailserver.quit()


if __name__ == "__main__": 
  generate_email(sender, receiver,subject, body,attachment)
  send_email() 

