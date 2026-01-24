class GameStats:
    # rastreia as estatísticas do Alien Invasion

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        # recorde não é redefinido
        self.high_score = 0

    def reset_stats(self):
        #estatísticas que mudam durante o jogo
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1