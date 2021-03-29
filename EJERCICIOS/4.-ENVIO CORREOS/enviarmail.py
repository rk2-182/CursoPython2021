"""
tutorial: https://www.youtube.com/watch?v=W0dsYcSELzM
"""
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP

mensaje = MIMEMultipart("plain")
mensaje["From"] = "ricardoplus@live.cl"
mensaje["To"] = "ricardoplus@live.cl"
mensaje["Subject"] = "Correo de pruena python 3x"

adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open("archivo.txt","rb").read()) #Archivo adjunto
adjunto.add_header("content-Disposition", "attachment; filename=mensaje.txt")
mensaje.attach(adjunto)

#correo tipo outlook
smtp = SMTP("smtp.live.com")
smtp.starttls()

#Logear
smtp.login("ricardoplus@live.cl","negrokuzey182")
smtp.sendmail("ricardoplus@live.cl","ricardoplus@live.cl",mensaje.as_bytes())
smtp.quit()