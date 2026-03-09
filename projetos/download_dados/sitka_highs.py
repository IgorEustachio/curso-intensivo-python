from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#criou uma instância do objeto Path
path = Path('C:\\Users\\SAMSUNG\\Documents\\Igor\\projeto\\python-crash-course\\projetos\\download_dados\\info_clima\\sitka_weather_07-2021_simple.csv') 

lines = path.read_text().splitlines() #armazena o conteúdo do arquivo em uma lista de linhas, usando o método read_text() para ler o conteúdo do arquivo e splitlines() para dividir o texto em linhas individuais.

reader = csv.reader(lines)
header_row = next(reader) #retorna a próxima linha do iterador reader, que é a primeira linha do arquivo CSV, e armazena essa linha na variável header_row. Essa linha geralmente contém os nomes das colunas do arquivo CSV.


#extrai as temperaturas máximas do arquivo CSV e as armazena em uma lista chamada highs. O código percorre cada linha do arquivo CSV usando um loop for, converte o valor da temperatura máxima (que está na coluna de índice 5) para um número inteiro e adiciona esse valor à lista highs.
highs = []
dates = []
lows = []

#utiliza a função enumerate() para percorrer a linha de cabeçalho e exibir simultaneamente o índice (posição) e o nome de cada coluna
for index, column_header in enumerate(header_row):
    colunas = {'Indice': index, 'Nome da Coluna': column_header}
    print(colunas)



for row in reader: #pula a primeira linha do arquivo CSV, que é a linha de cabeçalho, e percorre as linhas restantes usando um loop for
    high = int(row[4]) #o objeto reader já entrega cada linha como uma lista; acessamos a temperatura máxima no índice 4, convertemos para inteiro e guardamos em high
    highs.append(high) #adiciona o valor convertido à lista highs usando o método append()
    date = datetime.strptime(row[2], '%Y-%m-%d') #converte a string da data no índice 2 para um objeto datetime
    dates.append(date) #adiciona o objeto datetime à lista dates
    low = int(row[5])
    lows.append(low)

print(highs)

fig, ax = plt.subplots() #cria uma figura (fix) e um conjunto de eixos (ax) para o gráfico usando a função subplots() da biblioteca Matplotlib
ax.plot(dates, highs, color='red', alpha=0.5) #plota a lista highs em relação às datas usando a função plot() do objeto ax. O argumento c='red' define a cor da linha do gráfico como vermelha
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#formata o gráfico
ax.set_title('Temperaturas Máximas e Mínimas Diárias - Sitka, Julho 2021', fontsize=18) #define o título do gráfico do objeto ax
ax.set_xlabel('', fontsize=16) #define o rótulo do eixo x
fig.autofmt_xdate() #formata as datas no eixo x para que fiquem mais legíveis, usando a função autofmt_xdate() da figura (fig)
ax.set_ylabel('Temperatura (F)', fontsize=16) #define o rótulo do eixo y
ax.tick_params(labelsize=16) #define o tamanho dos rótulos dos ticks (marcadores) nos eixos x e y usando a função tick() do objeto ax. O argumento labelsize=16 define o tamanho da fonte dos rótulos dos ticks como 16

plt.show() #exibe o gráfico