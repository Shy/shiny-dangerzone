#!/usr/bin/python -tt

import smtplib
import string
 
SUBJECT = "Test email from Python"
TO = "john.opoku@dubtel.com"
FROM = "john.opoku@dubtel.com"
text = "blah blah blah"
BODY = string.join((
        "From: %s" % FROM,
        "To: %s" % TO,
        "Subject: %s" % SUBJECT ,
        "",
        text
        ), "\r\n")
server = smtplib.SMTP("email.dubtel.com")
server.sendmail(FROM, [TO], BODY)
server.quit()
