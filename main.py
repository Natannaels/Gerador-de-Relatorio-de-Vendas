import relatorio
import enviar_email

faturamento, quantidade_vendas, ticket_medio = relatorio.gerar_relatorio()

conteudo = f"""Subject: Relatório de Vendas por Loja

    Prezados,

    Segue o relatório de vendas por cada Loja.

    Faturamento:
    {faturamento}

    Quantidade Vendida:
    {quantidade_vendas}

    Ticket Médio dos Produtos:
    {ticket_medio}

    Att., 

    Ghiblicat
    """

enviar_email.enviar_email(conteudo)