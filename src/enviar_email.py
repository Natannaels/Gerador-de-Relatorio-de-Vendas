import smtplib 
from email.mime.text import MIMEText #permite envio de textos no formato html

# Utilização de SMTP (Simple Mail Transfer Protocol)
def enviar_email(content):

    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()

    # Utilizei a senha de APP gerada pelo Google(não a senha normal)
    servidor_email.login('remetente@gmail.com', 'Senha de APP')

    remetente = 'remetente@gmail.com'
    destinatarios = ['destinatario@discente.ufma.br']

    # conteudo = content.encode('utf-8')#o conteudo padrão sem formatação

    conteudo = MIMEText(content, 'html')#transforma o conteudo da mensagem em html

    servidor_email.sendmail(remetente, destinatarios, conteudo.as_string())

    servidor_email.quit()

    print("Email enviado!")
