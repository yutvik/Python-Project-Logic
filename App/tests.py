from django.test import TestCase
import csv
import jinja2
import pdfkit
from datetime import datetime
# Create your tests here.

# How to use in csv
# f = open(r"C:\Users\DELL\Downloads\1,2,3,4.csv","r")
# ro = csv.reader(f,delimiter = ",") #f file open/delimiter commaseprated mate
# ld = list(ro)#[["1", "2", "3", "4"], ["5", "6", "7", "8"], ["a", "b", "c", "d"]]
# ld = tuple(ro)#(["1", "2", "3", "4"], ["5", "6", "7", "8"], ["a", "b", "c", "d"])

# for row in ld:   #this type use  output
# ['1', '2', '3', '4']
# ['5', '6', '7', '8']
# ['a', 'b', 'c', 'd']
#   print(row)

# f.close()

my_name = "Yutvik Savani"
item1 = "TV"
item2 = "Couch"
item3 = "Washing Machine"
today_date = datetime.today().strftime("%d ,%b,%Y")

context = {'my_name':my_name,'item1':item1,'item2':item2,'item3':item3,'today_date':today_date}

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template=template_env.get_template('pdf.html')
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf=r"C:\Users\DELL\Desktop\New folder (2)")
pdfkit.from_string(output_text, 'pdf_generated.pdf', configuration=config)





