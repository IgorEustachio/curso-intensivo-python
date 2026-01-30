import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] #dados do eixo x
squares = [1, 4, 9, 16, 25] #dados do eixo y

#cria uma figura e um conjunto de subplots
fig, ax = plt.subplots() #ax = axes (eixos) = área do gráfico
ax.plot(input_values, squares, linewidth=3) #plota os dados com uma linha de largura 2

plt.show() #abre o visualizador de gráficos do Matplotlib

#métodos que definem o titulo e os eixos dos rótulos

ax.set_title("Números ao Quadrado", fontsize=24) #título do gráfico
ax.set_xlabel("Valor", fontsize=14) #rótulo do eixo x
ax.set_ylabel("Quadrado do Valor", fontsize=14) #rótulo do eixo y

#define o tamanho da fonte dos rótulos de marcação de escala para 14 em ambos os eixos.
ax.tick_params(labelsize=14)