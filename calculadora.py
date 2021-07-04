from datetime import datetime

anuncios = []


class Anuncio():
    def __init__(self, nomeAnuncio,
                 cliente,
                 dataInicio,
                 dataTermino,
                 periodoTotal,
                 investimentoPorDia):
        self.nomeAnuncio = nomeAnuncio
        self.cliente = cliente
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.periodoTotal = periodoTotal
        self.investimentoPorDia = investimentoPorDia

    def emitirRelatorio(self):
        valorTotalInvestido = self.periodoTotal * self.investimentoPorDia
        visualizacoes = valorTotalInvestido * 30
        cliques = visualizacoes * 0.12
        compartilhamentos = visualizacoes * 0.0179
        novasVisualizacoes = 0
        if compartilhamentos >= 4:  # o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
            novasVisualizacoes = visualizacoes + (4 * 40)
        elif compartilhamentos >= 1:
            novasVisualizacoes = visualizacoes + (compartilhamentos * 40)

        print(f'Nome do anúncio: {self.nomeAnuncio}')
        print(f'Cliente: {self.cliente}')
        print(f'Data de início: {self.dataInicio.strftime("%d/%m/%Y")}')
        print(f'Data de término: {self.dataTermino.strftime("%d/%m/%Y")}')
        print(f'Total de {self.periodoTotal} dias.')
        print('O total investido será de R$ {:.2f} reais.'.format(valorTotalInvestido))
        print('Projeção aproximada da quantidade máxima de:')
        print('     Visualizações: {:.0f}'.format(novasVisualizacoes))
        print('     Cliques: {:.0f}'.format(cliques))
        print('     Compartilhamentos: {:.0f}'.format(compartilhamentos))
        print('--' * 20)


def cadastrarAnuncio(args):
    nomeAnuncio = str(input('Nome do anúncio: ')).capitalize().strip()
    cliente = str(input('Cliente: ')).capitalize().strip()
    dataInicio = datetime.strptime(input('Data de início (dd/mm/aaaa): '), '%d/%m/%Y')
    dataTermino = datetime.strptime(input('Data de término (dd/mm/aaaa): '), '%d/%m/%Y')
    periodoTotal = abs((dataTermino - dataInicio).days)
    investimentoPorDia = float(input('Investimento por dia: R$ '))
    anuncio = Anuncio(nomeAnuncio, cliente, dataInicio, dataTermino, periodoTotal, investimentoPorDia)
    anuncios.append(anuncio)


def emitirRelatorio(args):
    print('')
    for anuncio in anuncios:
        anuncio.emitirRelatorio()


def filtrarAnunciosCliente(args):
    filtroCliente = str(input('Digite o nome do cliente: ')).upper().strip()
    if filtroCliente != '':
        for anuncio in anuncios:
            if filtroCliente in anuncio.cliente.upper():
                anuncio.emitirRelatorio()


def filtrarAnunciosIntervalo(args):
    dataInicioInput = input('Data de início do intervalo (dd/mm/aaaa): ').strip()
    dataTerminoInput = input('Data de término do intervalo (dd/mm/aaaa): ').strip()
    dataInicio = dataTermino = None

    if dataInicioInput != '' or dataTerminoInput != '':
        if dataInicioInput != '':
            dataInicio = datetime.strptime(dataInicioInput, '%d/%m/%Y')
        if dataTerminoInput != '':
            dataTermino = datetime.strptime(dataTerminoInput, '%d/%m/%Y')

        for anuncio in anuncios:
            print(f'dataInicio: {dataInicio}')
            print(f'dataTermino: {dataTermino}')
            print(f'anuncio.dataInicio: {anuncio.dataInicio}')
            print(f'anuncio.dataTermino: {anuncio.dataTermino}')
            if dataInicio is not None and anuncio.dataInicio >= dataInicio and dataTermino is not None and anuncio.dataTermino <= dataTermino:
                anuncio.emitirRelatorio()
            elif dataTermino is None and dataInicio is not None and anuncio.dataInicio >= dataInicio:
                anuncio.emitirRelatorio()
            elif dataInicio is None and dataTermino is not None and anuncio.dataTermino <= dataTermino:
                anuncio.emitirRelatorio()
    else:
        print('Opção inválida! Informe ao menos uma data.')


def filtrarAnuncios(args):
    filtro = 0
    while filtro != 3:
        print('''Filtrar por:     
        [ 1 ] Cliente
        [ 2 ] Intervalo de tempo
        [ 3 ] Retornar menu inicial''')
        filtro = int(input('Qual é a sua opção?'))
        if filtro == 1:
            filtrarAnunciosCliente('')
        elif filtro == 2:
            filtrarAnunciosIntervalo('')
        elif filtro == 3:
            print('Pesquisa encerrada!')
        else:
            print('Opção inválida. Tente novamente.')


def strToDate(data):
    return datetime.strptime(data, '%d/%m/%Y')


def executar(args):
    anuncios.append(Anuncio('flores', 'iasmini', strToDate('01/03/2021'), strToDate('30/03/2021'), 30, 5))
    anuncios.append(Anuncio('baby', 'larissa', strToDate('01/04/2021'), strToDate('30/04/2021'), 30, 5))
    anuncios.append(Anuncio('gatinhos', 'felipe', strToDate('01/05/2021'), strToDate('30/05/2021'), 30, 5))
    opcao = 0
    while opcao != 4:
        print('''Informe a opção desejada:     
        [ 1 ] Cadastrar anúncio
        [ 2 ] Emitir relatório 
        [ 3 ] Filtrar anúncios
        [ 4 ] Encerrar''')
        opcao = int(input('Qual é a sua opção?'))
        if opcao == 1:
            cadastrarAnuncio('')
        elif opcao == 2:
            emitirRelatorio('')
        elif opcao == 3:
            filtrarAnuncios('')
        elif opcao == 4:
            print('Programa encerrado!')
        else:
            print('Opção inválida. Tente novamente.')


executar('')
