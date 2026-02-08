from random import randint

class Die():
    #uma classe que representa um dado de seis lados

    def __init__(self, num_sides=6): #ao colocar num_sides=6, o valor padrão do número de lados do dado é 6, mas pode ser alterado ao criar uma instância da classe
        #nicializa o dado com o número de lados especificado
        self.num_sides = num_sides

    def roll(self):
        #Retorna um valor aleatório entre 1 e o número de lados do dado
        return randint(1, self.num_sides)