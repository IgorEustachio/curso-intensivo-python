class Settings():
    #classe para armazenar as configurações do jogo Alien Invasion 
    def __init__(self):
        #inicializa as configs do jogo
        #configurações da tela 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #configs da espaçonave
        self.ship_speed = 1.5

        #configs do projétil
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10