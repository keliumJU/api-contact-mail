import smtplib
from src import app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you holaaa"
 
# setup the parameters of the message
password = "3124075194JM26"
msg['From'] = "edison.jm26@gmail.com"
msg['To'] = "josment123jf@gmail.com"
msg['Subject'] = "Subscription"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
#server = smtplib.SMTP('smtp.gmail.com: 587')
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.ehlo()
server.starttls()

# Login Credentials for sending the mail
server.login('exilesoft.servico@gmail.com', 'oixzbucncdukgjio') 
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s:" % (msg['To']))



@app.route('/')
def hello():
    return 'Hello, World!'

print('Hello, World!')