import pygame.font

class Button():
    #classe para criar botões para o jogo

    def __init__(self, ai_game, msg): #toda classe relacionada ao fluxo principal do jogo precisa do parametro ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #defina as propriedades e atributos do botão
        self.width, self.height = 200,50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #prepara a fonte padrão (None) do sistema com tamanho 48 para renderizar texto no jogo. 

        self.rect = pygame.Rect(0,0, self.width, self.height) #cria o objeto rect do botão nas coordenadas iniciais (0,0) com a largura e altura especificadas.
        self.rect.center = self.screen_rect.center

        #a mensagem do botão precisa ser preparada apenas uma vez
        self._prep_msg(msg)

    def _prep_msg(self,msg):
        #transforma msg em uma imagem renderizada e centraliza texto no botão
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color) #converte o texto em imagem (Play), suaviza as bordas (antialiasing) e define as cores do texto e do fundo.
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #desenha o botão em branco e depois desenhe a mensagem
        self.screen.fill(self.button_color, self.rect) #preenche a parte retangular do botão com a cor de fundo definida nas configurações.
        self.screen.blit(self.msg_image, self.msg_image_rect) #desenha a imagem da mensagem de texto sobreposta ao botão na tela.