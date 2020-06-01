#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image 
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(attachment, title, paragraph): 
  """Generates a report with attachement being the path/file.ext, title 
  being a string value of the report title, and paragraph a list of dictionaries 
  to be parsed"""
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(attachment)
  report_title = Paragraph(title,styles['h1'])
  table_data = []
  for fruit in paragraph: 
    name = fruit['name']
    weight = fruit['weight']
    table_data.append(['name: {}'.format(name)])
    table_data.append(['weight: {} lbs'.format(weight)])
  print(table_data)
  report_table = Table(data = table_data)
  report.build([report_title,report_table]) 
  return 
if __name__ == "__main__": 
  generate_report(attachment, title, paragraph)


