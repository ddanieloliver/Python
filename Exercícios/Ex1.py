'''1) Escreva um código para armazenar as informações pedidas em cada item abaixo em um
dicionário:
a) Horário: composto por hora, minutos e segundos;
b) Data: composto por dia, mês e ano;
c) Compromisso: composto por data, horário e texto que descreve o compromisso'''

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