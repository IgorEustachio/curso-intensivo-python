import matplotlib.pyplot as plt
from random_walk import RandomWalk

#Cria um passeio aleatório e preenche os pontos do passeio
rw = RandomWalk(50_000) #parametro que define o número de pontos no passeio
rw.fill_walk()

while True: 
    #plota os pontos do passeio aleatório
    plt.style.use('classic') #define o estilo clássico para o gráfico
    fig, ax = plt.subplots(figsize=(15, 9)) #define o tamanho da figura
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_title("Random Walk", fontsize=24)
    ax.set_aspect('equal') #define a proporção igual para os eixos x e y
    
    #destaca o primeiro e o último ponto
    ax.scatter(0, 0, c='darkblue', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='lightblue', edgecolors='none',
    s=100)


    #remove os eixos
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("fazer outro mapa aleatório? (s/n): ")
    if keep_running == 'n':
        break