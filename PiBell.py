#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()
config = open('PiBell.config').readlines()

print "[PiBell] Ding, Dong!!! Doorbell rung."

"""
*!!!*!!!*!!!* 
NOTE!!!
 To edit the details (Username, Password and Recipient),
 edit the 'PiBell.config' file

 To edit the file, open LXTerminal and type 'leafpad PiBell.config'
*!!!*!!!*!!!*
"""


USERNAME = config[1].strip()
PASSWORD = config[4].strip()
RECIPIENT = config[7].strip()


msg = MIMEText('The doorbell has been rung!' + '\nRung at ' + now.strftime("%H:%M") + ' on ' + now.strftime("%d/%m/%Y") + '\n  ' + '\n--' + '\nSent via PiBell - Made by Sam Smith')
msg['Subject'] = '[PiBell] Ding, Dong!'
msg['From'] = USERNAME
msg['To'] = RECIPIENT

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo_or_helo_if_needed()
server.starttls()
server.ehlo_or_helo_if_needed()
server.login(USERNAME,PASSWORD)
server.sendmail(USERNAME, RECIPIENT, msg.as_string())
server.quit()

print "[PiBell] Email notification sent to " + RECIPIENT + " at " + now.strftime("%d/%m/%Y %H:%M")
