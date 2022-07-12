#Mail Service 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_message(from_admin, list_users_mail, subject, my_msg,key_sr):

	s = smtplib.SMTP('smtp.gmail.com')
	s.set_debuglevel(1)
	msg = MIMEText(my_msg)
	sender = from_admin

	recipients = list_users_mail 
	msg['Subject'] = subject 
	msg['From'] = sender
	msg['To'] = ", ".join(recipients)

	s.login(from_admin, key_sr) 
	s.sendmail(sender, recipients, msg.as_string())

	s.quit()
	



