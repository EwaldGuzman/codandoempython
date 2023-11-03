import smtplib

import base64
import mimetypes

from email.message import EmailMessage

mime_message = EmailMessage()

# headers
mime_message['To'] = 'lucaspietro.023@gmail.com'
mime_message['From'] = 'evaldogusmaocosta@gmail.com'
mime_message['Subject'] = 'sample with attachment'

# text
mime_message.set_content(
    'Hi, this is automated mail with attachment.'
    'Please do not reply.'
)

# attachment
attachment_filename = r'Tabelas_xlsx/Cadastros_xlsx/Cadastro de Consultas.xlsx'
# guessing the MIME type
type_subtype, _ = mimetypes.guess_type(attachment_filename)
maintype, subtype = type_subtype.split('/')

with open(attachment_filename, 'rb') as fp:
    attachment_data = fp.read()
mime_message.add_attachment(attachment_data, maintype, subtype)

encoded_message = base64.urlsafe_b64encode(mime_message.as_bytes()).decode()

create_draft_request_body = {
            'message': {
                'raw': encoded_message
            }
}


senha = 'pfnxzjiaaxmtdfby'


s = smtplib.SMTP('smtp.gmail.com: 587')
s.ehlo()
s.starttls()
s.login(mime_message['From'], senha)
s.sendmail(mime_message['From'], mime_message['To'], mime_message.as_string())
s.quit()
