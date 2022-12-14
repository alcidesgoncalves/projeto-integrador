import os
import smtplib
from email.message import EmailMessage
from secret import senha

#Configuração do email

EMAIL_ADRESS = 'caflo.2021114tads18@aluno.ifpi.edu.br'
EMAIL_PASSWORD = senha 

#CRIAÇÃO
msg = EmailMessage()
msg['Subject'] = 'Lembrete de revisão de flashcards'
msg['From'] = 'caflo.2021114tads18@aluno.ifpi.edu.br'
msg['To'] = 'bmalcidesneto@gmail.com'
msg.set_content('Revise seus flashcards imediatamente')

#ENVIO
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)


