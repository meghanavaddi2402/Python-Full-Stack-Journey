'''import day4
print(dir(day4))#dir -> directory will return all avaliable methods,attributes
print(type(day4.employees))
print(type(day4.details))
day4.employees("meghana",batch=4,location="vizag")
print(day4.details.keys())
print(day4.details['location'])
day4.details.update({"organization":"Codegnan","batch_name":"PFS"})
print(day4.details)

#from keyword
from day4 import employees,details
details.update({"organization":"Codegnan","batch":"PFS-4"})
print(details)
print(day4.__doc__)
'''
#Built-in modules -> math,random,os,time,datetime
#we download modules from -> pypi(python package index)
#Building QR Scanner using python (LinkedIn URL)
#pyqrcode,png

import pyqrcode
import png
#creating QR Code by giving a link
link = "https://www.linkedin.com/in/meghana-vaddi-5902722a7/"
qr = pyqrcode.create(link)
#print(qr)
qr.png("mtqr.png",scale=10)
