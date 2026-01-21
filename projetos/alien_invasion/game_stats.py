class GameStats:
    #rastreia as estatisticas do Alien Invasion

    def __init__(self, ai_game): #toda classe relacionada ao fluxo principal do jogo precisa do parametro ai_game
        #inicializa as estastísticas
        self.settings = ai_game.settings
        self.resets_stats()

    def resets_stats(self):
        #inicializa as estatísticas que mudam durante o jogo
        self.ships_left = self.settings.ship_limit