import smtplib

from email.mime.text import MIMEText
msg=MIMEText("Contenido de correo")

msg['subject']='Asunto del correo'
msg['From']='desdedonde@gmail.com'
msg['To']='haciadonde@gmail.com'

mailServer=smtplib.SMTP('smtp.gmail.com','587')
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('victormanuelap@gmail.com','xxxxxxxxxx')
mailServer.sendmail('victormanuelap@gmail.com','victormanuelap@gmail.com',msg_as_string())

mailServer.close()