import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Enviar_Email(destinatario, assunto, corpo, anexo, arquivo):

    host = 'smtp.gmail.com'
    port = 587
    login = 'evaldogusmaocosta@gmail.com'
    destintario_email = destinatario
    senha = 'pfnxzjiaaxmtdfby'

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(login, senha)

    msg = MIMEMultipart()
    msg['from'] = login
    msg['to'] = destintario_email
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    anexo_email = anexo
    attachment = open(anexo_email, 'rb')

    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)

    att.add_header('Content-Disposition', f'attachment; filename={arquivo}')
    attachment.close()
    msg.attach(att)


    server.sendmail(login, destintario_email, msg.as_string())
    server.quit()
