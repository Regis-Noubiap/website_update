# website_update
System updates the catalog information with data provided by suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images are converted to smaller jpeg images and the text is turned into an HTML file that shows the image and the product description. 

The contents of the HTML file is then uploaded to a web service that is already running using Django. System also analyzes the .txt files and use a Python request to upload it to your Django server.  Scripts also process the images and descriptions and then update your company's online website to add the new products.  Once the task is complete, the supplier is the notified with an email containing details of data analysis. 

The email contains a PDF attachment with the name of the fruit and its total weight (in lbs).  

Finally, in parallel to the automation running, the health of the system is monitored - any abnormalities is reported by email.
