class Settings():
    #classe para armazenar as configurações do jogo Alien Invasion 
    def __init__(self): #toda classe relacionada ao fluxo principal do jogo precisa do parametro ai_game
        #inicializa as configs do jogo que não mudam
        #configurações da tela 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #configs da espaçonave
        self.ship_limit = 3

        #configs do projétil
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #configs dos aliens
        self.fleet_drop_speed = 10

        #velocidade em que o jogo acelera a cada nível
        self.speedup_scale = 1.1

        #com que rapidez os valores dos pontos alienígenas aumentam
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        #configurações de pontuação
        self.alien_points = 50

    def initialize_dynamic_settings(self):
        #inicializa as configurações que mudam durante o jogo
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #fleet_direction de 1 representa a direita e de - 1 a esquerda
        self.fleet_direction = 1

    def increase_speed(self):
        #aumenta as configs de velocidade
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
