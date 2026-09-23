'''
in this case we need to add subject and to address fro mail
we will use email package
'''
import email
import smtplib
#MIME => MultiPurpose Internet Mail Extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#PROVIDING DETAILS
from_addr = "meghanavaddi2402@gmail.com"
to_addr = "meenav1143@gmail.com"
subject = "Nekosameee........."
#CHECKING DETAILS AND THROWING TO MULTIPART
msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = from_addr
msg['To'] = to_addr
msg['subject'] = subject
msg['body'] = "neke mail peta.....sosukoooo....."
msg.attach(MIMEText(msg['body'], "plain"))
server = smtplib.SMTP('smtp.gmail.com',587)
#START CONNECTION
server.starttls()
#LOGIN
server.login(from_addr,"zzuk yxdn oidu htkl")
server.sendmail(from_addr,to_addr,msg.as_string())
#CLOSE CONNECTION
server.quit()
print("Mail sent")
