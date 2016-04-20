# ------------------------------------------------------------------------------------------
#                  Programa en Python para enviar correos con GMAIL
# ------------------------------------------------------------------------------------------
#
# Nota: Hay que habilitar el acceso de aplicaciones menos seguras en la siguiente direccion
#       https://www.google.com/settings/security/lesssecureapps
#
# ------------------------------------------------------------------------------------------

import getpass
import smtplib

def send_email(user, pwd, recipient, subject, body):
    
    gmail_user = user
    gmail_pwd = pwd
    
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Preparar el mensage
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print '[+] Correo Enviado correctamente'
    except:
        print "[!] Fallo al enviar el correo"


usuario         = raw_input("Introduzca el USUARIO de correo: ")
password        = getpass.getpass("Introduzca la CONTRASENA:")
destinatario    = raw_input("Introduzca DESTINATARIO: ")
asunto          = raw_input("Introduzca ASUNTO del mensaje: ")
mensaje         = raw_input("Introduzca el MENSAJE a enviar:")



send_email (usuario,password,destinatario,asunto,mensaje)
