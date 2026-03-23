import pandas as pd #precisa do openpyxl para abrir arquivos excel

# importar a base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')


# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas[['ID Loja', 'Valor Final']])


# faturamento por loja
#tabela_vendas.groupby('ID Loja').sum()
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# quantidade de produtos vendidos por loja
quantidade_vendas = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade_vendas)

print("#" * 50)
# ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade_vendas['Quantidade']).round(2).to_frame()
print(ticket_medio)

# enviar relatório em email
