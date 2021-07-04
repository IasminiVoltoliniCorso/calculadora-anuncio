from datetime import datetime

nomeAnuncio = str(input('Nome do anúncio: ')).title().strip()
cliente = str(input('Cliente: ')).title().strip()
dataInicio = datetime.strptime(input('Data de início (dd/mm/aaaa): '), '%d/%m/%Y')
dataTermino = datetime.strptime(input('Data de término (dd/mm/aaaa): '), '%d/%m/%Y')
periodoTotal = abs((dataTermino - dataInicio).days)
investimentoPorDia = float(input('Investimento por dia: R$ '))

valorTotalInvestido = periodoTotal * investimentoPorDia

visualizacoes = valorTotalInvestido * 30
cliques = visualizacoes * 0.12
compartilhamentos = visualizacoes * 0.0179
novasVisualizacoes = 0
if compartilhamentos >= 4:  # o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
    novasVisualizacoes = visualizacoes + (4 * 40)
elif compartilhamentos >= 1:
    novasVisualizacoes = visualizacoes + (compartilhamentos * 40)

print('--' * 20)
print(f'Nome do anúncio: {nomeAnuncio}')
print(f'Cliente: {cliente}')
print(f'Data de início: {dataInicio.strftime("%d/%m/%Y")}')
print(f'Data de término: {dataTermino.strftime("%d/%m/%Y")}')
print(f'Total de {periodoTotal} dias.')
print('O total investido será de R$ {:.2f} reais.'.format(valorTotalInvestido))
print('Projeção aproximada da quantidade máxima de:')
print('     Visualizações: {:.0f}'.format(novasVisualizacoes))
print('     Cliques: {:.0f}'.format(cliques))
print('     Compartilhamentos: {:.0f}'.format(compartilhamentos))
