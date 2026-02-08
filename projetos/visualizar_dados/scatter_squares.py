import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x_values = range(1, 1001) #eixo x
y_values = [x**2 for x in x_values] #eixo y 

#utiliza o método scatter() para desenhar uma série de pontos nas coordenadas x e y; 
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10) #o parâmetro s estabelece o tamanho (size) do marcador
#o parâmetro c=y_values associa a cor de cada ponto ao seu respectivo valor no eixo y, 
#enquanto cmap=plt.cm.Blues define o mapa de cores integrado "Blues" para criar um gradiente que varia do azul claro (valores baixos) ao azul escuro (valores altos)

#define o título do gráfico e os eixos do rótulo
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#define o tamanho dos rótulos de marcação de escala
ax.tick_params(labelsize=14)

#define o intervalo de visualização de ambos os eixos simultaneamente; 
ax.axis([0, 1100, 0, 1_000_000]) #a lista de quatro valores estabelece que o eixo x variará de 0 a 50, enquanto o eixo y variará de 0 a 1.000.

#Configura a escala dos rótulos para exibir números em formato simples, 
#desativando a notação científica que a biblioteca aplica automaticamente em valores muito elevados
ax.ticklabel_format(style='plain')

plt.savefig('squares_plot.png', bbox_inches='tight') #Salva o gráfico como um arquivo PNG com bordas ajustadas
plt.show() #Exibe o gráfico na tela