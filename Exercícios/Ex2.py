'''2) Continue o código anterior e construa funções para:
a) Cadastrar compromissos
b) Listar esses compromissos em formato de tabela'''

tabela = []
def cadastrarCompromisso():
    hora = int(input("Digite a hora: "))
    minutos = int(input("Digite os minutos: "))
    segundos = int(input("Digite os segundos: "))
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    compromisso = {
        "horario" : {"hora": hora, "minutos": minutos, "segundos": segundos},
        "data" : {"dia":dia, "mes": mes, "ano": ano}
    }
    print(f'''O seu compromisso foi foi agendado para
    {compromisso["data"]["dia"]}/{compromisso["data"]["mes"]}/{compromisso["data"]["ano"]} -- às {compromisso["horario"]["hora"]}:{compromisso["horario"]["minutos"]}:{compromisso["horario"]["segundos"]} ''')
    

    compro = {
        "nome": str(input("Digite o nome do Compromisso: ")),
        "dataHora": compromisso
    }
    tabela.append(compro)
    return f"{compro['nome']}\n{compromisso['data']['dia']}/{compromisso['data']['mes']}/{compromisso['data']['ano']}\n às {compromisso['horario']['hora']}:{compromisso['horario']['minutos']}:{compromisso['horario']['segundos']}"
print(cadastrarCompromisso())