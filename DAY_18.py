import smtplib
import ssl
from email.message import EmailMessage
sender_email = "your_email@gmail.com"
password =  "your_app_password"
receiver_mail = "vaddi1234YT@gmail.com"
message = EmailMessage()
message ["From"] =   "meghanavaddi2402@gmail.com"
message ["To"] =   "recipient@example.com"
message["Subject"] = "Welcome Mail"
message.set_content(f"""
Hello Meghana!!

Welcome to our python class

Regards,
Python Team
""")

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)
                                                                                                                                                                                        print("Functions_DAY12.py
