import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = os.getenv("smtp_server")
smtp_port = os.getenv("smtp_port")
smtp_username = os.getenv("smtp_username")
smtp_password = os.getenv("smtp_password")
contacts = os.getenv("contacts")
cc_contacts = os.getenv("cc_contacts")

body = os.getenv("body")

with open(body, 'r') as file:
    for line in file:
        line = line.strip()
        msg_fix = 'DIGITE AQUI SUA MENSAGEM FIXA: \n\n - {} \n\nAtenciosamente, \n NOME'.format(line)

        # Cria uma conexão com o servidor SMTP do Gmail
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = contacts
        msg['Cc'] = cc_contacts
        msg['Subject'] = line
        msg.attach(MIMEText(msg_fix, 'plain'))

        # Envia o e-mail
        server.sendmail(smtp_username, contacts, msg.as_string())

        # Finaliza a conexão
        server.quit()

        time.sleep(5)
