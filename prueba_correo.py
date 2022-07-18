
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# Define to/from
sender = 'info@chursys.com'
sender_title = "NOTIFICACIÓN DE SERVICIO"
recipient = 'douglas.vasquezp@hotmail.com'

# Create message
msg = MIMEText("Message text", 'plain', 'utf-8')
msg['Subject'] =  Header("Sent from python", 'utf-8')
msg['From'] = formataddr((str(Header(sender_title, 'utf-8')), sender))
msg['To'] = recipient

# Create server object with SSL option
server = smtplib.SMTP_SSL('smtp.zoho.com', 465)

# Perform operations via server
server.login('info@chursys.com', 'Douglas1688*')
server.sendmail(sender, [recipient], msg.as_string())
server.quit()
server.close()