from datetime import datetime

# Obter a data e hora atual
data_atual = datetime.now()

# Convertendo para String
data_convertida = data_atual.strftime('%Y-%m-%d')
hora_atual = data_atual.strftime('%H:%M:%S')

# Imprimindo a data e hora atuais
print('Data atual: ', data_convertida)
print('Hora atual: ', hora_atual)
