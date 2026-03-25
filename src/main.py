from relatorio import gerar_relatorio
from enviar_email import enviar_email

faturamento, quantidade_vendas, ticket_medio = gerar_relatorio()

assunto = 'Relatório automatico teste'
remetente = 'remetente@gmail.com'
senha = 'Senha de APP'
destinatarios = ['destinatario@gmail.com']

conteudo = f"""

    <p>Prezados,</p>

    <p>Segue o relatório de vendas por cada Loja.</p>

    <p>Faturamento:</p>
    {faturamento.to_html()}

    <p>Quantidade Vendida:</p>
    {quantidade_vendas.to_html()}

    <p>Ticket Médio dos Produtos:</p>
    {ticket_medio.to_html()}

    <p>Att.,</p>

    <p>Ghiblicat</p>
    """

enviar_email(conteudo, assunto, remetente, senha, destinatarios)