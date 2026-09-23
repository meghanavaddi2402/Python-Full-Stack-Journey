'''
Adding an attachement along with subject to send mail
'''
import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase #Loading attachment as header file
from email import encoders #encode the file into binary file formate
#PROVIDING DETAILS
from_addr = "meghanavaddi2402@gmail.com"
to_addr = "meenav1143@gmail.com"
subject = "PYTHON FULLSTACK TRAINING"
body = "Hello,\nMs.Meenakshi,\nYour PYTHON FULL STACAK TRAINING starts from 21sept2026 so,please make sure your are present\n\nRegards,\nMEGHANA VADDI"
attach = "subj_mail.py"
#CHECKING DETAILS AND THROWING TO MULTIPART
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['subject'] = subject
msg.attach(MIMEText(body))
part = MIMEBase('application','octet-stream')
print(part)
part.set_payload(open(attach).read())
encoders.encode_base64(part)
#ADDING HEADER TO FILENAME
part.add_header("Content-Disposition",f"attachment; filename = {os.path.basename(attach)}")
msg.attach(part)
#CONVER THIS TO STRING
text = msg.as_string()
#INCLUDING smptlib CODE
server = smtplib.SMTP('smtp.gmail.com',587)
#START CONNECTION
server.starttls()
#LOGIN
server.login(from_addr,"zzuk yxdn oidu htkl")
server.sendmail(from_addr,to_addr,msg.as_string())
#CLOSE CONNECTION
server.quit()
print("Mail sent")
