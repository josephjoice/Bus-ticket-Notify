import smtplib
import ConfigParser
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.utils import  formataddr
from email.header import  Header

Config=ConfigParser.ConfigParser()
Config.read("config.ini")

fromaddr =Config.get("gmail","email")
toaddr = Config.get("gmail","to")
msg = MIMEMultipart()
msg['From'] = formataddr((str(Header(u'Joseph Joice', 'utf-8')),fromaddr))
msg['To'] = toaddr
msg['Subject'] = "KSRTC seats available"
 
body = "Hi, joseph there are "+sys.argv[1]+" seats in the bus available."
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,Config.get("gmail","pass"))
text = msg.as_string()
server.sendmail(fromaddr, Config.get("gmail","to"), text)
server.quit()

