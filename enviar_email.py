import smtplib 

# Utilização de SMTP (Simple Mail Transfer Protocol)
def enviar_email(content):

    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()

    # Utilizei a senha de APP gerada pelo Google(não a senha normal)
    servidor_email.login('remetente@gmail.com', 'Senha de APP')

    remetente = 'remetente@gmail.com'
    destinatarios = ['destinatario@gmail.com']

    conteudo = content.encode('utf-8')

    servidor_email.sendmail(remetente, destinatarios, conteudo)

    servidor_email.quit()

    print("Email enviado!")
