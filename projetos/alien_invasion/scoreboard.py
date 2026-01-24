import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    #classe para exibir info da pontuação

    def __init__(self, ai_game): #toda classe relacionada ao fluxo principal do jogo precisa do parametro ai_game
        #inicializa os atributos de pontuação
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #configurações de fonte para informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #prepara a imagem inicial da pontuação
        self.prep_score() 
        self.prep_level()
        self.prep_ships()
        self.prep_high_score()

    def prep_score(self):
        #transforma a pontuação em uma imagem renderizada
        score_str = str(self.stats.score)  #converte o valor numérico da pontuação em uma string para que possa ser processada visualmente
        rounded_score = round(self.stats.score, -1)  #o parâmetro -1 instrui a função a arredondar o valor para o múltiplo de 10 mais próximo
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
        self.text_color, self.settings.bg_color)  #renderiza a string como uma imagem, aplicando suavização (antialising) e as cores de texto e fundo definidas

        #exibe a pontuação no canto superior direito da tela
        self.score_rect = self.score_image.get_rect() #cria um objeto retangular (rect) a partir da imagem renderizada para gerenciar seu posicionamento.
        self.score_rect.right = self.screen_rect.right - 20 #posiciona a borda direita da pontuação com uma margem de 20 pixels em relação ao lado direito da tela.

        self.score_rect.top = 20 #define a localização vertical da pontuação a 20 pixels da parte superior da janela do jogo.

    def check_high_score(self):
        #verifica se há uma nova pontuação máxima"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        #desenha a pontuação na tela com o blit, além do nível e naves restantes
        self.screen.blit(self.score_image, self.score_rect) #desenha a imagem da pontuação atual na tela na posição definida pelo seu retângulo correspondente.
        self.screen.blit(self.high_score_image, self.high_score_rect) #desenha a imagem do recorde histórico na tela na posição centralizada especificada pelo seu retângulo.
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_level(self):
        #transforma o nível em uma imagem renderizada
        level_str = str(self.stats.level) #converte o valor numérico do nível em uma string para que possa ser renderizado como texto.
        self.level_image = self.font.render(level_str, True, 
        self.text_color, self.settings.bg_color) #transforma a string do nível em uma imagem, aplicando suavização e as cores de texto e fundo definidas.
        #posiciona o nível abaixo da pontuação
        self.level_rect = self.level_image.get_rect() #cria um objeto retângulo (rect) para a imagem do nível, permitindo controlar sua posição exata na tela.
        self.level_rect.right = self.score_rect.right #alinha a borda direita do nível com a da pontuação para manter um padrão visual consistente no placar.
        self.level_rect.top = self.score_rect.bottom + 10 #posiciona o indicador de nível 10 pixels abaixo da pontuação para criar um espaçamento organizado.

    def prep_ships(self):
        #mostra as espaçonaves restantes
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_high_score(self):
        #transforma a pontuação em uma imagem renderizada
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score:,}'
        self.high_score_image = self.font.render(high_score_str, True,  
        self.text_color, self.settings.bg_color) #renderiza a string como uma imagem, aplicando suavização (antialising) e as cores de texto e fundo definidas

        # alinha horizontalmente o recorde ao centro da tela; o atributo centerx do objeto rect é utilizado para igualar a posição central do 
        # retângulo da imagem do recorde com a posição central do retângulo da tela, 
        # garantindo que a informação fique centralizada independentemente da largura do número.
        self.high_score_rect = self.high_score_image.get_rect() #transforma a imagem renderiza em um retângulo
        self.high_score_rect.centerx = self.screen_rect.centerx 
        self.high_score_rect.top = self.score_rect.top