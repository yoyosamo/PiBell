#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

#Put the message that you want to be put into the terminal when the code is started (when the bell is rung) between the " and " below
print "[PiBell] Ding, Dong!!! Doorbell rung."

USERNAME = "<Put the username (email address) of YOUR *Gmail* (HAS to be Gmail) account here>"
PASSWORD = "<Put the password of YOUR Gmail account here>"
To1 = "<Put the recipient address here>"

#Put the message between the ' and ' on the next line
msg = MIMEText('The doorbell has been rung!' + '\nRung at ' + now.strftime("%H:%M") + ' on ' + now.strftime("%d/%m/%Y") + '\n  ' + '\n--' + '\nSent via PiBell - Made by Sam Smith')

#Put what you want the email's subject line to be between the ' and ' on the next line
msg['Subject'] = '[PiBell] Ding, Dong!'

msg['From'] = USERNAME
msg['To'] = To1

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo_or_helo_if_needed()
server.starttls()
server.ehlo_or_helo_if_needed()
server.login(USERNAME,PASSWORD)
server.sendmail(USERNAME, To1, msg.as_string())
server.quit()

#Put the message that you want to be put into the terminal AFTER the email is sent between the " and " below (Currently says the recipient and the time/date)
print "[PiBell] Email notification sent to " + To1 + " at " + now.strftime("%d/%m/%Y %H:%M")
