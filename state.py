import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from time import gmtime, strftime
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d')
date


email_user = 'nitingupta.du2@gmail.com'
email_password = '#########'
email_send = 'nitin5266@gmail.com'

subject = 'Dark AI'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hello world'
msg.attach(MIMEText(body,'plain'))

filename= date + "_State.csv"
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)

text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()