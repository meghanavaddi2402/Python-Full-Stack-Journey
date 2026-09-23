'''
simple mail automation
mail otp
mail with subjrect attachments
bulk mail
'''
'''
#SIMPLE MAIL AUTOMATION
#SMTP
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#START CONNECTION
server.starttls()
#LOGIN
server.login("meghanavaddi2402@gmail.com","zzuk yxdn oidu htkl")
msg = "Hello,Yemi chestunavu...???tinava..???"
server.sendmail("meghanavaddi2402@gmail.com","meenav1143@gmail.com",msg)
#CLOSE CONNECTION
server.quit()
print("Mail sent")

#SENDING OTP To MAIL
import math
import random
import smtplib
#OTP GENERATION
otp = random.randint(1000,9999)
print(otp)
"""
digits = '1234567890'
otp = ""
for i in range(6):
    otp += digits[math.floor(random.random()*10)]
    print(otp)"""
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#START CONNECTION
server.starttls()
#LOGIN
server.login("meghanavaddi2402@gmail.com","zzuk yxdn oidu htkl")
msg = f"your OTP is {otp}"
server.sendmail("meghanavaddi2402@gmail.com","meenav1143@gmail.com",msg)
#OTP VALIDATION
your_otp = int(input("Enter your otp: "))
if otp == your_otp:
        print("You entered opt is verifed\nYou can proceed")
else:
    print("Check your otp\nYou entered wrong otp!!!")

#CLOSE CONNECTION
server.quit()
print("Mail sent")

'''
