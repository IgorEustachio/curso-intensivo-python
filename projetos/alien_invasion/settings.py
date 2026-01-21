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
        self.ship_limit = 3

        #configs do projétil
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #configs dos aliens
        self.alien_speed = 5.0
        self.fleet_drop_speed = 10
        #fleet_direction de 1 representa a direita e -1 representa a esquerda
        self.fleet_direction = 1