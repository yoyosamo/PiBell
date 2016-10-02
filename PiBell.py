#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText

import datetime
now = datetime.datetime.now()

import os
import sys
import configobj
import traceback

print "[PiBell] Ding, Dong!!! Doorbell rung."

"""
 NOTE!!!
 To edit the details (Username, Password and Recipient),
 edit the 'PiBell.config' file

"""
try:
    file = os.path.expanduser('~/PiBell.config')
    config = configobj.ConfigObj(open(file).read().splitlines())
    USERNAME = config['config']['username']
    PASSWORD = config['config']['password']
    RECIPIENT = config['config']['recipient']
except:
#    traceback.print_exc()
#    oops = traceback.format_exc()
#    print(oops)

    print("""
                ****** SEVERE PIBELL ERROR!!! ******
[PiBell][ERROR] There is an issue with the config file! (Program stopped)
[PiBell][ERROR] Make sure that it is in the 'pi' ('home') directory
[PiBell][ERROR] Make sure that it is the latest version of the code
[PiBell][ERROR] The latest version is on GitHub (http://bit.ly/PiBell_Git/)
                ****** SEVERE PIBELL ERROR!!! ******
""")

    sys.exit(1)

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
