import pygame.font

class Scoreboard():
    #classe para exibir info da pontuação

    def __init__(self, ai_game): #toda classe relacionada ao fluxo principal do jogo precisa do parametro ai_game
        """Inicializa os atributos de pontuação"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #configurações de fonte para informações de pontuação
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        #prepara a imagem inicial da pontuação
        self.prep_score() 

    def prep_score(self):
        #transforma a pontuação em uma imagem renderizada
        score_str = str(self.stats.score)  #converte o valor numérico da pontuação em uma string para que possa ser processada visualmente
        self.score_image = self.font.render(score_str, True,
        self.text_color, self.settings.bg_color)  #renderiza a string como uma imagem, aplicando suavização (antialising) e as cores de texto e fundo definidas

        #exibe a pontuação no canto superior direito da tela
        self.score_rect = self.score_image.get_rect() #cria um objeto retangular (rect) a partir da imagem renderizada para gerenciar seu posicionamento.
        self.score_rect.right = self.screen_rect.right - 20 #posiciona a borda direita da pontuação com uma margem de 20 pixels em relação ao lado direito da tela.

        self.score_rect.top = 20 #define a localização vertical da pontuação a 20 pixels da parte superior da janela do jogo.

    def show_score(self):
        #desenha a pontuação na tela
        self.screen.blit(self.score_image, self.score_rect)
