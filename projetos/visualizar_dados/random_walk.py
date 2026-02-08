from random import choice 

class RandomWalk():
    #classe para gerar passeios aleatórios

    def __init__(self, num_points=5000):
        self.num_points = num_points

        #todos os passeios começam no ponto (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #calcula todos os pontos do passeio
        while len(self.x_values) < self.num_points:
            #decide a direção a seguir e a distância a percorrer nessa direção
            x_direction = choice([1, -1]) #escolhe entre mover para a direita (1) ou para a esquerda (-1)
            x_distance = choice([0, 1, 2, 3, 4]) #escolhe uma distância aleatória entre 0 e 4
            x_step = x_direction * x_distance #calcula o passo no eixo x

            y_direction = choice([1, -1]) #escolhe entre mover para cima (1) ou para baixo (-1)
            y_distance = choice([0, 1, 2, 3, 4]) #escolhe uma distância aleatória entre 0 e 4
            y_step = y_direction * y_distance #calcula o passo no eixo y

            #rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue

            #calcula os próximos valores de x e y
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)