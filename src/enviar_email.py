import smtplib 
from email.mime.text import MIMEText #permite envio de textos no formato html

# Utilização de SMTP (Simple Mail Transfer Protocol)
def enviar_email(conteudo, assunto, remetente, senha, destinatarios):

    servidor_email = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_email.starttls()

    # Utilizei a senha de APP gerada pelo Google(não a senha normal)
    servidor_email.login(remetente, senha)

    # remetente = 'remetente@gmail.com'
    # destinatarios = ['destinatario@discente.ufma.br']

    # conteudo = content.encode('utf-8')#o conteudo padrão sem formatação

    mensagem = MIMEText(conteudo, 'html')#transforma o conteudo da mensagem em html
    mensagem['Subject'] = assunto
    mensagem['From'] = remetente
    mensagem['To'] = ', '.join(destinatarios)
    
    servidor_email.sendmail(remetente, destinatarios, mensagem.as_string())

    servidor_email.quit()

    print("Email enviado!")
