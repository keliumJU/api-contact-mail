import smtplib
from flask import jsonify,request
from src import app
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from src.config.db import connection


# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you holaaa"
 
# setup the parameters of the message

msg['From'] = ""
msg['To'] = ""
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
#server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
#print("successfully sent email to %s:" % (msg['To']))



@app.route('/api/v1/correo', methods=['POST'])
def crearCorreo():
    #request_data = request.get_json()
    correo = request.json['correo']
    print(correo)
    cursor = connection.cursor()
    print(correo)
    cursor.execute('INSERT INTO Correo(Correo) values (%s,)',(correo))
    connection.commit()
    response = {'message': 'success'}
    return jsonify(response)


@app.route('/')
def hello():
    return 'Hello, World!'

print('Hello, World!')